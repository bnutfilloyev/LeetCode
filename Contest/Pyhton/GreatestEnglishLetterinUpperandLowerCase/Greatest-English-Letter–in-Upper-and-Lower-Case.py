

class Solution:
    def greatestLetter(self, s: str) -> str:
        ans = []
        for i in s:
            if i.islower():
                if i.upper() in s:
                    ans.append(i.upper())
            if i.isupper():
                if i.lower() in s:
                    ans.append(i.upper())
        if len(ans):
            return sorted(ans)[-1]
        return ""

sol = Solution()
print(sol.greatestLetter("arRAzFif"))