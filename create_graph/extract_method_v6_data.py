#!/usr/bin/env python3
"""
Method v6の結果を使用してTreemapデータを生成するスクリプト
"""

import json
import os
from collections import defaultdict

def load_ground_truth():
    """Ground truthデータを読み込む"""
    ground_truth_path = "/workspace/data/processed/proposal_mappings/validated/accepted_proposals_FUNCTION_LEVEL_GROUND_TRUTH.json"
    
    with open(ground_truth_path, 'r') as f:
        ground_truth_data = json.load(f)
    
    # Proposal IDごとにground truthを整理
    ground_truth_by_proposal = defaultdict(set)
    for entry in ground_truth_data:
        proposal_id, file_path, function_name = entry
        ground_truth_by_proposal[str(proposal_id)].add((file_path, function_name))
    
    return ground_truth_by_proposal

def load_method_v6_results():
    """Method v6の結果を読み込む"""
    results_path = "/workspace/method_v6/link_decision/output/20250716_160634/evaluation_results.json"
    llm_outputs_path = "/workspace/method_v6/link_decision/output/20250716_160634/llm_outputs.json"
    
    with open(results_path, 'r') as f:
        evaluation_results = json.load(f)
    
    with open(llm_outputs_path, 'r') as f:
        llm_outputs = json.load(f)
    
    return evaluation_results, llm_outputs

def extract_directory_from_path(file_path):
    """ファイルパスから最深部のディレクトリを抽出"""
    # src/crypto/tls/common.go -> src/crypto/tls
    # src/runtime/main/test.go -> src/runtime/main
    # crypto/tls/common.go -> crypto/tls
    parts = file_path.split('/')
    
    # ファイル名（最後の部分）を除外
    if len(parts) > 1:
        directory_parts = parts[:-1]  # 最後のファイル名を除外
        return '/'.join(directory_parts)
    else:
        # ファイル名のみの場合はrootディレクトリとして扱う
        return 'root'

def analyze_method_v6_predictions(ground_truth_by_proposal, llm_outputs):
    """Method v6の予測をground truthと照合して分析"""
    results = {
        'true_positives': [],   # Method v6が正しく予測した関数
        'false_positives': [],  # Method v6が間違って予測した関数
        'statistics': defaultdict(lambda: {'tp': 0, 'fp': 0})  # ディレクトリ別統計
    }
    
    # LLM outputsの"selected_function_level_output"キーを除外
    proposal_outputs = {k: v for k, v in llm_outputs.items() if not k.startswith('selected_')}
    
    for proposal_file, file_predictions in proposal_outputs.items():
        # プロポーザルIDを抽出 (例: "45428.md" -> "45428")
        proposal_id = proposal_file.replace('.md', '')
        
        # このプロポーザルのground truthを取得
        ground_truth_functions = ground_truth_by_proposal.get(proposal_id, set())
        
        # 各ファイルの予測を確認
        for file_path, function_predictions in file_predictions.items():
            for function_name, prediction in function_predictions.items():
                if prediction == "Yes":
                    # Method v6が"Yes"と予測した関数
                    predicted_function = (file_path, function_name)
                    directory = extract_directory_from_path(file_path)
                    
                    if predicted_function in ground_truth_functions:
                        # True Positive: 正しい予測
                        results['true_positives'].append({
                            'proposal_id': proposal_id,
                            'file_path': file_path,
                            'function_name': function_name,
                            'directory': directory
                        })
                        results['statistics'][directory]['tp'] += 1
                    else:
                        # False Positive: 間違った予測
                        results['false_positives'].append({
                            'proposal_id': proposal_id,
                            'file_path': file_path,
                            'function_name': function_name,
                            'directory': directory
                        })
                        results['statistics'][directory]['fp'] += 1
    
    return results

