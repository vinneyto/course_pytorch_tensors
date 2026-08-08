import torch
from task import compare_products


def test_compare_products():
    a = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
    b = torch.tensor([[5.0, 6.0], [7.0, 8.0]])
    elementwise, matrix = compare_products(a, b)
    assert torch.equal(elementwise, torch.tensor([[5.0, 12.0], [21.0, 32.0]]))
    assert torch.equal(matrix, torch.tensor([[19.0, 22.0], [43.0, 50.0]]))
