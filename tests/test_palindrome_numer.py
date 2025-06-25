import pytest
from problems.ispalindrome import isPalindrome

@pytest.mark.parametrize("x, expected", [
    (121, True),
    (1221, True),
    (22, True), 
    (10, False),
    (1, True),
])
def test_palindrome_number(x, expected):
    result = isPalindrome(x)
    assert result == expected

