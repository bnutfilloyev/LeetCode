from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        srt = sorted(heights)
        count = 0
        for i, j in zip(srt, heights):
            if i != j:
                count += 1
        return count