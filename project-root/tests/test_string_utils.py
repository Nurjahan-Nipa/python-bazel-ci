import pytest
from src.string_utils import reverse_string, is_palindrome, count_vowels

def test_reverse_string():
    assert reverse_string("hello") == "olleh"

def test_is_palindrome():
    assert is_palindrome("racecar") is True
    assert is_palindrome("hello") is False

def test_count_vowels():
    assert count_vowels("hello") == 2
    assert count_vowels("abcde") == 2
