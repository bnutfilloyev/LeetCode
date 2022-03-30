from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        for row in matrix:
            if row[0] <= target <= row[-1]:
                return target in row
        return False

ans = Solution()
print(ans.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 3))