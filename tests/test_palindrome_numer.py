import pytest
from problems.ispalindrome import isPalindrome

@pytest.mark.parametrize("x, expected", [
    (121, True),         # Odd-length palindrome
    (1221, True),        # Even-length palindrome
    (22, True),          # Two-digit palindrome
    (10, False),         # Not a palindrome
    (1, True),           # Single digit
    (0, True),           # Zero is a palindrome
    (-121, False),       # Negative number (not palindrome)
    (12321, True),       # Larger odd-length palindrome
    (123321, True),      # Larger even-length palindrome
    (1001, True),        # Palindrome with zeros inside
    (100, False),        # Ends with zero, not a palindrome
    (2147447412, True),  # Large palindrome
    (2147483647, False), # Large non-palindrome (max 32-bit int)
])
def test_palindrome_number(x, expected):
    result = isPalindrome(x)
    assert result == expected