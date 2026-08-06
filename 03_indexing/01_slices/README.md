# Срезы

Реализуйте `interior_and_border(x)` для квадратной матрицы: верните внутреннюю часть без крайних строк и столбцов, а также верхнюю строку в обратном порядке. Для центра используйте срезы, а для изменения порядка — `flip`.

## Материалы

- [Индексирование, срезы и соединение](https://docs.pytorch.org/tutorials/beginner/basics/tensorqs_tutorial.html#standard-numpy-like-indexing-and-slicing)
- [`torch.flip`](https://docs.pytorch.org/docs/stable/generated/torch.flip.html)
- [Справочник `Tensor`](https://docs.pytorch.org/docs/stable/tensors.html)

## Как проверить

```bash
uv run pytest test_task.py
```
