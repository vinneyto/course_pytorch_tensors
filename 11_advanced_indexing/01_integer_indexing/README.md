# Индексирование тензором

## Задание

Реализуйте `select_rows(x, indices)` как индексирование `x[indices]`. Индексы могут повторяться и менять порядок.

В отличие от обычного slice, advanced indexing создаёт новый tensor: после возврата изменение результата не должно менять `x`.

## Материалы

- [`Tensor indexing`](https://docs.pytorch.org/docs/stable/tensor_view.html)
- [`torch.index_select`](https://docs.pytorch.org/docs/stable/generated/torch.index_select.html)

## Как проверить

```bash
uv run pytest test_task.py
```
