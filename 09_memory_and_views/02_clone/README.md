# View и независимая копия

Реализуйте `view_and_copy(x)`. Возьмите срез `x[:, 1:-1]` и верните пару: сам view и его независимую копию через `clone()`.

После задачи сравните поведение двух результатов при изменении данных: view должен разделять память с `x`, а clone — нет.

## Материалы

- [torch.Tensor.clone.html](https://docs.pytorch.org/docs/stable/generated/torch.Tensor.clone.html)
- [tensor_view.html](https://docs.pytorch.org/docs/stable/tensor_view.html)

## Как проверить

```bash
uv run pytest test_task.py
```
