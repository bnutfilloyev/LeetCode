from typing import List


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        i = 0
        ans = []
        while 2*i+1 <= len(nums):
            freq, val = nums[2*i], nums[2*i+1]
            for _ in range(freq):
                ans.append(val)
            i += 1
        return ans