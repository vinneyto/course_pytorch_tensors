# keepdim для broadcasting

## Задание

Реализуйте `center_spatially(x)` для `[B, H, W, C]`: одним reduction вычислите среднее по `H, W` с `keepdim=True`, затем вычтите его из `x`. Верните `(centered, mean)` с формами `[B,H,W,C]` и `[B,1,1,C]`.

Сохранённые единичные оси делают последующий broadcasting явным.

## Материалы

- [`Tensor.mean`](https://docs.pytorch.org/docs/stable/generated/torch.Tensor.mean.html)
- [`Broadcasting semantics`](https://docs.pytorch.org/docs/stable/notes/broadcasting.html)

## Как проверить

```bash
uv run pytest test_task.py
```
