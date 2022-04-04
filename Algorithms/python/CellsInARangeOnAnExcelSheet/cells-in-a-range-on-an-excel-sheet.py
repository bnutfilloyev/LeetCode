from typing import List
import string


class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        answer = []
        letters = string.ascii_uppercase
        first = s.split(":")[0]
        last = s.split(":")[1]
        first_col, first_row = first[0], int(first[1])
        last_col, last_row = last[0], int(last[1])
        columns = letters[letters.index(first_col): letters.index(last_col) + 1]

        for i in columns:
            for j in range(first_row, last_row + 1):
                answer.append(i + str(j))
        return answer


answer = Solution()
print(answer.cellsInRange("A1:F2"))