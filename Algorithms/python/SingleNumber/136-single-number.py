from collections import Counter
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counter = Counter(nums)
        for j in counter.keys():
            if counter[j] == 1:
                return j
