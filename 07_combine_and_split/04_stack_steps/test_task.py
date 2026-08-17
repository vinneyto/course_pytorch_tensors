import torch
from task import stack_steps


def test_stack_steps_puts_time_after_batch():
    steps = [
        torch.tensor([[1, 2], [3, 4]]),
        torch.tensor([[10, 20], [30, 40]]),
        torch.tensor([[100, 200], [300, 400]]),
    ]

    result = stack_steps(steps)

    assert result.shape == (2, 3, 2)
    assert torch.equal(result[:, 0], steps[0])
    assert torch.equal(result[:, 1], steps[1])
    assert torch.equal(result[:, 2], steps[2])


def test_stack_steps_with_single_feature():
    steps = [
        torch.tensor([[1], [2], [3]]),
        torch.tensor([[4], [5], [6]]),
    ]

    result = stack_steps(steps)

    assert result.shape == (3, 2, 1)
    assert torch.equal(
        result,
        torch.tensor([[[1], [4]], [[2], [5]], [[3], [6]]]),
    )
