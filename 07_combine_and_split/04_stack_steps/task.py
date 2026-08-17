import torch


def stack_steps(steps: list[torch.Tensor]) -> torch.Tensor:
    """Собрать шаги времени в новую ось после batch-оси."""
    for step in steps:
        print(step)
    print('------------')
    print('len(steps)=', len(steps))
    print(torch.stack(steps, dim=0).shape)
    print(torch.stack(steps, dim=1).shape)
    print(torch.stack(steps, dim=-1))
    return torch.stack(steps, dim=1)
