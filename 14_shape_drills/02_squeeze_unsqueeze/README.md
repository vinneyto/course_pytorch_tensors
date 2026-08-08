# Shape drill: squeeze и unsqueeze

Реализуйте `make_column_batch(x)` для матрицы `(N, C)`: добавьте оси так, чтобы получить `(N, 1, C, 1)`, затем удалите **только последнюю** единичную ось и получите `(N, 1, C)`.

Верните оба тензора. Перед запуском тестов предскажите формы и подумайте, чем `squeeze()` без `dim` отличается от `squeeze(-1)`.

## Материалы

- [torch.unsqueeze.html](https://docs.pytorch.org/docs/stable/generated/torch.unsqueeze.html)
- [torch.squeeze.html](https://docs.pytorch.org/docs/stable/generated/torch.squeeze.html)

## Как проверить

```bash
uv run pytest test_task.py
```
