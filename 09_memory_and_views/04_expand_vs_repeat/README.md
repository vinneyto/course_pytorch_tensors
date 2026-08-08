# expand и repeat

## Задание

Реализуйте `make_rows(x, count)` для вектора `[D]`: добавьте ведущую ось и получите два результата `[count, D]` — через `expand` и через `repeat`.

Заметьте stride `0` у расширенной оси: `expand` использует то же значение при broadcasting без копирования, тогда как `repeat` хранит повторы отдельно. Не записывайте на месте в expanded tensor.

## Материалы

- [`Tensor.expand`](https://docs.pytorch.org/docs/stable/generated/torch.Tensor.expand.html)
- [`Tensor.repeat`](https://docs.pytorch.org/docs/stable/generated/torch.Tensor.repeat.html)
- [`Broadcasting semantics`](https://docs.pytorch.org/docs/stable/notes/broadcasting.html)

## Как проверить

```bash
uv run pytest test_task.py
```
