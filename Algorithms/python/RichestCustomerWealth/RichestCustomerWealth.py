class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        max = 0
        for i in accounts:
            sub_max = 0
            for j in i:
                sub_max += j
                if sub_max > max:
                    max = sub_max
        return max