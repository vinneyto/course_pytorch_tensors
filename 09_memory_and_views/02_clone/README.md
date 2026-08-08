# Представление и независимая копия

## Задание

Реализуйте `view_and_copy(x)`: верните два тензора для столбцов `1:-1`. Первый должен быть обычным срезом, второй — его независимой копией через `clone()`.

После теста измените оба результата и заметьте: изменение view видно в `x`, а изменение clone — нет.

## Материалы

- [`Tensor.clone`](https://docs.pytorch.org/docs/stable/generated/torch.Tensor.clone.html)
- [`Tensor views`](https://docs.pytorch.org/docs/stable/tensor_view.html)

## Как проверить

```bash
uv run pytest test_task.py
```
