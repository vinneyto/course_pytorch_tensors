# Shape drill: оси без запуска

Реализуйте `axis_variants(x)` для 3D-тензора `(A, B, C)`. Верните четыре результата:

1. `x[:, None, :, :]`;
2. `x[..., 0]`;
3. `x.mean(dim=-1, keepdim=True)`;
4. `x.permute(2, 0, 1)`.

**До запуска тестов запишите на бумаге shape каждого результата.** Нового API здесь почти нет: задача тренирует чтение выражений с осями.

## Материалы

- [torch.unsqueeze.html](https://docs.pytorch.org/docs/stable/generated/torch.unsqueeze.html)
- [torch.permute.html](https://docs.pytorch.org/docs/stable/generated/torch.permute.html)
- [torch.mean.html](https://docs.pytorch.org/docs/stable/generated/torch.mean.html)

## Как проверить

```bash
uv run pytest test_task.py
```
