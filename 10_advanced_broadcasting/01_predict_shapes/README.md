# Предсказываем broadcasting-формы

## Задание

Сначала **на бумаге** предскажите формы трёх результатов, затем реализуйте `broadcast_examples(a, b, c, d)`: верните `a + b`, `c + d` и самостоятельно построенный через `torch.ones` тензор формы `[3, 4, 5]`, равный сумме operands форм `[3, 1, 5]` и `[1, 4, 1]`.

Размерности сравниваются справа налево; отсутствующие ведущие оси мысленно равны `1`. В тесте `c: [8, 3, 1]`, `d: [1, 5]`.

## Материалы

- [`Broadcasting semantics`](https://docs.pytorch.org/docs/stable/notes/broadcasting.html)
- [`torch.ones`](https://docs.pytorch.org/docs/stable/generated/torch.ones.html)

## Как проверить

```bash
uv run pytest test_task.py
```
