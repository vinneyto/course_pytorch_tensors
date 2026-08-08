# Поэлементное и матричное умножение

Реализуйте `compare_products(a, b)` для двух квадратных матриц одинаковой формы. Верните пару: поэлементное произведение `a * b` и матричное произведение `a @ b`.

Задача должна закрепить, что эти две операции имеют разный математический смысл, даже когда shape результата совпадает.

## Материалы

- [torch.mul.html](https://docs.pytorch.org/docs/stable/generated/torch.mul.html)
- [torch.matmul.html](https://docs.pytorch.org/docs/stable/generated/torch.matmul.html)

## Как проверить

```bash
uv run pytest test_task.py
```
