# Попарные разности

## Задание

Реализуйте `pairwise_differences(points, queries)` для `points: [N, D]` и `queries: [M, D]`. Результат `[N, M, D]` должен удовлетворять `delta[n, m] = points[n] - queries[m]`.

Используйте два осмысленных `unsqueeze` и broadcasting. Python-циклы и `torch.cdist` запрещены.

## Материалы

- [`Tensor.unsqueeze`](https://docs.pytorch.org/docs/stable/generated/torch.Tensor.unsqueeze.html)
- [`Broadcasting semantics`](https://docs.pytorch.org/docs/stable/notes/broadcasting.html)

## Как проверить

```bash
uv run pytest test_task.py
```
