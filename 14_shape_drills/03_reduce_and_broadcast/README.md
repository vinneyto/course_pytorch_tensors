# Shape drill: reduction и broadcasting

## Задание

Для `x: [B,T,C]` предскажите формы `x.mean(dim=-1, keepdim=True)` и результата его вычитания из `x`. Реализуйте `center_last_axis(x)`, возвращающую `(centered, mean)`.

## Материалы

- [`Tensor.mean`](https://docs.pytorch.org/docs/stable/generated/torch.Tensor.mean.html)
- [`Broadcasting semantics`](https://docs.pytorch.org/docs/stable/notes/broadcasting.html)

## Как проверить

```bash
uv run pytest test_task.py
```
