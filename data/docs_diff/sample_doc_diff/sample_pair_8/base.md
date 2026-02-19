# ベース仕様: エラーコードの文字列化

## 概要

アプリケーション内で使用するエラーコードを、ユーザー向けメッセージに変換する。

## 仕様（変更前）

- ErrorCode 列挙型の各値に対応する説明文字列を返す。
- ERR_OK: "ok"
- ERR_NOT_FOUND: "not found"
- ERR_IO: "io error"
- ERR_NO_MEMORY: "no memory"
- 未知のコード: "unknown error"
