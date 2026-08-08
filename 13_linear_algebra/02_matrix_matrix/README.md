# Матричное умножение

## Задание

Реализуйте `matrix_product(a, b)` для `[M,K]` и `[K,N]` через `@`/`matmul`.

До запуска сравните ожидаемые формы `a * b` (поэлементно, только при broadcast-совместимости) и `a @ b` (свёртка общей оси `K`).

## Материалы

- [`torch.matmul`](https://docs.pytorch.org/docs/stable/generated/torch.matmul.html)
- [`Tensor.mul`](https://docs.pytorch.org/docs/stable/generated/torch.Tensor.mul.html)

## Как проверить

```bash
uv run pytest test_task.py
```
