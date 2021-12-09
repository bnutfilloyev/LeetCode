class Solution:
    def canReach(self, arr, start: int) -> bool:
        if start >= 0 and start < len(arr) and arr[start] >= 0:
            if arr[start] == 0:
                return True
            arr[start] = -arr[start]
            return self.canReach(arr, start + arr[start]) or self.canReach(arr, start - arr[start])
        return False
sol = Solution()
print(sol.canReach( [3,0,2,1,2], 2))