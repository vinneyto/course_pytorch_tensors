# Диагональ матрицы

## Задание

Реализуйте `diagonal_roundtrip(values, offset=0)`. Сначала с помощью
`torch.diag` создайте из одномерного `values` матрицу, разместив значения на
диагонали с номером `offset`. Затем вторым вызовом `torch.diag` извлеките ту же
диагональ. Верните `(matrix, restored)`.

Положительный `offset` выбирает диагональ выше главной, отрицательный — ниже.
Не создавайте матрицу вручную и не используйте Python-циклы.

## Материалы

- [`torch.diag`](https://docs.pytorch.org/docs/stable/generated/torch.diag.html)

## Как проверить

```bash
uv run pytest test_task.py
```
