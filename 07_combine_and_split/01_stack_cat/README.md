# stack и cat

Реализуйте `combine(a, b)` для одинаковых одномерных тензоров. Верните результат `stack` по новой нулевой оси и результат `cat` по существующей нулевой оси. Сравните формы результатов.

## Материалы

- [`torch.stack`](https://docs.pytorch.org/docs/stable/generated/torch.stack.html)
- [`torch.cat`](https://docs.pytorch.org/docs/stable/generated/torch.cat.html)
- [Соединение тензоров в учебнике](https://docs.pytorch.org/tutorials/beginner/basics/tensorqs_tutorial.html#joining-tensors)

## Как проверить

```bash
uv run pytest test_task.py
```
