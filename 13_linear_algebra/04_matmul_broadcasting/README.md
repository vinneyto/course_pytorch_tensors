# Broadcasting batch-осей в matmul

Реализуйте `apply_shared_vector(matrices, vector)`. `matrices` имеет форму `(N, M, K)`, а общий `vector` — `(K,)`. Примените один и тот же вектор ко всем матрицам через `@`/`matmul`, не добавляя Python-цикл.

Перед запуском теста предскажите shape результата. `matmul` отдельно обрабатывает последние матричные размерности и умеет broadcasting batch-осей.

## Материалы

- [torch.matmul.html](https://docs.pytorch.org/docs/stable/generated/torch.matmul.html)

## Как проверить

```bash
uv run pytest test_task.py
```
