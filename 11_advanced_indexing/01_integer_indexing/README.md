# Индексирование тензором индексов

Реализуйте `select_rows(x, indices)`: выберите строки `x` в порядке, заданном одномерным `indices`, используя advanced indexing `x[indices]`.

После выполнения сравните это с обычным slice. Advanced indexing создаёт новый тензор с выбранными данными; изменение результата не должно менять `x`.

## Материалы

- [tensor_view.html](https://docs.pytorch.org/docs/stable/tensor_view.html)
- [tensorqs_tutorial.html#standard-numpy-like-indexing-and-slicing](https://docs.pytorch.org/tutorials/beginner/basics/tensorqs_tutorial.html#standard-numpy-like-indexing-and-slicing)

## Как проверить

```bash
uv run pytest test_task.py
```
