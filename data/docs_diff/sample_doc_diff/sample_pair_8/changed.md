# 変更後仕様: エラーコードの文字列化

## 概要

アプリケーション内で使用するエラーコードを、ユーザー向けメッセージに変換する。

## 仕様（変更後）

- ErrorCode 列挙型の各値に対応する説明文字列を返す。
- ERR_OK: "ok"
- **変更点**: ERR_NOT_FOUND のメッセージを "resource not found" に変更（より明確な説明のため）
- ERR_IO: "io error"
- ERR_NO_MEMORY: "no memory"
- 未知のコード: "unknown error"
