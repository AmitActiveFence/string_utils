"""
Advanced string manipulation utilities.
"""

import unicodedata
from typing import List


def is_palindrome(s: str, normalize: bool = True) -> bool:
    """Check if a string is a palindrome."""
    if normalize:
        s = ''.join(c for c in unicodedata.normalize('NFKD', s).lower() if c.isalnum())
    return s == s[::-1]


def are_anagrams(s1: str, s2: str) -> bool:
    """Check if two strings are anagrams."""
    from collections import Counter
    return Counter(s1.replace(' ', '').lower()) == Counter(s2.replace(' ', '').lower())


def normalize_string(s: str) -> str:
    """Normalize a string (Unicode, case, whitespace)."""
    s = unicodedata.normalize('NFKC', s)
    s = s.lower()
    s = ' '.join(s.split())
    return s


def kmp_search(text: str, pattern: str) -> List[int]:
    """Knuth-Morris-Pratt substring search. Returns start indices of all matches."""
    def build_lps(pattern: str) -> List[int]:
        lps = [0] * len(pattern)
        length = 0
        i = 1
        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps
    lps = build_lps(pattern)
    result = []
    i = j = 0
    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == len(pattern):
            result.append(i - j)
            j = lps[j - 1]
        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return result


def levenshtein_distance(s1: str, s2: str) -> int:
    """Compute the Levenshtein distance between two strings."""
    if len(s1) < len(s2):
        return levenshtein_distance(s2, s1)
    if len(s2) == 0:
        return len(s1)
    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
    return previous_row[-1]


def tokenize(s: str, delimiters: str = ' ', keep_delimiters: bool = False) -> List[str]:
    """Tokenize a string by delimiters. Optionally keep delimiters as tokens."""
    import re
    if keep_delimiters:
        pattern = f'([{re.escape(delimiters)}])'
        tokens = re.split(pattern, s)
        return [t for t in tokens if t]
    else:
        pattern = f'[{re.escape(delimiters)}]+'
        return [t for t in re.split(pattern, s) if t]


def tokenize_graphemes(s: str) -> List[str]:
    """Tokenize string into grapheme clusters using the optional textplus extra."""
    try:
        import regex
    except ImportError as exc:
        raise RuntimeError(
            "tokenize_graphemes requires optional dependency 'regex'. "
            "Install with: pip install string_utils[textplus]"
        ) from exc

    return regex.findall(r"\X", s)
