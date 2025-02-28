"""Importing necessary functions"""

from src.string_utils import reverse_string, is_palindrome, count_vowels


def test_reverse_string():
    """
    Tests the reverse_string function.
    """
    assert reverse_string("hello") == "olleh"
    assert reverse_string("Python") == "nohtyP"
    assert reverse_string("racecar") == "racecar"  # Palindrome remains the same
    assert reverse_string("") == ""  # Edge case: empty string
    assert reverse_string("a") == "a"  # Single character remains the same


def test_is_palindrome():
    """
    Tests the is_palindrome function.
    """
    assert is_palindrome("racecar") is True
    assert is_palindrome("hello") is False
    assert (
        is_palindrome("A man a plan a canal Panama") is True
    )  # Handles spaces and case
    assert (
        is_palindrome("No lemon, no melon") is True
    )  # Palindrome with punctuation removed
    assert is_palindrome(" ") is True  # Edge case: Single space is a palindrome
    assert is_palindrome("") is True  # Edge case: Empty string is a palindrome


def test_count_vowels():
    """
    Tests the count_vowels function.
    """
    assert count_vowels("hello") == 2
    assert count_vowels("abcde") == 2
    assert count_vowels("AEIOUaeiou") == 10  # All vowels
    assert count_vowels("rhythm") == 0  # No vowels
    assert count_vowels("") == 0  # Edge case: Empty string
    assert count_vowels("PYTHON") == 1  # Only 'O' is a vowel
