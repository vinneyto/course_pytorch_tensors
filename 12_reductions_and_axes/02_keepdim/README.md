# keepdim для последующего broadcasting

Реализуйте `center_spatial(x)` для `(B, H, W, C)`. Найдите среднее по `H` и `W` с `keepdim=True`, затем вычтите его из `x` broadcasting-ом. Верните пару `(centered, means)`.

`means` должна иметь форму `(B, 1, 1, C)`: единичные оси сохраняют смысл исходных размерностей и сразу подходят для broadcasting.

## Материалы

- [torch.mean.html](https://docs.pytorch.org/docs/stable/generated/torch.mean.html)
- [broadcasting.html](https://docs.pytorch.org/docs/stable/notes/broadcasting.html)

## Как проверить

```bash
uv run pytest test_task.py
```
