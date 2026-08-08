# Кусочное преобразование

## Задание

Реализуйте `signed_square(x)`: для неотрицательных элементов верните `x ** 2`, для отрицательных — `-x ** 2`. Используйте `torch.where`, без Python-циклов и изменения входа.

## Материалы

- [`torch.where`](https://docs.pytorch.org/docs/stable/generated/torch.where.html)

## Как проверить

```bash
uv run pytest test_task.py
```
