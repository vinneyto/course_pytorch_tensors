# Преобразование типа

Реализуйте `as_probabilities(x)`: преобразуйте целочисленный тензор в `float32` на том же устройстве и разделите на сумму всех элементов. Исходный тензор не меняйте.

## Материалы

- [Атрибуты `dtype` и `device`](https://docs.pytorch.org/docs/stable/tensor_attributes.html)
- [`Tensor.to`](https://docs.pytorch.org/docs/stable/generated/torch.Tensor.to.html)
- [`Tensor.float`](https://docs.pytorch.org/docs/stable/generated/torch.Tensor.float.html)

## Как проверить

```bash
uv run pytest test_task.py
```
