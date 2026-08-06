# Булевы маски

Реализуйте `clip_negatives(x, limit)`. Создайте новый тензор, замените отрицательные элементы нулями, затем верните его элементы, строго превышающие `limit`. Исходный `x` менять нельзя. Используйте `clone` и булевы маски.

## Материалы

- [`Tensor.clone`](https://docs.pytorch.org/docs/stable/generated/torch.Tensor.clone.html)
- [`torch.masked_select`](https://docs.pytorch.org/docs/stable/generated/torch.masked_select.html)
- [Индексирование и срезы в учебнике](https://docs.pytorch.org/tutorials/beginner/basics/tensorqs_tutorial.html#standard-numpy-like-indexing-and-slicing)

## Как проверить

```bash
uv run pytest test_task.py
```
