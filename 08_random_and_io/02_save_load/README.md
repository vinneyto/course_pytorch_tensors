# Сохранение тензоров

Реализуйте `save_pair(path, x, y)` и `load_pair(path)`. Сохраните оба тензора одним вызовом `torch.save` в словаре с ключами `x` и `y`; загрузите с `torch.load`, явно используя `weights_only=True`, и верните пару в исходном порядке.

## Материалы

- [Учебник по сохранению и загрузке](https://docs.pytorch.org/tutorials/beginner/saving_loading_models.html#saving-loading-a-general-checkpoint-for-inference-and-or-resuming-training)
- [`torch.save`](https://docs.pytorch.org/docs/stable/generated/torch.save.html)
- [`torch.load` и `weights_only`](https://docs.pytorch.org/docs/stable/generated/torch.load.html)

## Как проверить

```bash
uv run pytest test_task.py
```