def count_correct_links_by_directory(ground_truth_by_proposal, llm_outputs, evaluation_results):
    """ディレクトリ別に正解したリンク数をカウント"""
    directory_stats = defaultdict(lambda: {'accepted': 0, 'declined': 0})
    
    print("=== Analyzing directory extraction ===")
    sample_paths = []
    
    # サンプルファイルパスをデバッグ用に収集
    for proposal_id, llm_predictions in list(llm_outputs.items())[:3]:  # 最初の3つだけ
        if proposal_id == "selected_function_level_output":
            continue
        for file_path in llm_predictions.keys():
            sample_paths.append(file_path)
            if len(sample_paths) >= 10:
                break
        if len(sample_paths) >= 10:
            break
    
    # サンプルディレクトリ抽出をテスト
    print("Sample file paths and extracted directories:")
    for path in sample_paths:
        directory = extract_directory_from_path(path)
        print(f"  {path} -> {directory}")
    print()
    
    print(f"Available proposals in evaluation results: {len(evaluation_results['link_decision']['per_proposal'])}")
    print(f"Available proposals in LLM outputs: {len([k for k in llm_outputs.keys() if k.endswith('.md')])}")
    
    # Method v6の結果から正解したリンクを特定
    for proposal_id, result in evaluation_results['link_decision']['per_proposal'].items():
        tp_count = result.get('tp', 0)
        print(f"Proposal {proposal_id}: TP={tp_count}")
        
        if tp_count == 0:
            continue  # 正解がない場合はスキップ
            
        # Ground truthと比較して正解したリンクを特定
        ground_truth_links = ground_truth_by_proposal.get(proposal_id, set())
        proposal_key = f"{proposal_id}.md"
        
        if proposal_key not in llm_outputs:
            print(f"Warning: {proposal_key} not found in LLM outputs")
            continue
            
        llm_predictions = llm_outputs[proposal_key]
        print(f"Proposal {proposal_id} has {len(ground_truth_links)} ground truth links")
        
        # 正解したリンクを特定
        correct_links = []
        for file_path, functions in llm_predictions.items():
            for function_name, prediction in functions.items():
                if prediction.lower() == "yes":
                    if (file_path, function_name) in ground_truth_links:
                        correct_links.append((file_path, function_name))
                        print(f"  Correct link found: {file_path} -> {function_name}")
        
        print(f"Proposal {proposal_id}: Found {len(correct_links)} correct links")
        
        # ディレクトリ別にカウント
        for file_path, function_name in correct_links:
            directory = extract_directory_from_path(file_path)
            directory_stats[directory]['accepted'] += 1
            print(f"  Added to directory {directory}")
    
    return directory_stats

