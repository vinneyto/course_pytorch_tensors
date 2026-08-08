import pytest
import torch
from task import broadcast_shape


def test_compatible_shapes():
    assert broadcast_shape((3, 1, 5), (1, 4, 1)) == torch.Size((3, 4, 5))
    assert broadcast_shape((8, 3, 1), (1, 5)) == torch.Size((8, 3, 5))


def test_incompatible_shapes():
    with pytest.raises(RuntimeError):
        broadcast_shape((2, 3), (4, 3))
