class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res, prefix_sum = 0, 0
        seen = {}

        for num in nums:
            seen[prefix_sum] = seen.get(prefix_sum, 0) + 1
            prefix_sum += num
            res += seen.get(prefix_sum - k, 0)

        return res