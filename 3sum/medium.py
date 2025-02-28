def threeSum(nums: list[int]) -> list[list[int]]:
    nums.sort()
    res = []

    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        l, r = i + 1, len(nums) - 1
        while l < r:
            sums = nums[i] + nums[l] + nums[r]
            if sums > 0:
                r -= 1
            elif sums < 0:
                l += 1
            else:
                res.append([nums[i], nums[l], nums[r]])
                l += 1
                while nums[l] == nums[l - 1] and l < r:
                    l += 1



    return res



nums =  [-1,0,1,2,-1,-4]

print(threeSum(nums), len(threeSum(nums)))