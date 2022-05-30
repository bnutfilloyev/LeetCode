class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Kadanes Algorithm
        _sum = -float('inf')
        mark = 0
        for i in range(len(nums)):
            mark += nums[i]
            if mark > _sum:
                _sum = mark
            if mark < 0:
                mark = 0
        return _sum