class Solution:
    def minTimeToType(self, word: str) -> int:
        ini = 'a'
        count = 0
        for i in word:
            x = abs(ord(ini) - ord(i))
            count += min(x, 26-x) + 1
            ini = i
        return count