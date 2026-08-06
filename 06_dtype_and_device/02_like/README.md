# Фабрики *_like

Реализуйте `describe_like(x)`: создайте через фабрики `*_like` тензор нулей и булев тензор единиц с той же формой и устройством, что `x`. У первого должен сохраниться dtype входа, у второго dtype — `torch.bool`.

## Материалы

- [`torch.zeros_like`](https://docs.pytorch.org/docs/stable/generated/torch.zeros_like.html)
- [`torch.ones_like`](https://docs.pytorch.org/docs/stable/generated/torch.ones_like.html)
- [Типы данных `torch.dtype`](https://docs.pytorch.org/docs/stable/tensor_attributes.html#torch-dtype)

## Как проверить

```bash
uv run pytest test_task.py
```
