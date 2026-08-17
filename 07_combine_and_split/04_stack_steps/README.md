# stack по ненулевой оси

## Задание

Дан список `steps` из тензоров одинаковой формы `[B, F]`: batch объектов и
их признаки на последовательных шагах времени.

Реализуйте `stack_steps(steps)`. Добавьте новую ось времени после batch-оси и
верните тензор формы `[B, T, F]`, где `T = len(steps)`. Используйте
`torch.stack` с ненулевым значением `dim`.

Перед запуском кода предскажите форму результата. Чем она отличалась бы при
`dim=0`?

## Материалы

- [`torch.stack`](https://docs.pytorch.org/docs/stable/generated/torch.stack.html)
- [Соединение тензоров в учебнике](https://docs.pytorch.org/tutorials/beginner/basics/tensorqs_tutorial.html#joining-tensors)

## Как проверить

```bash
uv run pytest test_task.py
```
