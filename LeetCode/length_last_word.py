def lengthOfLastWord(s: str) -> int:
    return len(s.strip().split()[-1])

result = lengthOfLastWord('hallo nama saya  k jhga khmzkuun')
print(result)