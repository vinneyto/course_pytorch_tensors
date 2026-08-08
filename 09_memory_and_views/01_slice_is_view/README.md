# Срез как view

Реализуйте `middle_columns(x)`: верните все строки без первого и последнего столбца обычным срезом. Не используйте `clone`.

После выполнения отдельно проверьте, что изменение результата меняет соответствующие элементы исходного тензора. Это показывает важную идею: тензор-срез может быть **представлением (view)** той же памяти, а не независимой копией.

## Материалы

- [tensor_view.html](https://docs.pytorch.org/docs/stable/tensor_view.html)
- [tensorqs_tutorial.html#standard-numpy-like-indexing-and-slicing](https://docs.pytorch.org/tutorials/beginner/basics/tensorqs_tutorial.html#standard-numpy-like-indexing-and-slicing)

## Как проверить

```bash
uv run pytest test_task.py
```
