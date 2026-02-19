# 変更後仕様: math_utils multiply

## API 仕様（変更後）

- int multiply(int a, int b)
  - 2つの整数の積を返す。
  - **変更点**: どちらかが 0 の場合は 0 を返す（早期リターン）。オーバーフロー時は -1 を返す。
  - 例: multiply(3, 4) は 12、multiply(0, 100) は 0 を返す。
