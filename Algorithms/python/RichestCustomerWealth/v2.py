class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        import numpy as np
        a = np. array(accounts)
        ans = a[a.sum(axis=1).argmax()]
        return np.sum(ans)