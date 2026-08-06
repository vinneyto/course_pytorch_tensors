# Поэлементная математика

Реализуйте евклидово расстояние `euclidean(a, b)` между двумя одинаковыми тензорами: квадрат разности, сумма всех элементов, квадратный корень. Нельзя использовать Python-циклы и `torch.cdist`.

## Материалы

- [`torch.sum`](https://docs.pytorch.org/docs/stable/generated/torch.sum.html)
- [`torch.sqrt`](https://docs.pytorch.org/docs/stable/generated/torch.sqrt.html)
- [`torch.linalg.vector_norm` — готовый аналог](https://docs.pytorch.org/docs/stable/generated/torch.linalg.vector_norm.html)

## Как проверить

```bash
uv run pytest test_task.py
```
