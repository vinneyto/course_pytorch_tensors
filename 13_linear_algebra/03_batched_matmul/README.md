# Batched matrix multiplication

Реализуйте `apply_batch(matrices, vectors)`. `matrices` имеет форму `(N, 3, 3)`, `vectors` — `(N, 3, 1)`. Примените каждую матрицу к соответствующему вектору одним `@`, без Python-циклов. Результат должен иметь форму `(N, 3, 1)`.

## Материалы

- [torch.matmul.html](https://docs.pytorch.org/docs/stable/generated/torch.matmul.html)

## Как проверить

```bash
uv run pytest test_task.py
```
