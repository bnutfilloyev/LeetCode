import collections
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        myDictP = collections.Counter(p)
        myDictS = collections.Counter(s[:len(p)])
        output = []
        i = 0
        j = len(p)

        while j <= len(s):
            if myDictS == myDictP:
                output.append(i)

            myDictS[s[i]] -= 1
            if myDictS[s[i]] <= 0:
                myDictS.pop(s[i])

            if j < len(s):
                myDictS[s[j]] += 1
            j += 1
            i += 1

        return output

sol = Solution()
print(sol.findAnagrams("cbaebabacd", "abc")) # [0, 6]