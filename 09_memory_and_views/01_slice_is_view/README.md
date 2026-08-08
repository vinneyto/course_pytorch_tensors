# Срез как представление

## Задание

Реализуйте `edit_middle(x, value)`: получите срез `x[:, 1:3]`, заполните его `value` **на месте** и верните этот срез. Исходный `x` должен измениться вместе со срезом. Не создавайте копию.

После выполнения сравните `data_ptr()` и подумайте: почему тензор может не владеть отдельной памятью?

## Материалы

- [`Tensor.__getitem__`](https://docs.pytorch.org/docs/stable/tensor_view.html)
- [`Tensor.fill_`](https://docs.pytorch.org/docs/stable/generated/torch.Tensor.fill_.html)

## Как проверить

```bash
uv run pytest test_task.py
```
