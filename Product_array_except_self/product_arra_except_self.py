# Algorithm with product numbers without nums[i]

nums = [1,2,4,6]
res = [1] * len(nums)

for i in range(1, len(nums)): #-> Save in list left side product numbers without first element.
    res[i] = res[i-1] * nums[i-1] # -> Result: [1, 1, 2, 8] -> each iteration -> res[i-1] * nums[i-1] -> 1 * 1 ... last iter -> [1, 2] * 4 or res[i-1] * 4
right = nums[-1] # -> Init  last element from nums for saving results of multy elements from nums
for i in range(len(nums)-2, -1, -1): # -> Multy elements from right side nums to res
    res[i] *= right
    right *= nums[i] # -> Save result of multy for next to multy each element our result list

print(res)

url = 'https://leetcode.com/problems/product-of-array-except-self/'

"""
============================================================
1 2 4 6 |1
1 2 4 6 |2 ->  Numbers that we need to skip each row iteration 
1 2 4 6 |4
1 2 4 6 |6
1    |     |2 4 6
1 2  |  *  |  4 6
1 2 3|     |    6  
=============================================================
"""