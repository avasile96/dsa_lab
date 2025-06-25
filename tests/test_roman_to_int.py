import pytest
from problems.roman_to_int import Solution

@pytest.mark.parametrize("roman, expected", [
    ("III", 3),         # Simple addition
    ("IV", 4),          # Subtractive notation
    ("IX", 9),          # Subtractive notation
    ("LVIII", 58),      # L=50, V=5, III=3
    ("MCMXCIV", 1994),  # M=1000, CM=900, XC=90, IV=4
    ("XL", 40),         # Subtractive notation
    ("XC", 90),         # Subtractive notation
    ("CD", 400),        # Subtractive notation
    ("CM", 900),        # Subtractive notation
    ("MMXXIV", 2024),   # Large number
    ("I", 1),           # Smallest value
    ("MMMCMXCIX", 3999) # Largest standard Roman numeral
])
def test_roman_to_int(roman, expected):
    sol = Solution()
    assert sol.romanToInt(roman) == expected