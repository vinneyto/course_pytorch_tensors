# Shape drill: индекс и permute

## Задание

Для `x: [B,T,C]` сначала предскажите формы `x[..., 0]` и `x.permute(2,0,1)`. Реализуйте `read_shapes(x)`, возвращающую оба выражения. Следите, какая ось исчезает при целочисленном индексе.

## Материалы

- [`Tensor.permute`](https://docs.pytorch.org/docs/stable/generated/torch.Tensor.permute.html)
- [`Indexing`](https://docs.pytorch.org/docs/stable/tensor_view.html)

## Как проверить

```bash
uv run pytest test_task.py
```
