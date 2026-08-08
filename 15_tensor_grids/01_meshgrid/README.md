# Сетка координат

## Задание

Реализуйте `pixel_grid(height, width)`. Создайте `xs = torch.arange(width)` и `ys = torch.arange(height)`, вызовите `torch.meshgrid(xs, ys, indexing="xy")`, затем сложите координаты в последней оси и преобразуйте в список `[height * width, 2]`. Верните `(grid_x, grid_y, coordinates)`.

До запуска предскажите формы обеих сеток. В каждой строке `coordinates` порядок координат — `(x, y)`.

## Материалы

- [`torch.meshgrid`](https://docs.pytorch.org/docs/stable/generated/torch.meshgrid.html)
- [`torch.stack`](https://docs.pytorch.org/docs/stable/generated/torch.stack.html)
- [`Tensor.reshape`](https://docs.pytorch.org/docs/stable/generated/torch.Tensor.reshape.html)

## Как проверить

```bash
uv run pytest test_task.py
```
