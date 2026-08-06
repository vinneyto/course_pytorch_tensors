# Фабрики тензоров

Реализуйте `make_grid(rows, cols)`. Верните матрицу нулей `rows × cols`, вектор единиц длины `cols` и целочисленный вектор `0..rows*cols-1`, преобразованный в матрицу. Используйте `zeros`, `ones`, `arange` и `reshape`.

## Материалы

- [`torch.zeros`](https://docs.pytorch.org/docs/stable/generated/torch.zeros.html)
- [`torch.ones`](https://docs.pytorch.org/docs/stable/generated/torch.ones.html)
- [`torch.arange`](https://docs.pytorch.org/docs/stable/generated/torch.arange.html)
- [`torch.reshape`](https://docs.pytorch.org/docs/stable/generated/torch.reshape.html)

## Как проверить

```bash
uv run pytest test_task.py
```
