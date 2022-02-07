

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = list(s)
        t = list(t)
        for i in sorted(s):
            for j in sorted(t):
                if i == j:
                    s.remove(i)
                    t.remove(j)
                    break
        return t[0]


sol = Solution()


print(sol.findTheDifference("abcd", "abcde"))