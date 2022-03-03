class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_list = list(s)[::-1]
        count = len(s_list)
        if count <= 0:
            return True

        temp = s_list.pop()
        for i in t:

            if i == temp:
                count = len(s_list)
                if count <= 0:
                    return True
                temp = s_list.pop()

        return False


ans = Solution()
print(ans.isSubsequence("abc", "ahbgdc"))
