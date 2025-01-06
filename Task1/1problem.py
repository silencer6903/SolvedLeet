from  collections import Counter as ct, deque


def groupAnagrams(strs: list[str]) -> list[list[str]]:
    res = {}
    for i, v in enumerate(strs):
        s = ''.join(sorted(v))
        if s in res:
            res.setdefault(s, []).append(v)
        else:
            res.setdefault(s, []).append(v)


    res = sorted(res.values(), key=lambda s: len(s))

    return res
s =["eat","tea","tan","ate","nat","bat"]

print(groupAnagrams(s))

b = [["max"],["buy"],["doc"],["may"],["ill"],["duh"],["tin"],["bar"],["pew"],["cab"]]
print([*map(lambda s: ord(s[0][0]), b)])


