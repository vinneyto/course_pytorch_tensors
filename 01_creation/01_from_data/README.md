# Создание из данных

Реализуйте `make_tensors(values)`. Верните пару: тензор `float32` из `values` и тензор `int64` с теми же значениями. Не меняйте входной список. Используйте `torch.tensor` и параметр `dtype`.

## Материалы

- [Учебник: знакомство с тензорами](https://docs.pytorch.org/tutorials/beginner/basics/tensorqs_tutorial.html)
- [`torch.tensor`](https://docs.pytorch.org/docs/stable/generated/torch.tensor.html)
- [Типы данных `torch.dtype`](https://docs.pytorch.org/docs/stable/tensor_attributes.html#torch-dtype)

## Как проверить

```bash
uv run pytest test_task.py
```
