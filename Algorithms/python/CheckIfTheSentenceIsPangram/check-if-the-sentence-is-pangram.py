class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        if len(sentence) < 26:
            return False

        temp = [chr(i) for i in range(ord('a'), ord('z') + 1)]
        if sorted(set(sentence)) == temp:
            return True
        return False