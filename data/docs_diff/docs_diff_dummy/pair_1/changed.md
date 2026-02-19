# 変更後仕様: math_utils add

## API 仕様（変更後）

- int add(int a, int b)
  - 2つの整数の和を返す。オーバーフロー時は -1 を返す。
  - 例: add(3, 5) は 8、add(INT_MAX, 1) は -1 を返す。
