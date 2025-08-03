#!/usr/bin/env python3
"""
大きなファイルに対応した統計計算スクリプト
"""

import json
import os
from pathlib import Path
from collections import defaultdict
import sys

def load_ground_truth_data(filepath):
    """正解データを読み込む"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"エラー: {filepath} の読み込みに失敗しました: {e}")
        return None

def count_repo_structure_streaming(filepath):
    """大きなリポジトリ構造ファイルをストリーミングで処理"""
    print("リポジトリ構造ファイルを処理中...")
    
    total_files = 0
    total_functions = 0
    directories = set()
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            # ファイルサイズを取得してプログレス表示
            file_size = os.path.getsize(filepath)
            print(f"ファイルサイズ: {file_size / 1024 / 1024:.1f} MB")
            
            # JSONを手動でパース（メモリ効率のため）
            content = f.read()
            
        print("JSONをパース中...")
        data = json.loads(content)
        
        print("データを分析中...")
        for file_path, file_data in data.items():
            total_files += 1
            
            # ディレクトリを抽出
            path_parts = Path(file_path).parts
            for i in range(1, len(path_parts)):
                dir_path = '/'.join(path_parts[:i])
                if dir_path:
                    directories.add(dir_path)
            
            # 関数数を数える
            if isinstance(file_data, dict) and 'functions' in file_data:
                if isinstance(file_data['functions'], dict):
                    total_functions += len(file_data['functions'])
            
            # プログレス表示
            if total_files % 1000 == 0:
                print(f"処理済みファイル数: {total_files}")
    
    except Exception as e:
        print(f"エラー: {e}")
        return None
    
    return {
        'total_directories': len(directories),
        'total_files': total_files,
        'total_functions': total_functions
    }

def extract_directories_from_paths(file_paths):
    """ファイルパスのリストからディレクトリのセットを抽出"""
    directories = set()
    for file_path in file_paths:
        path_parts = Path(file_path).parts
        for i in range(1, len(path_parts)):
            dir_path = '/'.join(path_parts[:i])
            if dir_path:
                directories.add(dir_path)
    return directories

def analyze_ground_truth_data(data):
    """正解データを分析"""
    if not data:
        return None
    
    print("=== 正解データ（accepted_proposals_ground_truth.json）の分析 ===")
    
    proposal_stats = []
    total_files = 0
    total_functions = 0
    total_directories = set()
    
    for proposal in data:
        proposal_id = proposal.get('proposal_id', 'unknown')
        files = proposal.get('files', [])
        functions = proposal.get('detected_functions', [])
        
        # このプロポーザルのディレクトリを抽出
        proposal_dirs = extract_directories_from_paths(files)
        total_directories.update(proposal_dirs)
        
        # 統計を記録
        stats = {
            'proposal_id': proposal_id,
            'directories': len(proposal_dirs),
            'files': len(files),
            'functions': len(functions)
        }
        proposal_stats.append(stats)
        
        total_files += len(files)
        total_functions += len(functions)
    
    # 統計計算
    num_proposals = len(data)
    total_directories_count = len(total_directories)
    
    avg_dirs_per_proposal = total_directories_count / num_proposals if num_proposals > 0 else 0
    avg_files_per_proposal = total_files / num_proposals if num_proposals > 0 else 0
    avg_functions_per_proposal = total_functions / num_proposals if num_proposals > 0 else 0
    
    results = {
        'proposals_count': num_proposals,
        'total_directories': total_directories_count,
        'total_files': total_files,
        'total_functions': total_functions,
        'avg_directories_per_proposal': avg_dirs_per_proposal,
        'avg_files_per_proposal': avg_files_per_proposal,
        'avg_functions_per_proposal': avg_functions_per_proposal,
        'proposal_stats': proposal_stats
    }
    
    # 結果表示
    print(f"プロポーザル数: {num_proposals}")
    print(f"総ディレクトリ数: {total_directories_count}")
    print(f"総ファイル数: {total_files}")
    print(f"総関数数: {total_functions}")
    print(f"プロポーザルあたりの平均ディレクトリ数: {avg_dirs_per_proposal:.2f}")
    print(f"プロポーザルあたりの平均ファイル数: {avg_files_per_proposal:.2f}")
    print(f"プロポーザルあたりの平均関数数: {avg_functions_per_proposal:.2f}")
    
    return results

def compare_statistics(ground_truth_stats, repo_stats):
    """統計を比較"""
    if not ground_truth_stats or not repo_stats:
        print("統計の比較ができません")
        return
    
    print("\n=== 統計比較 ===")
    
    # 正解データの合計と対象データの比較
    print("【合計数の比較】")
    print(f"ディレクトリ数:")
    print(f"  正解データ合計: {ground_truth_stats['total_directories']:,}")
    print(f"  対象データ合計: {repo_stats['total_directories']:,}")
    print(f"  対象データに対する正解データの割合: {ground_truth_stats['total_directories'] / repo_stats['total_directories'] * 100:.2f}%")
    
    print(f"\nファイル数:")
    print(f"  正解データ合計: {ground_truth_stats['total_files']:,}")
    print(f"  対象データ合計: {repo_stats['total_files']:,}")
    print(f"  対象データに対する正解データの割合: {ground_truth_stats['total_files'] / repo_stats['total_files'] * 100:.2f}%")
    
    print(f"\n関数数:")
    print(f"  正解データ合計: {ground_truth_stats['total_functions']:,}")
    print(f"  対象データ合計: {repo_stats['total_functions']:,}")
    print(f"  対象データに対する正解データの割合: {ground_truth_stats['total_functions'] / repo_stats['total_functions'] * 100:.2f}%")
    
    print("\n【正解データの平均数】")
    print(f"プロポーザルあたりの平均ディレクトリ数: {ground_truth_stats['avg_directories_per_proposal']:.2f}")
    print(f"プロポーザルあたりの平均ファイル数: {ground_truth_stats['avg_files_per_proposal']:.2f}")
    print(f"プロポーザルあたりの平均関数数: {ground_truth_stats['avg_functions_per_proposal']:.2f}")

def main():
    print("統計計算を開始します...")
    
    # ファイルパス
    ground_truth_file = "/workspace/data/preprocess/accepted_proposals_ground_truth.json"
    repo_structure_file = "/workspace/data/preprocess/go_repo_structure.json"
    
    # 正解データ分析
    print("正解データを読み込んでいます...")
    ground_truth_data = load_ground_truth_data(ground_truth_file)
    
    if ground_truth_data is None:
        print("正解データの読み込みに失敗しました")
        return
    
    ground_truth_stats = analyze_ground_truth_data(ground_truth_data)
    
    # リポジトリ構造データ分析
    print("\n=== 対象データ（go_repo_structure.json）の分析 ===")
    repo_stats = count_repo_structure_streaming(repo_structure_file)
    
    if repo_stats:
        print(f"総ディレクトリ数: {repo_stats['total_directories']:,}")
        print(f"総ファイル数: {repo_stats['total_files']:,}")
        print(f"総関数数: {repo_stats['total_functions']:,}")
    
    # 比較
    compare_statistics(ground_truth_stats, repo_stats)
    
    print("\n分析完了!")

if __name__ == "__main__":
    main()
