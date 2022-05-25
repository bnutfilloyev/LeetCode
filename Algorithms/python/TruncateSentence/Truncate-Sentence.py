class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        temp = s.split()
        return " ".join(temp[:k])
