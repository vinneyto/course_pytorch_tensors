# Координатная сетка через meshgrid

Реализуйте `pixel_grid(width, height)`. Создайте `xs = arange(width)` и `ys = arange(height)`, затем `torch.meshgrid(xs, ys, indexing="xy")`.

Соберите координаты `(x, y)` в тензор формы `(H, W, 2)` через `stack`, а затем получите плоский список пикселей `(H*W, 2)` через `reshape`. Верните оба тензора.

Обратите внимание на порядок координат и на отличие `indexing="xy"` от матричного порядка индексов.

## Материалы

- [torch.meshgrid.html](https://docs.pytorch.org/docs/stable/generated/torch.meshgrid.html)
- [torch.stack.html](https://docs.pytorch.org/docs/stable/generated/torch.stack.html)
- [torch.reshape.html](https://docs.pytorch.org/docs/stable/generated/torch.reshape.html)

## Как проверить

```bash
uv run pytest test_task.py
```
