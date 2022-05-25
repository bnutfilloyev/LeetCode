class Solution:
    def digitSum(self, s: str, k: int) -> str:
        l = len(s)
        ans = 0
        while l > 0:
            num = s[:3]
            print(num)
            s = s[3:]
            l = len(s)
            for i in num:
                ans += int(i)

        return str(ans)

sol = Solution()
print(sol.digitSum("11111222223", 3))