# Strides и contiguous layout

Реализуйте `transpose_and_flatten(x)` для contiguous 2D-тензора. Переставьте оси через `permute(1, 0)`, затем создайте contiguous-копию. Верните четыре значения: переставленный тензор, contiguous-копию, плоский view contiguous-копии и результат `reshape(-1)` исходного переставленного тензора.

Обратите внимание на `stride()` и `is_contiguous()`: `permute` меняет способ интерпретации той же памяти, поэтому результат обычно non-contiguous. `view` требует совместимого layout, а `reshape` при необходимости может создать копию.

## Материалы

- [tensor_view.html](https://docs.pytorch.org/docs/stable/tensor_view.html)
- [torch.Tensor.contiguous.html](https://docs.pytorch.org/docs/stable/generated/torch.Tensor.contiguous.html)
- [torch.Tensor.view.html](https://docs.pytorch.org/docs/stable/generated/torch.Tensor.view.html)
- [torch.Tensor.reshape.html](https://docs.pytorch.org/docs/stable/generated/torch.Tensor.reshape.html)

## Как проверить

```bash
uv run pytest test_task.py
```
