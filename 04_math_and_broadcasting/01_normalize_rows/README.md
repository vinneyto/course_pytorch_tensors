# Broadcasting

Реализуйте `center_rows(x)`: вычтите из каждой строки её среднее. Сохраняйте агрегируемую ось (`keepdim=True`), чтобы broadcasting был очевиден. Верните центрированную матрицу.

## Материалы

- [Семантика broadcasting](https://docs.pytorch.org/docs/stable/notes/broadcasting.html)
- [`torch.mean`](https://docs.pytorch.org/docs/stable/generated/torch.mean.html)
- [Операции с тензорами](https://docs.pytorch.org/tutorials/beginner/basics/tensorqs_tutorial.html#operations-on-tensors)

## Как проверить

```bash
uv run pytest test_task.py
```
