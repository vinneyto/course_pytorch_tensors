import torch
from task import apply_batch


def test_apply_batch():
    matrices = torch.stack([torch.eye(3), 2 * torch.eye(3), torch.diag(torch.tensor([1.0, 2.0, 3.0]))])
    vectors = torch.tensor([[[1.0], [2.0], [3.0]], [[1.0], [2.0], [3.0]], [[2.0], [3.0], [4.0]]])
    result = apply_batch(matrices, vectors)
    assert result.shape == (3, 3, 1)
    assert torch.equal(result[0], vectors[0])
    assert torch.equal(result[1], 2 * vectors[1])
    assert torch.equal(result[2, :, 0], torch.tensor([2.0, 6.0, 12.0]))
