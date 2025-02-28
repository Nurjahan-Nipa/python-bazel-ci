"""
string_utils.py

This module provides string utility functions such as reversing strings,
checking palindromes, and counting vowels.
"""

def reverse_string(s: str) -> str:
    """Reverses the given string."""
    return s[::-1]

def is_palindrome(s: str) -> bool:
    """Checks if a string is a palindrome."""
    s = s.lower().replace(" ", "")  # Normalize case and spaces
    return s == s[::-1]

def count_vowels(s: str) -> int:
    """Counts the number of vowels in a string."""
    vowels = "aeiou"
    return sum(1 for char in s.lower() if char in vowels)
