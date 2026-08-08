# Запись через scatter

## Задание

Реализуйте `place_per_row(values, indices, width)`: создайте нулевой tensor `[N, width]` через `values.new_zeros` и запишите каждое `values[n]` в столбец `indices[n]` с помощью `scatter`/`scatter_` по `dim=1`.

`gather` читает из позиций, а `scatter` записывает в позиции. Python-циклы запрещены.

## Материалы

- [`Tensor.scatter_`](https://docs.pytorch.org/docs/stable/generated/torch.Tensor.scatter_.html)
- [`Tensor.new_zeros`](https://docs.pytorch.org/docs/stable/generated/torch.Tensor.new_zeros.html)

## Как проверить

```bash
uv run pytest test_task.py
```
