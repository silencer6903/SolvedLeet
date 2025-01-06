
"""A simple solution to the problem, but I don't
know how effective it is relative to O(?) time"""

def encode(self, strs: list[str]) -> str:
    if not strs:
        return "0"
    elif len(strs) == 1 and strs[0] == str():
        return ""
    return "*%$@".join(strs)


def decode(self, s: str) -> list[str]:
    return s.split('*%$@') if s != "0" else []
