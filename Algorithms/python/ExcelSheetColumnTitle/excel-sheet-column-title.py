class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        alphabet = {i: chr(i + ord('A')) for i in range(26)}
        result = ''
        while columnNumber > 0:
            result = alphabet[(columnNumber - 1) % 26] + result
            columnNumber = (columnNumber - 1) // 26
        return result


answer = Solution()
print(answer.convertToTitle(15))
