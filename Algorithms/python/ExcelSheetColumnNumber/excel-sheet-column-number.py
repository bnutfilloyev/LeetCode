class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        alphabet = {chr(i + ord('A')): i + 1 for i in range(26)}
        counter = 0
        column = list(columnTitle)
        ans = 0
        while len(column) > 0:
            ans += alphabet[column.pop()] * pow(26, counter)
            counter += 1

        return ans