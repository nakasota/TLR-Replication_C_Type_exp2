#!/usr/bin/env python3
"""
MERGED状態のCLのみを対象としたGround Truth作成スクリプト
現在のリポジトリで実装されている関数のみを含む、クリーンなground truthを作成する
（MERGED状態のCLのみを使用）
変更内容の検証機能付き
"""

import json
import os
from pathlib import Path
from content_validator import ContentValidator
from repo_loader import GoRepoLoader
from tqdm import tqdm
import logging

# ログ設定
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def create_ground_truth():
    """メイン処理：MERGED状態のCLのみからground truthを作成"""
    
    # 入力ファイル
    func_analysis_path = "../data/ground_truth/accepted_proposals_func_analysis_merged_validated.json"
    repo_structure_path = "../data/ground_truth/go_repo_structure.json"
    output_path = "../data/ground_truth/accepted_proposals_ground_truth_content_validated.json"
    
    print("🚀 Ground Truth作成開始（MERGED状態のCL + 変更内容厳格検証）")
    print(f"📁 関数解析データ: {func_analysis_path}")
    print(f"📁 リポジトリ構造: {repo_structure_path}")
    print(f"💾 出力ファイル: {output_path}")
    
    # ファイル存在チェック
    for p in [func_analysis_path, repo_structure_path]:
        if not os.path.exists(p):
            print(f"❌ ファイルが見つかりません: {p}")
            return
    
    # リポジトリローダーと変更内容検証器を初期化
    print("🔧 リポジトリローダーと変更内容検証器を初期化中...")
    repo_loader = GoRepoLoader(repo_structure_path)
    content_validator = ContentValidator(repo_loader)
    
    # リポジトリ構造をロード
    print("📖 リポジトリ構造を読み込み中...")
    with open(repo_structure_path, 'r', encoding='utf-8') as f:
        repo_data = json.load(f)
    
    # ファイルパスと関数の効率的な検索用データ構造
    repo_files = set(repo_data.keys())
    repo_file_functions = {
        fp: set(d['functions'].keys()) 
        for fp, d in repo_data.items() 
        if 'functions' in d
    }
    
    print(f"✓ リポジトリファイル数: {len(repo_files)}")
    print(f"✓ 関数を持つファイル数: {len(repo_file_functions)}")
    
    # 関数解析データをロード
    print("📖 関数解析データを読み込み中...")
    with open(func_analysis_path, 'r', encoding='utf-8') as f:
        func_analysis = json.load(f)
    
    results = func_analysis.get('results', [])
    statistics = func_analysis.get('statistics', {})
    print(f"✓ 解析済み提案数: {len(results)}")
    print(f"✓ MERGED状態のCL数: {statistics.get('merged_cls_count', 'N/A')}")
    
    # Ground truthを作成
    print("🔍 Ground truth作成中（変更内容検証付き）...")
    ground_truth = []
    
    matched_proposals = 0
    total_matched_files = 0
    total_matched_functions = 0
    total_merged_cls = 0
    content_validated_functions = 0
    content_validation_stats = {
        'content_matches': 0,        # 追加行が存在しGround Truth認定
        'content_differs': 0,        # 追加行が存在するが一致せずGround Truth除外
        'validation_errors': 0
    }
    ground_truth_qualified = 0      # 追加行検証でGround Truth認定
    ground_truth_rejected = 0       # 追加行なしまたは不一致でGround Truth除外
    
    # 進捗表示のために提案をループ
    try:
        from tqdm import tqdm
        proposal_iterator = tqdm(results, desc="提案処理中", unit="提案")
    except ImportError:
        print("tqdmが利用できないため、シンプルな進捗表示を使用します...")
        proposal_iterator = results
    
    for i, proposal in enumerate(proposal_iterator):
        # tqdmが利用できない場合の進捗表示
        if not hasattr(proposal_iterator, 'set_postfix'):
            if i % 10 == 0 or i == len(results) - 1:
                print(f"進捗: {i+1}/{len(results)} 提案処理中... (MERGED CL: {total_merged_cls}, GT関数: {ground_truth_qualified})")
        
        try:
            # 提案ID（ファイル名から抽出）
            proposal_file = proposal.get('proposal_file', '')
            proposal_id = Path(proposal_file).stem if proposal_file else 'unknown'
            
            # この提案で一致するファイルと関数を収集
            matched_files = set()
            matched_functions = []
            merged_cl_count = 0
            
            for cl_analysis in proposal.get('cl_analyses', []):
                # MERGED状態の確認（念のため再チェック）
                if cl_analysis.get('status', '').upper() == 'MERGED':
                    merged_cl_count += 1
                    
                    for file_data in cl_analysis.get('files', []):
                        file_path = file_data.get('file_path')
                        ast_analysis = file_data.get('ast_analysis', {})
                        detected_functions = ast_analysis.get('detected_functions', [])
                        
                        # ファイルがリポジトリに存在するかチェック
                        if file_path in repo_files:
                            repo_funcs = repo_file_functions.get(file_path, set())
                            
                            # このファイルで一致する関数
                            file_matched_functions = []
                            for func in detected_functions:
                                func_name = func.get('function_name')
                                if func_name and func_name in repo_funcs:
                                    # 基本情報を収集
                                    basic_func_info = {
                                        'function_name': func_name,
                                        'file_path': file_path,
                                        'start_line': func.get('start_line'),
                                        'end_line': func.get('end_line'),
                                        'cl_number': cl_analysis.get('cl_number'),
                                        'cl_status': cl_analysis.get('status')
                                    }
                                    
                                    # 変更内容の検証を実行
                                    content_validation = None
                                    is_qualified_ground_truth = False  # デフォルトはFalse
                                    
                                    try:
                                        # CLの変更情報を取得（追加行のみ）
                                        changed_lines = file_data.get('changed_lines', [])
                                        cl_added_lines = [
                                            line.get('content', '') 
                                            for line in changed_lines 
                                            if line.get('type') == 'added'
                                        ]
                                        
                                        # 変更内容の検証（追加行が必須）
                                        if cl_added_lines:
                                            content_validation = content_validator.validate_function_content(
                                                func_name=func_name,
                                                file_path=file_path,
                                                cl_added_lines=cl_added_lines,
                                                func_start_line=func.get('start_line', 1),
                                                func_end_line=func.get('end_line', 1)
                                            )
                                            
                                            # Ground Truth判定を更新
                                            is_qualified_ground_truth = content_validation.get('is_ground_truth', False)
                                            
                                            # Ground Truth統計を更新
                                            if is_qualified_ground_truth:
                                                ground_truth_qualified += 1
                                            else:
                                                ground_truth_rejected += 1
                                            
                                            # 統計を更新
                                            validation_status = content_validation.get('validation_status', 'error')
                                            if validation_status in content_validation_stats:
                                                content_validation_stats[validation_status] += 1
                                            else:
                                                content_validation_stats['validation_errors'] += 1
                                            
                                            content_validated_functions += 1
                                        else:
                                            # 追加行がない場合はGround Truthとして認定しない
                                            is_qualified_ground_truth = False
                                            ground_truth_rejected += 1
                                        
                                    except Exception as e:
                                        logging.error(f"Content validation error for {func_name}: {str(e)}")
                                        content_validation_stats['validation_errors'] += 1
                                    
                                    # Ground Truthとして認定された場合のみ追加
                                    if is_qualified_ground_truth:
                                        # 検証結果を関数情報に追加
                                        if content_validation:
                                            basic_func_info['content_validation'] = content_validation
                                        
                                        file_matched_functions.append(basic_func_info)
                            
                            # 一致する関数があれば記録
                            if file_matched_functions:
                                matched_files.add(file_path)
                                matched_functions.extend(file_matched_functions)
            
            # 一致するファイル・関数があれば ground truth に追加
            if matched_files and matched_functions:
                ground_truth_entry = {
                    'proposal_id': proposal_id,
                    'proposal_file': proposal_file,
                    'merged_cl_count': merged_cl_count,
                    'files': sorted(list(matched_files)),  # ソートして一貫性を保つ
                    'detected_functions': matched_functions
                }
                
                ground_truth.append(ground_truth_entry)
                matched_proposals += 1
                total_matched_files += len(matched_files)
                total_matched_functions += len(matched_functions)
                total_merged_cls += merged_cl_count
                
        except Exception as e:
            logging.error(f"Error processing proposal {proposal_id}: {str(e)}")
            print(f"⚠️  提案 {proposal_id} の処理中にエラーが発生しました: {str(e)}")
            # エラーが発生しても処理を続行
            continue
    
    print(f"✅ Ground truth作成完了！")
    print(f"📊 統計:")
    print(f"├─ 一致した提案数: {matched_proposals}")
    print(f"├─ 総MERGED CL数: {total_merged_cls}")
    print(f"├─ 総ファイル数: {total_matched_files}")
    print(f"├─ 総関数数: {total_matched_functions}")
    print(f"├─ 変更内容検証済み関数数: {content_validated_functions}")
    print(f"├─ 平均ファイル/提案: {total_matched_files/matched_proposals:.2f}")
    print(f"├─ 平均関数/提案: {total_matched_functions/matched_proposals:.2f}")
    print(f"└─ 平均MERGED CL/提案: {total_merged_cls/matched_proposals:.2f}")
    
    print(f"\n🔍 変更内容検証統計:")
    print(f"├─ 追加行あり & 内容一致（Ground Truth認定）: {content_validation_stats['content_matches']}件")
    print(f"├─ 追加行あり & 内容不一致（Ground Truth除外）: {content_validation_stats['content_differs']}件")
    print(f"├─ 検証エラー: {content_validation_stats['validation_errors']}件")
    print(f"├─ Ground Truth認定済み: {ground_truth_qualified}件")
    print(f"└─ Ground Truth除外済み: {ground_truth_rejected}件（追加行なし含む）")
    
    # JSONファイルに保存
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    final_result = {
        "ground_truth": ground_truth,
        "metadata": {
            "total_proposals": matched_proposals,
            "total_merged_cls": total_merged_cls,
            "total_files": total_matched_files,
            "total_functions": total_matched_functions,
            "content_validated_functions": content_validated_functions,
            "content_validation_stats": content_validation_stats,
            "ground_truth_qualified": ground_truth_qualified,
            "ground_truth_rejected": ground_truth_rejected,
            "source_statistics": statistics
        }
    }
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(final_result, f, ensure_ascii=False, indent=2)
    
    print(f"💾 結果を保存: {output_path}")
    
    # サンプル表示
    if ground_truth:
        print(f"\n📝 サンプル提案:")
        sample = ground_truth[0]
        print(f"├─ ID: {sample['proposal_id']}")
        print(f"├─ MERGED CL数: {sample['merged_cl_count']}")
        print(f"├─ ファイル数: {len(sample['files'])}")
        print(f"├─ 関数数: {len(sample['detected_functions'])}")
        print(f"└─ 最初の3ファイル: {sample['files'][:3]}")

def main():
    """エントリーポイント"""
    create_ground_truth()

if __name__ == "__main__":
    main()