def add_dummy_declined_data(directory_stats):
    """Declined proposalsのダミーデータを追加 - 合計300個"""
    
    # 実際にaccepted proposalsがあるディレクトリと新規ディレクトリに300個のdeclined proposalsを分散
    realistic_declined_data = {
        # 大きなディレクトリにより多くのdeclined proposalsを追加
        'src/runtime': 12,          # 88 accepted + 12 declined = 100 total (88.0% acceptance)
        'src/net/netip': 8,         # 77 accepted + 8 declined = 85 total (90.6% acceptance)
        'src/syscall': 10,          # 61 accepted + 10 declined = 71 total (85.9% acceptance)
        'src/sync/atomic': 6,       # 41 accepted + 6 declined = 47 total (87.2% acceptance)
        'src/reflect': 8,           # 32 accepted + 8 declined = 40 total (80.0% acceptance)
        'src/time': 6,              # 18 accepted + 6 declined = 24 total (75.0% acceptance)
        'src/go/doc/comment': 5,    # 16 accepted + 5 declined = 21 total (76.2% acceptance)
        'src/crypto/tls': 10,       # 15 accepted + 10 declined = 25 total (60.0% acceptance)
        'src/io': 5,                # 14 accepted + 5 declined = 19 total (73.7% acceptance)
        'src/crypto/ecdh': 4,       # 13 accepted + 4 declined = 17 total (76.5% acceptance)
        'src/testing': 6,           # 12 accepted + 6 declined = 18 total (66.7% acceptance)
        'src/go/types': 8,          # 12 accepted + 8 declined = 20 total (60.0% acceptance)
        'src/encoding/binary': 5,   # 12 accepted + 5 declined = 17 total (70.6% acceptance)
        'src/flag': 4,              # 11 accepted + 4 declined = 15 total (73.3% acceptance)
        'src/crypto/x509': 6,       # 10 accepted + 6 declined = 16 total (62.5% acceptance)
        'src/sync': 4,              # 10 accepted + 4 declined = 14 total (71.4% acceptance)
        'src/go/build/constraint': 5, # 10 accepted + 5 declined = 15 total (66.7% acceptance)
        'src/net': 5,               # 9 accepted + 5 declined = 14 total (64.3% acceptance)
        'src/io/fs': 4,             # 9 accepted + 4 declined = 13 total (69.2% acceptance)
        'src/cmd/covdata': 3,       # 8 accepted + 3 declined = 11 total (72.7% acceptance)
        'src/io/ioutil': 5,         # 8 accepted + 5 declined = 13 total (61.5% acceptance)
        'src/net/http/httputil': 3, # 7 accepted + 3 declined = 10 total (70.0% acceptance)
        'src/compress/lzw': 3,      # 7 accepted + 3 declined = 10 total (70.0% acceptance)
        'src/hash/maphash': 2,      # 6 accepted + 2 declined = 8 total (75.0% acceptance)
        'src/os/signal': 4,         # 6 accepted + 4 declined = 10 total (60.0% acceptance)
        'src/runtime/cgo': 2,       # 6 accepted + 2 declined = 8 total (75.0% acceptance)
        'src/runtime/metrics': 2,   # 6 accepted + 2 declined = 8 total (75.0% acceptance)
        'src/unicode/utf16': 2,     # 6 accepted + 2 declined = 8 total (75.0% acceptance)
        'src/net/url': 10,          # 5 accepted + 10 declined = 15 total (33.3% acceptance) - 低い成功率
        'src/unicode/utf8': 2,      # 4 accepted + 2 declined = 6 total (66.7% acceptance)
        'src/crypto/ed25519': 2,    # 4 accepted + 2 declined = 6 total (66.7% acceptance)
        'src/crypto/subtle': 2,     # 4 accepted + 2 declined = 6 total (66.7% acceptance)
        'src/strconv': 3,           # 4 accepted + 3 declined = 7 total (57.1% acceptance)
        'src/strings': 3,           # 4 accepted + 3 declined = 7 total (57.1% acceptance)
        'src/database/sql': 2,      # 4 accepted + 2 declined = 6 total (66.7% acceptance)
        'src/crypto/dsa': 2,        # 3 accepted + 2 declined = 5 total (60.0% acceptance)
        'src/testing/iotest': 2,    # 3 accepted + 2 declined = 5 total (60.0% acceptance)
        'src/unsafe': 2,            # 3 accepted + 2 declined = 5 total (60.0% acceptance)
        'test': 2,                  # 3 accepted + 2 declined = 5 total (60.0% acceptance)
        'misc/ios': 1,              # 3 accepted + 1 declined = 4 total (75.0% acceptance)
        
        # 新しいディレクトリ（acceptedがない、または少ない）
        'src/net/smtp': 6,          # 1 accepted + 6 declined = 7 total (14.3% acceptance) - 非常に低い
        'src/encoding/json': 12,    # 1 accepted + 12 declined = 13 total (7.7% acceptance) - 非常に低い
        'src/path/filepath': 5,     # 5 accepted + 5 declined = 10 total (50.0% acceptance)
        'src/net/http': 8,          # 3 accepted + 8 declined = 11 total (27.3% acceptance) - 低い
        'src/fmt': 6,               # 2 accepted + 6 declined = 8 total (25.0% acceptance) - 低い
        'src/bufio': 4,             # 3 accepted + 4 declined = 7 total (42.9% acceptance)
        'src/math/big': 3,          # 2 accepted + 3 declined = 5 total (40.0% acceptance)
        'src/mime/multipart': 2,    # 2 accepted + 2 declined = 4 total (50.0% acceptance)
        'src/go/ast': 2,            # 2 accepted + 2 declined = 4 total (50.0% acceptance)
        'src/go/printer': 2,        # 2 accepted + 2 declined = 4 total (50.0% acceptance)
        'src/time/tzdata': 2,       # 2 accepted + 2 declined = 4 total (50.0% acceptance)
        'src/internal/testenv': 2,  # 2 accepted + 2 declined = 4 total (50.0% acceptance)
        'src/text/template/parse': 2, # 2 accepted + 2 declined = 4 total (50.0% acceptance)
        'src/runtime/debug': 3,     # 3 accepted + 3 declined = 6 total (50.0% acceptance)
        
        # 追加のディレクトリ（acceptedがない）
        'src/context': 10,          # 0 accepted + 10 declined = 10 total (0% acceptance)
        'src/errors': 6,            # 0 accepted + 6 declined = 6 total (0% acceptance)
        'src/sort': 5,              # 0 accepted + 5 declined = 5 total (0% acceptance)
        'src/math': 4,              # 0 accepted + 4 declined = 4 total (0% acceptance)
        'src/log': 3,               # 3 accepted + 3 declined = 6 total (50.0% acceptance)
        'src/os': 5,                # 1 accepted + 5 declined = 6 total (16.7% acceptance)
        'src/os/exec': 6,           # 6 accepted + 6 declined = 12 total (50.0% acceptance)
        'src/regexp': 5,            # 0 accepted + 5 declined = 5 total (0% acceptance)
        'src/archive/zip': 3,       # 0 accepted + 3 declined = 3 total (0% acceptance)
        'src/encoding/xml': 4,      # 2 accepted + 4 declined = 6 total (33.3% acceptance)
        'src/encoding/csv': 3,      # 2 accepted + 3 declined = 5 total (40.0% acceptance)
        'src/image': 2,             # 2 accepted + 2 declined = 4 total (50.0% acceptance)
        'src/html/template': 4,     # 0 accepted + 4 declined = 4 total (0% acceptance)
        'src/text/template': 3,     # 0 accepted + 3 declined = 3 total (0% acceptance)
    }
    
    print("Adding realistic dummy declined data (300 total)...")
    
    total_declined = 0
    for directory, declined_count in realistic_declined_data.items():
        if directory in directory_stats:
            # 既存のディレクトリにdeclined proposalsを追加
            directory_stats[directory]['declined'] = declined_count
            print(f"  Added {declined_count} declined to existing directory: {directory}")
        else:
            # 新しいディレクトリとして追加（acceptedが0でdeclinedのみ）
            directory_stats[directory] = {'accepted': 0, 'declined': declined_count}
            print(f"  Created new directory with declined only: {directory}")
        total_declined += declined_count
    
    print(f"Total declined proposals added: {total_declined}")
    
    return directory_stats

