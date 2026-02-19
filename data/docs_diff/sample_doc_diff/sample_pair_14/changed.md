# 変更後仕様: アプリケーション設定

## 概要

アプリケーションの設定を保持する構造体とデフォルト値を提供する。

## 仕様（変更後）

- AppConfig 構造体: enable_cache, max_connections, log_level に加え、**retry_count フィールドを新規追加**する。
- default_config(): 上記 4 フィールドのデフォルト値を返す。retry_count のデフォルトは 3。
- ヘッダ（構造体定義）と実装の両方を更新する必要がある。
