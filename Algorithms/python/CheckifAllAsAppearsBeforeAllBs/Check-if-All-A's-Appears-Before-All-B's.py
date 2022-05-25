class Solution:
    def checkString(self, s: str) -> bool:
        return list(s) == sorted(s)