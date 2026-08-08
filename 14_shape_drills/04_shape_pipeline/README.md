# Shape drill: цепочка операций

## Задание

Реализуйте `shape_pipeline(x)` для `[B,T,C]`: переставьте в `[B,C,T]`, вставьте ось после batch, суммируйте последнюю ось и уберите созданную единичную ось через `squeeze(1)`. До запуска последовательно запишите форму после каждого шага; итог `[B,C]`.

## Материалы

- [`Tensor.transpose`](https://docs.pytorch.org/docs/stable/generated/torch.Tensor.transpose.html)
- [`Tensor.squeeze`](https://docs.pytorch.org/docs/stable/generated/torch.Tensor.squeeze.html)
- [`Tensor.sum`](https://docs.pytorch.org/docs/stable/generated/torch.Tensor.sum.html)

## Как проверить

```bash
uv run pytest test_task.py
```
