# string_utils

Advanced string manipulation utilities for Python.

## Features
- Palindrome detection
- Anagram checking
- String normalization (Unicode, case, whitespace)
- Substring search (KMP algorithm)
- Levenshtein distance
- Customizable string tokenization

## Installation
```bash
pip install .
```

## Usage
```python
from string_utils.advanced import is_palindrome, are_anagrams, normalize_string, kmp_search, levenshtein_distance, tokenize

print(is_palindrome("A man a plan a canal Panama"))
print(are_anagrams("listen", "silent"))
print(normalize_string("  Café   au Lait  "))
print(kmp_search("ababcabcabababd", "ababd"))
print(levenshtein_distance("kitten", "sitting"))
print(tokenize("a,b;c.d", delimiters=",;.", keep_delimiters=True))
print(string_to_base64("hello"))
```

## Testing
```bash
pytest
```
