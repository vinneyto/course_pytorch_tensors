# Выбор через gather

## Задание

Реализуйте `pick_per_row(x, indices)`: из каждой строки матрицы `[N, C]` выберите столбец, заданный соответствующим элементом `indices: [N]`, и верните `[N]`.

Для `torch.gather` индекс должен иметь столько же измерений, сколько `x`: добавьте ось, выберите `dim=1`, затем уберите единичную ось.

## Материалы

- [`torch.gather`](https://docs.pytorch.org/docs/stable/generated/torch.gather.html)
- [`Tensor.unsqueeze`](https://docs.pytorch.org/docs/stable/generated/torch.Tensor.unsqueeze.html)

## Как проверить

```bash
uv run pytest test_task.py
```
