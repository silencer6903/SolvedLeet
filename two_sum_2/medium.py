
# -->> My Solved variant with O(n) time and O(n) space. Do not know algorithms? Use hash map:)
def twoSum(numbers: list[int], target: int) -> list[int]:
    d = dict(zip(numbers, range(1, len(numbers)+1)))
    for v, i in enumerate(numbers, start=1):
        if d.get(target - i, False):
            return [v, d.get(target-i)]
    return [-1, -1]

numbers = [1]
print(twoSum(numbers, 3))

# --->>> Solved problem using Binary Search O(n) time, O(1) space
def twoSum(self, numbers: list[int], target: int) -> list[int]:
    l, r = 0, len(numbers) - 1
    while l < r:
        cur_sum = numbers[l] + numbers[r]
        if cur_sum == target:
            return [l + 1, r + 1]
        elif cur_sum < target:
            l += 1
        elif cur_sum > target:
            r -= 1
    return [-1, -1]