import re


def isPalindrome(s: str) -> bool:
    s = re.sub(r"[^a-z0-9]", '', s.lower().replace(' ', ''))
    print(s, s[::-1])
    return s == s[::-1]


s="0P"
print(isPalindrome(s))