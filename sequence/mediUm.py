from collections import defaultdict
"""Subtract from each element in the list 1 and in the absence of                                                      
such a result in the Set enter the 2nd cycle with the variable 
Length and add to it AND checking whether there is such a value
in the Set if there is a continuous. At the end of this loop, we
choose which is longer String or the standard value of the variable 
before entering the loop"""
# O(n) -> time
# O(n) -> space
def longestConsecutive(nums: list[int]) -> int:
        map_set = set(nums)
        longest = 0

        for i in map_set:
            if i-1 not in map_set:
                length = 1
                while (i + length) in map_set:
                    length += 1
                longest = max(longest, length)
        return longest
L  = [0, 1]
print(longestConsecutive(L))