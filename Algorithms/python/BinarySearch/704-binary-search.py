from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            temp = nums[mid]

            if temp == target:
                return mid

            if temp > target:
                high = mid - 1
            else:
                low = mid + 1

        return -1