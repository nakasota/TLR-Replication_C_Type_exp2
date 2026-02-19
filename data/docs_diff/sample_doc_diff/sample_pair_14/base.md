# ベース仕様: アプリケーション設定

## 概要

アプリケーションの設定を保持する構造体とデフォルト値を提供する。

## 仕様（変更前）

- AppConfig 構造体: enable_cache, max_connections, log_level を持つ。
- default_config(): 上記 3 フィールドのデフォルト値を返す。
