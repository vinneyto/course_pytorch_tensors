import torch


def sample(seed: int, shape: tuple[int, ...]) -> torch.Tensor:
    """Получить воспроизводимую равномерную выборку."""
    generator = torch.Generator()
    generator.manual_seed(seed)

    print(torch.rand(shape, generator=generator))
    return torch.rand(shape, generator=generator)
