# Внешнее произведение векторов

## Задание

Реализуйте `batched_outer(a, b)` для пакетов векторов `a: [N, R]` и `b: [N, C]`.

Для каждого элемента пакета нужно получить матрицу `[R, C]`, в которой элемент `[i, j]` равен `a[i] * b[j]`. Итоговая форма результата — `[N, R, C]`.

Используйте `unsqueeze` и broadcasting. Не используйте циклы, `torch.outer` или `torch.einsum`.

## Подсказка

Добавьте к `a` ось столбцов, а к `b` — ось строк. Перед умножением предскажите формы обоих промежуточных тензоров.

## Материалы

- [Broadcasting semantics](https://docs.pytorch.org/docs/stable/notes/broadcasting.html)
- [`torch.unsqueeze`](https://docs.pytorch.org/docs/stable/generated/torch.unsqueeze.html)

## Как проверить

```bash
uv run pytest test_task.py
```
