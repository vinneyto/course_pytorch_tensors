# gather: свой столбец для каждой строки

Реализуйте `choose_columns(x, indices)`. `x` имеет форму `(N, C)`, `indices` — `(N,)`. Для каждой строки `n` выберите `x[n, indices[n]]` через `torch.gather` и верните вектор `(N,)`.

Разберитесь, почему индексам временно нужна форма `(N, 1)` и что означает `dim=1`.

## Материалы

- [torch.gather.html](https://docs.pytorch.org/docs/stable/generated/torch.gather.html)
- [torch.unsqueeze.html](https://docs.pytorch.org/docs/stable/generated/torch.unsqueeze.html)

## Как проверить

```bash
uv run pytest test_task.py
```
