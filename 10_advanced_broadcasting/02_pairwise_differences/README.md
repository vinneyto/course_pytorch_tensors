# Попарные разности без циклов

Реализуйте `pairwise_differences(points, queries)`. `points` имеет форму `(N, D)`, `queries` — `(M, D)`. Получите тензор `(N, M, D)`, где `result[n, m] = points[n] - queries[m]`.

Python-циклы запрещены. Осознанно вставьте единичные оси через `unsqueeze` и используйте broadcasting.

## Материалы

- [torch.unsqueeze.html](https://docs.pytorch.org/docs/stable/generated/torch.unsqueeze.html)
- [broadcasting.html](https://docs.pytorch.org/docs/stable/notes/broadcasting.html)

## Как проверить

```bash
uv run pytest test_task.py
```
