class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        index = 0
        l = len(s)
        ans = ''
        while len(ans) < l:
            for i in range(len(indices)):
                if indices[i] == index:
                    index += 1
                    ans += s[i]

        return ans