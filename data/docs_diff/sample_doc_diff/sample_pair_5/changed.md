# 変更後仕様: string_utils strlen_safe

## API 仕様（変更後）

- int strlen_safe(const char* s)
  - 文字列長を返す。s が NULL のときは -1 を返す。
  - 例: strlen_safe("hello") は 5、strlen_safe(NULL) は -1 を返す。
