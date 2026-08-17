# cat по ненулевой оси

## Задание

Даны две матрицы признаков: `left` формы `[B, F_left]` и `right` формы
`[B, F_right]`. Строки с одинаковым индексом описывают один и тот же объект.

Реализуйте `concat_features(left, right)`: объедините признаки каждого объекта
и верните тензор формы `[B, F_left + F_right]`. Используйте `torch.cat` по
оси `dim=1`.

Перед запуском кода ответьте: какая форма получилась бы при `dim=0` и почему
это не соответствует условию?

## Материалы

- [`torch.cat`](https://docs.pytorch.org/docs/stable/generated/torch.cat.html)
- [Соединение тензоров в учебнике](https://docs.pytorch.org/tutorials/beginner/basics/tensorqs_tutorial.html#joining-tensors)

## Как проверить

```bash
uv run pytest test_task.py
```
