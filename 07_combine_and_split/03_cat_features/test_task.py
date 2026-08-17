import torch
from task import concat_features


def test_concat_features_uses_feature_axis():
    left = torch.tensor([[1, 2], [3, 4]])
    right = torch.tensor([[10], [20]])

    result = concat_features(left, right)

    assert result.shape == (2, 3)
    assert torch.equal(result, torch.tensor([[1, 2, 10], [3, 4, 20]]))


def test_concat_features_supports_different_widths():
    left = torch.tensor([[1], [2], [3]])
    right = torch.tensor([[10, 11], [20, 21], [30, 31]])

    result = concat_features(left, right)

    assert result.shape == (3, 3)
    assert torch.equal(
        result,
        torch.tensor([[1, 10, 11], [2, 20, 21], [3, 30, 31]]),
    )
