# Shape drill: маленький pipeline

Реализуйте `channel_summary(x)` для изображения batch в формате `(B, H, W, C)`.

1. Переставьте оси в `(B, C, H, W)`;
2. объедините `H` и `W` через `reshape` в `(B, C, H*W)`;
3. найдите среднее по последней оси с `keepdim=True`, получив `(B, C, 1)`.

Верните все три промежуточных тензора. Перед кодом проследите shapes всей цепочки вручную.

## Материалы

- [torch.permute.html](https://docs.pytorch.org/docs/stable/generated/torch.permute.html)
- [torch.reshape.html](https://docs.pytorch.org/docs/stable/generated/torch.reshape.html)
- [torch.mean.html](https://docs.pytorch.org/docs/stable/generated/torch.mean.html)

## Как проверить

```bash
uv run pytest test_task.py
```
