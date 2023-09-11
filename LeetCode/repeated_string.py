def repeatedSubstringPattern(s: str) -> bool:
    return s in (s+s)[1:-1]

is_repeated = repeatedSubstringPattern('abab')
print(is_repeated)
