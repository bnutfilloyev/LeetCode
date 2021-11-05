class Solution:
    def arrangeCoins(self, n: int) -> int:
        s = 0
        i = 0
        while s <= n:
            i += 1
            s = i*(i+1)//2
         
        return i - 1