class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        from math import pow
        return pow(x, n)

sol = Solution
print(sol.myPow(2.0, 10))
