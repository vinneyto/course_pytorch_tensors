# Единичная ось в середине

Реализуйте `scale_channels(x, scales)`. `x` имеет форму `(N, T, C)`, а `scales` — `(N, C)`: для каждого элемента batch свой коэффициент для каждого канала. Получите `(N, T, C)` без циклов.

Здесь недостаточно добавить ось «где-нибудь»: нужно вставить её именно между `N` и `C`, чтобы `scales` превратился в `(N, 1, C)`.

## Материалы

- [torch.unsqueeze.html](https://docs.pytorch.org/docs/stable/generated/torch.unsqueeze.html)
- [broadcasting.html](https://docs.pytorch.org/docs/stable/notes/broadcasting.html)

## Как проверить

```bash
uv run pytest test_task.py
```
