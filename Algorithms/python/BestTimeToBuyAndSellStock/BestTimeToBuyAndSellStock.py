from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = prices[0]
        profit = 0
        for i in prices:
            if min > i:
                min = i
            elif i - min > profit:
                profit = i - min
        return profit