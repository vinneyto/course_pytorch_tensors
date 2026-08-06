# Изменение формы

Реализуйте `to_batches(x, width)`: превратите одномерный тензор в матрицу с `width` столбцами, не вычисляя число строк вручную. Затем верните эту матрицу и снова «плоское» представление. Используйте `reshape` и `-1`.

## Материалы

- [Учебник о представлениях тензора](https://docs.pytorch.org/tutorials/beginner/basics/tensorqs_tutorial.html#bridge-to-numpy)
- [`Tensor.reshape`](https://docs.pytorch.org/docs/stable/generated/torch.Tensor.reshape.html)
- [Семантика tensor views](https://docs.pytorch.org/docs/stable/tensor_view.html)

## Как проверить

```bash
uv run pytest test_task.py
```