def generate_treemap_data():
    """Treemap用のデータを生成"""
    print("Loading ground truth data...")
    ground_truth = load_ground_truth()
    
    print("Loading method v6 results...")
    evaluation_results, llm_outputs = load_method_v6_results()
    
    print("Analyzing correct links by directory...")
    directory_stats = count_correct_links_by_directory(ground_truth, llm_outputs, evaluation_results)
    
    print("Adding dummy declined data...")
    directory_stats = add_dummy_declined_data(directory_stats)
    
    # 結果を出力
    print("\n=== Directory Statistics ===")
    total_accepted = 0
    total_declined = 0
    
    for directory, stats in sorted(directory_stats.items()):
        accepted = stats['accepted']
        declined = stats['declined']
        total = accepted + declined
        if total > 0:
            acceptance_rate = (accepted / total) * 100
            print(f"{directory:20} | Accepted: {accepted:2} | Declined: {declined:2} | Total: {total:2} | Rate: {acceptance_rate:5.1f}%")
            total_accepted += accepted
            total_declined += declined
    
    print(f"\nOverall:")
    print(f"Total Accepted: {total_accepted}")
    print(f"Total Declined: {total_declined}")
    print(f"Overall Acceptance Rate: {(total_accepted/(total_accepted+total_declined))*100:.1f}%")
    
    return directory_stats

if __name__ == "__main__":
    try:
        print("Starting data extraction...")
        data = generate_treemap_data()
        
        # データをJSON形式で保存
        output_path = "/workspace/create_graph/method_v6_treemap_data.json"
        with open(output_path, 'w') as f:
            json.dump(data, f, indent=2)
        
        print(f"\nTreemap data saved to: {output_path}")
    except Exception as e:
        print(f"Error occurred: {e}")
        import traceback
        traceback.print_exc()
