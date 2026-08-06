# Оси и размерности

Реализуйте `channel_first(x)` для изображения формы `(height, width, channels)`: перенесите каналы в начало и добавьте batch-ось. Результат имеет форму `(1, channels, height, width)`. Используйте `permute` и `unsqueeze`.

## Материалы

- [`Tensor.permute`](https://docs.pytorch.org/docs/stable/generated/torch.Tensor.permute.html)
- [`Tensor.unsqueeze`](https://docs.pytorch.org/docs/stable/generated/torch.Tensor.unsqueeze.html)
- [Учебник по операциям с тензорами](https://docs.pytorch.org/tutorials/beginner/basics/tensorqs_tutorial.html#operations-on-tensors)

## Как проверить

```bash
uv run pytest test_task.py
```
