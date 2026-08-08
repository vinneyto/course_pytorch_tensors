# Broadcasting в matmul

## Задание

Реализуйте `shared_vector_product(a, x)` для `a: [N, R, C]` и общего `x: [C]`. Предскажите форму, затем используйте один `matmul`: batch-оси матриц обрабатываются автоматически, результат `[N,R]`.

## Материалы

- [`torch.matmul`](https://docs.pytorch.org/docs/stable/generated/torch.matmul.html)

## Как проверить

```bash
uv run pytest test_task.py
```
