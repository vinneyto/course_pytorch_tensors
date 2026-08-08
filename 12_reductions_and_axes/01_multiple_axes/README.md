# Reduction по нескольким осям

## Задание

Реализуйте `spatial_mean(x)` для данных `[B, H, W, C]`: усредните сразу пространственные оси `H` и `W`, получив `[B, C]`. Используйте один вызов `mean(dim=(1, 2))`, без последовательных reductions.

## Материалы

- [`Tensor.mean`](https://docs.pytorch.org/docs/stable/generated/torch.Tensor.mean.html)

## Как проверить

```bash
uv run pytest test_task.py
```
