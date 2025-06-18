import pytest
from problems.two_sum import two_sum

@pytest.mark.parametrize("nums, target, expected", [
    ([2, 7, 11, 15], 9, [0, 1]),
    ([3, 3], 6, [0, 1]),
    ([1, 2, 3, 4], 5, [[0, 3], [1, 2]]),  # multiple valid answers
    ([-3, 4, 3, 90], 0, [0, 2]),
    ([10, 5, 2, 3, 7], 9, [1, 2]),
])
def test_two_sum(nums, target, expected):
    result = two_sum(nums, target)
    if isinstance(expected[0], list):  # handling multiple valid answers
        assert sorted(result) in [sorted(ans) for ans in expected]
    else:
        assert sorted(result) == sorted(expected)

def test_large_input():
    arr = list(range(1, 10001))  # 1 to 10,000
    target = 19999
    assert sorted(two_sum(arr, target)) == [9997, 9998]
