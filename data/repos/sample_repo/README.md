# c_sample

企業のCプロジェクトを模したディレクトリ構造のサンプルです。

## ディレクトリ構成

- include/ : ヘッダファイル（API定義）
- src/     : 実装ファイル
- utils/   : 補助的なユーティリティ
- tests/   : テストコード

## ファイル一覧

- include/math_utils.h, include/string_utils.h
- src/math_utils.c, src/string_utils.c
- utils/logger.h, utils/logger.c
- tests/test_math.c, tests/test_string.c

## 概要
- math_utils: 四則演算の関数群
- string_utils: 文字列操作関数群
- logger: ログ出力用ユーティリティ
- tests: 各APIの簡単なテスト
