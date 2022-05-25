from typing import List


class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        low = 0
        high = len(nums) - 1
        while low <= high:
            if nums[low] == nums[high]:
                if low == high:
                    return [low]
                return [low, high]

            if nums[low] < target:
                low += 1
            if nums[high] > target:
                high -= 1



sol = Solution()
print(sol.f([1, 2, 2, 3, 4, 5], 2))
print(sol.f([1,2,5,2,3], 3))