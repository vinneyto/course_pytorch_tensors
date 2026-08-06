# Разбиение

Реализуйте `split_columns(x, sizes)`: разбейте матрицу на части по столбцам с размерами из списка `sizes` и верните кортеж частей. Используйте `torch.split` и правильный `dim`.

## Материалы

- [`torch.split`](https://docs.pytorch.org/docs/stable/generated/torch.split.html)
- [`torch.chunk` — разбиение на количество частей](https://docs.pytorch.org/docs/stable/generated/torch.chunk.html)
- [`torch.cat` для обратной проверки](https://docs.pytorch.org/docs/stable/generated/torch.cat.html)

## Как проверить

```bash
uv run pytest test_task.py
```
