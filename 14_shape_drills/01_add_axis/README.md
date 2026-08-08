# Shape drill: новая ось

## Задание

Для `x: [B,T,C]` **до запуска** предскажите форму `x[:, None, :, :]`. Реализуйте `add_group_axis(x)` именно таким индексированием и верните результат. Нового API здесь нет: тренируем чтение осей.

## Материалы

- [`Tensor indexing`](https://docs.pytorch.org/docs/stable/tensor_view.html)

## Как проверить

```bash
uv run pytest test_task.py
```
