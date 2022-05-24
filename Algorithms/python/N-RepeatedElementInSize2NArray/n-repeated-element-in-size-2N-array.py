class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        ct = Counter(nums)

        for key, value in ct.items():
            if value == len(nums) // 2:
                return key