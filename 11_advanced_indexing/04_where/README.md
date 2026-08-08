# Условная поэлементная операция

Реализуйте `dead_zone(x, limit)`: элементы с `abs(x) < limit` замените нулями, остальные оставьте без изменений. Используйте `torch.where`, без Python-циклов и без изменения исходного `x`.

## Материалы

- [torch.where.html](https://docs.pytorch.org/docs/stable/generated/torch.where.html)
- [torch.abs.html](https://docs.pytorch.org/docs/stable/generated/torch.abs.html)

## Как проверить

```bash
uv run pytest test_task.py
```
