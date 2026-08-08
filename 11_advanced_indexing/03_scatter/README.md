# scatter: запись по индексам

Реализуйте `place_values(values, indices, width)`. `values` и `indices` имеют форму `(N,)`. Создайте нулевую матрицу `(N, width)` того же dtype/device, что `values`, и разместите `values[n]` в столбце `indices[n]` каждой строки через `scatter` или `scatter_`.

Это логическое дополнение `gather`: `gather` читает по индексам, `scatter` записывает по индексам.

## Материалы

- [torch.Tensor.scatter.html](https://docs.pytorch.org/docs/stable/generated/torch.Tensor.scatter.html)
- [torch.zeros.html](https://docs.pytorch.org/docs/stable/generated/torch.zeros.html)

## Как проверить

```bash
uv run pytest test_task.py
```
