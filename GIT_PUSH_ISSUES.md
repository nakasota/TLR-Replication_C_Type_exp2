# Git Push Issues - Large Files

## 問題

GitHubのファイルサイズ制限により、以下の大きなファイルが原因でプッシュできません：

- `data/ground_truth/go_repo_structure.json` (145.97 MB)
- `embedding_based/embeddings_cache_openai/function_embeddings.pkl` (2013.97 MB)
- その他多数の.pklファイル

## 解決策

### 1. .gitignoreの更新 ✅

以下のパターンを追加済み：
```
# Large files (>50MB) - GitHub file size limits
data/ground_truth/go_repo_structure.json
data/ground_truth/accepted_proposals_func_analysis*.json
data/preprocess/accepted_proposals_func_analysis.json
data/preprocess/go_repo_structure.json

# Embedding cache files (pickle files can be regenerated)
embedding_based/embeddings_cache_openai/*.pkl
embedding_based/output/*.pkl
*.pkl
```

### 2. メモリ効率化スクリプトの修正 ✅

`embedding_based_localization_full.py`を修正：
- デフォルトで10個の提案のみ処理
- `--max-proposals N` で処理数を指定
- `--all` で全ての提案を処理
- メモリ管理とガベージコレクションを追加

### 3. Git履歴のクリーンアップが必要

**オプション A: BFG Repo-Cleaner使用**
```bash
# BFG Repo-Cleanerをダウンロード
wget https://repo1.maven.org/maven2/com/madgag/bfg/1.14.0/bfg-1.14.0.jar

# 大きなファイルを削除
java -jar bfg-1.14.0.jar --strip-blobs-bigger-than 50M

# 履歴をクリーンアップ
git reflog expire --expire=now --all && git gc --prune=now --aggressive
```

**オプション B: 新しいブランチ作成**
```bash
# 現在の状態で新しいブランチを作成
git checkout --orphan clean-main
git add .
git commit -m "Initial commit without large files"
git push origin clean-main
```

## 使用方法

### メモリ効率化されたevaluationスクリプト

```bash
# デフォルト（10個の提案）
python embedding_based_localization_full.py

# 特定の数を指定
python embedding_based_localization_full.py --max-proposals 20

# 全ての提案（メモリに注意）
python embedding_based_localization_full.py --all

# テストスクリプト
bash embedding_based/test_memory_efficient.sh
```

## 注意事項

- .pklファイルは再生成可能なため、gitignoreで除外
- 大きなground truthファイルは別途管理が必要
- メモリ制限のあるDocker環境では--max-proposalsを使用
