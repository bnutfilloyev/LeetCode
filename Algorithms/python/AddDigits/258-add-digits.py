class Solution:
    def addDigits(self, num: int) -> int:
            if num == 0:
                return 0

            if num % 10 == num:
                return num

            return self.addDigits(num % 10 + num // 10)
