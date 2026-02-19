# ベース仕様: string_utils strlen_safe

## API 仕様（変更前）

- int strlen_safe(const char* s)
  - NULL 安全な文字列長を返す。s が NULL のときは 0 を返す。
  - 例: strlen_safe("hello") は 5 を返す。
