# Пакетное матричное умножение

## Задание

Реализуйте `batched_matrix_vector(a, x)` для `a: [N,3,3]`, `x: [N,3,1]`. Верните `[N,3,1]` одним `matmul`, без Python-цикла.

## Материалы

- [`torch.matmul`](https://docs.pytorch.org/docs/stable/generated/torch.matmul.html)
- [`torch.bmm`](https://docs.pytorch.org/docs/stable/generated/torch.bmm.html)

## Как проверить

```bash
uv run pytest test_task.py
```
