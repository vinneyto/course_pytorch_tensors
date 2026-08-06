# Агрегации

Реализуйте `column_stats(x)`: верните среднее и максимум каждого столбца. Для максимума нужен только тензор значений, без индексов. Изучите `mean(dim=...)` и `amax(dim=...)`.

## Материалы

- [`torch.mean`](https://docs.pytorch.org/docs/stable/generated/torch.mean.html)
- [`torch.amax`](https://docs.pytorch.org/docs/stable/generated/torch.amax.html)
- [Обзор операций с тензорами](https://docs.pytorch.org/tutorials/beginner/basics/tensorqs_tutorial.html#operations-on-tensors)

## Как проверить

```bash
uv run pytest test_task.py
```
