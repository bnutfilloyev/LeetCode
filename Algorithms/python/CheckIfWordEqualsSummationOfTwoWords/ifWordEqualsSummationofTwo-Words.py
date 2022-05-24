class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        num1 = "".join([str(ord(i)-97) for i in firstWord])
        num2 = "".join([str(ord(i)-97) for i in secondWord])
        num3 = "".join([str(ord(i)-97) for i in targetWord])

        if int(num1) + int(num2) == int(num3):
            return True
        return False


