# Несовместимые формы

## Задание

Реализуйте `broadcast_shape(shape_a, shape_b)`, возвращающую итоговый `torch.Size` через `torch.broadcast_shapes`. Для несовместимых форм функция должна естественно оставить `RuntimeError` от PyTorch.

Перед тестом вручную выровняйте формы справа и отметьте первую пару осей, где размеры не равны и ни один из них не `1`. Не ловите исключение внутри функции.

## Материалы

- [`torch.broadcast_shapes`](https://docs.pytorch.org/docs/stable/generated/torch.broadcast_shapes.html)
- [`Broadcasting semantics`](https://docs.pytorch.org/docs/stable/notes/broadcasting.html)

## Как проверить

```bash
uv run pytest test_task.py
```
