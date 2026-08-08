# Broadcasting по средней оси

## Задание

Реализуйте `add_sequence_bias(sequence, bias)`, где `sequence: [N, T, C]`, а индивидуальный для каждого объекта `bias: [N, C]`. Вставьте единичную ось в правильное место и верните `[N, T, C]`.

До запуска решите, почему `unsqueeze(0)` и `unsqueeze(-1)` здесь неверны.

## Материалы

- [`Tensor.unsqueeze`](https://docs.pytorch.org/docs/stable/generated/torch.Tensor.unsqueeze.html)
- [`Broadcasting semantics`](https://docs.pytorch.org/docs/stable/notes/broadcasting.html)

## Как проверить

```bash
uv run pytest test_task.py
```
