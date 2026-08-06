# Индексы экстремумов

Реализуйте `best_in_each_row(scores)`: верните индекс максимального элемента каждой строки и сами максимальные значения. Используйте `argmax`, а значения получите через `gather` либо подходящую агрегацию.

## Материалы

- [`torch.argmax`](https://docs.pytorch.org/docs/stable/generated/torch.argmax.html)
- [`torch.gather`](https://docs.pytorch.org/docs/stable/generated/torch.gather.html)
- [`torch.max`](https://docs.pytorch.org/docs/stable/generated/torch.max.html)

## Как проверить

```bash
uv run pytest test_task.py
```
