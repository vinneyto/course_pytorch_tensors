# Strides и contiguous layout

## Задание

Реализуйте `reorder_and_flatten(x)`. Для матрицы `[H, W]` получите `y = x.permute(1, 0)`, затем верните `y`, его `stride()`, плоский результат `reshape(-1)` и плоский результат `y.contiguous().view(-1)`.

`permute` не переставляет данные физически: меняются метаданные формы и strides, поэтому `y` обычно non-contiguous и прямой `y.view(-1)` невозможен. `reshape` при необходимости сам делает копию, а `contiguous` явно создаёт подходящий layout.

## Материалы

- [`Tensor.stride`](https://docs.pytorch.org/docs/stable/generated/torch.Tensor.stride.html)
- [`Tensor.contiguous`](https://docs.pytorch.org/docs/stable/generated/torch.Tensor.contiguous.html)
- [`Tensor.view`](https://docs.pytorch.org/docs/stable/generated/torch.Tensor.view.html)
- [`Tensor.reshape`](https://docs.pytorch.org/docs/stable/generated/torch.Tensor.reshape.html)

## Как проверить

```bash
uv run pytest test_task.py
```
