# Из несовместимых форм в совместимые

Реализуйте `outer_sum_per_batch(a, b)`. `a` имеет форму `(N, T)`, `b` — `(N, C)`. Напрямую эти формы обычно несовместимы для broadcasting, если `T != C`.

Получите `(N, T, C)`, где `result[n, t, c] = a[n, t] + b[n, c]`. Для этого вставьте единичные оси в правильные места.

## Материалы

- [broadcasting.html](https://docs.pytorch.org/docs/stable/notes/broadcasting.html)
- [torch.unsqueeze.html](https://docs.pytorch.org/docs/stable/generated/torch.unsqueeze.html)

## Как проверить

```bash
uv run pytest test_task.py
```
