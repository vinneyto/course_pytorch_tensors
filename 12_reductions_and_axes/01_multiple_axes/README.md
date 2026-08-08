# Reduction сразу по нескольким осям

Реализуйте `spatial_mean(x)` для тензора изображения формы `(B, H, W, C)`. Усредните пространственные оси `H` и `W` одним вызовом `mean`, чтобы получить `(B, C)`.

## Материалы

- [torch.mean.html](https://docs.pytorch.org/docs/stable/generated/torch.mean.html)

## Как проверить

```bash
uv run pytest test_task.py
```
