# Воспроизводимые числа

Реализуйте `sample(seed, shape)`. Создайте локальный `torch.Generator`, задайте ему seed и передайте в `torch.rand`. Не вызывайте глобальный `torch.manual_seed`: функция не должна менять глобальный генератор.

## Материалы

- [`torch.Generator`](https://docs.pytorch.org/docs/stable/generated/torch.Generator.html)
- [`torch.rand`](https://docs.pytorch.org/docs/stable/generated/torch.rand.html)
- [Заметка о воспроизводимости](https://docs.pytorch.org/docs/stable/notes/randomness.html)

## Как проверить

```bash
uv run pytest test_task.py
```
