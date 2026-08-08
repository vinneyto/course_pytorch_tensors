import torch
from task import transpose_and_flatten


def test_transpose_and_flatten_layout():
    x = torch.arange(12).reshape(3, 4)
    transposed, packed, flat_view, flat_reshape = transpose_and_flatten(x)

    assert torch.equal(transposed, x.T)
    assert transposed.stride() == (1, 4)
    assert not transposed.is_contiguous()
    assert packed.is_contiguous()
    assert packed.stride() == (3, 1)
    assert torch.equal(flat_view, torch.tensor([0, 4, 8, 1, 5, 9, 2, 6, 10, 3, 7, 11]))
    assert torch.equal(flat_reshape, flat_view)


def test_transpose_and_flatten_other_shape():
    x = torch.arange(10).reshape(2, 5)
    _, packed, flat_view, flat_reshape = transpose_and_flatten(x)
    assert packed.shape == (5, 2)
    assert torch.equal(flat_view, flat_reshape)
