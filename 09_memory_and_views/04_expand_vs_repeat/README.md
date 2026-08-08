# expand и repeat

Реализуйте `repeat_column(x, copies)` для тензора формы `(N, 1)`. Верните два тензора формы `(N, copies)`: первый через `expand`, второй через `repeat`.

Сравните их `stride()`. У expanded-представления повторяемая ось может иметь stride 0: несколько логических элементов указывают на одно и то же значение. `repeat`, напротив, материализует повторённые данные.

## Материалы

- [torch.Tensor.expand.html](https://docs.pytorch.org/docs/stable/generated/torch.Tensor.expand.html)
- [torch.Tensor.repeat.html](https://docs.pytorch.org/docs/stable/generated/torch.Tensor.repeat.html)
- [broadcasting.html](https://docs.pytorch.org/docs/stable/notes/broadcasting.html)

## Как проверить

```bash
uv run pytest test_task.py
```
