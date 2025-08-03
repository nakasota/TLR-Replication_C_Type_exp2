# シンプルGround Truth作成システム

このディレクトリは、Go言語の提案（proposal）ファイルから**CL番号を抽出**し、**変更されたファイル全体を取得**することに特化したシンプルなシステムです。

## 🎯 目的

1. **mdファイルからCL番号を抽出**: `data/preprocess/accepted_proposals/`のmdファイルからCL番号を自動検出
2. **変更ファイル全体を取得**: 検出したCLで変更されたすべてのファイルの内容を取得

## 📁 ファイル構成

```
create_ground_truth/
├── README.md                    # このファイル
├── cl_extractor.py             # CL抽出とファイル内容取得
├── ground_truth_generator.py   # Ground Truth生成メインスクリプト
└── output/                     # 生成されたground truthの出力先
```

## 🚀 使用方法

### 1. テスト実行（推奨）

```bash
cd create_ground_truth
python ground_truth_generator.py --test_mode
```

### 2. 全ファイル処理

```bash
cd create_ground_truth
python ground_truth_generator.py
```

### 3. カスタムディレクトリ指定

```bash
python ground_truth_generator.py --input_dir /path/to/proposals --output_dir /path/to/output
```

## 📊 出力データ

### ファイルレベルGround Truth
各提案で変更されたファイルの一覧
```json
{
  "15513": {
    "proposal_file": "../data/preprocess/accepted_proposals/15513.md",
    "cl_numbers": ["42531"],
    "total_changed_files": 2,
    "changed_files": [
      {
        "file_path": ".gitignore",
        "cl_number": "42531",
        "status": "",
        "lines_inserted": 1,
        "lines_deleted": 0,
        "has_content": true,
        "content_length": 1234
      }
    ]
  }
}
```

### ディレクトリレベルGround Truth
各提案で変更されたディレクトリの一覧
```json
{
  "15513": {
    "proposal_file": "../data/preprocess/accepted_proposals/15513.md",
    "cl_numbers": ["42531"],
    "total_changed_directories": 2,
    "changed_directories": [".", "src"]
  }
}
```

### 統計情報
処理結果の統計データ
```json
{
  "generation_time": "2025-01-01T12:00:00",
  "total_proposals": 5,
  "successful_extractions": 4,
  "extraction_rate": 0.8,
  "total_cls": 4,
  "total_changed_files": 12,
  "total_changed_directories": 8
}
```

## 🔧 機能詳細

### CL抽出パターン
以下のパターンでCL番号を自動検出：
- `https://golang.org/cl/123456`
- `https://go.dev/cl/123456`
- `Change https://golang.org/cl/123456`
- `CL 123456`

### Gerrit API連携
- **CL詳細情報**: ステータス、件名、変更日時
- **変更ファイル一覧**: CLで変更されたすべてのファイル
- **ファイル内容**: CL時点での各ファイルの全内容

### エラーハンドリング
- API制限対策（0.5秒間隔）
- 複数エンドポイントでのフォールバック
- 詳細なログ出力

## 📈 使用例

### 単一ファイルテスト
```python
from cl_extractor import SimpleCLExtractor

extractor = SimpleCLExtractor()
result = extractor.extract_cl_from_proposal("../data/preprocess/accepted_proposals/15513.md")

if result:
    print(f"CL番号: {result['cl_numbers']}")
    print(f"変更ファイル数: {result['total_changed_files']}")
    
    for cl in result['cl_details']:
        print(f"CL {cl['cl_number']}: {cl['subject']}")
        for file_info in cl['changed_files']:
            print(f"  - {file_info['file_path']} ({len(file_info['content'])} 文字)")
```

### 複数ファイル処理
```python
from ground_truth_generator import SimpleGroundTruthGenerator

generator = SimpleGroundTruthGenerator("output")
result = generator.generate_ground_truth("../data/preprocess/accepted_proposals")
```

## ⚡ パフォーマンス

- **テストモード**: 5ファイル、約30秒
- **全体処理**: 300+ファイル、約15-20分（API制限により）
- **成功率**: 通常80-90%（CLが存在する提案のみ）

## 🔍 トラブルシューティング

### よくある問題

1. **CL番号が見つからない**
   - 提案にCLが含まれていない場合は正常
   - mdファイルの形式を確認

2. **API接続エラー**
   - ネットワーク接続を確認
   - Gerrit APIが利用可能か確認

3. **ファイル内容が取得できない**
   - CLがマージされていない場合
   - プライベートCLの場合

### ログの確認
詳細なログが出力されるので、問題の特定に活用してください：
```
2025-01-01 12:00:00 - INFO - ✓ 1個のCL番号を検出: ['42531']
2025-01-01 12:00:01 - INFO - ✓ CL 42531: x/build: misc-compile trybots should compile tests
```

## 🎉 成果物

このシステムにより、Go言語の提案から以下を自動取得できます：

- ✅ 提案に関連するCL番号
- ✅ CLで変更されたすべてのファイル
- ✅ 各ファイルの完全な内容
- ✅ 変更統計情報（行数、ディレクトリなど）
- ✅ 構造化されたGround Truthデータ

このデータは機械学習モデルの訓練や評価に直接利用できます。