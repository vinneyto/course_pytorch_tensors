import torch
from task import make_rows


def test_expand_vs_repeat():
    x = torch.tensor([2.0, 4.0, 6.0])
    expanded, repeated = make_rows(x, 5)
    assert expanded.shape == repeated.shape == (5, 3)
    assert torch.equal(expanded, repeated)
    assert expanded.stride()[0] == 0
    assert expanded.untyped_storage().data_ptr() == x.untyped_storage().data_ptr()
    assert repeated.untyped_storage().data_ptr() != x.untyped_storage().data_ptr()
