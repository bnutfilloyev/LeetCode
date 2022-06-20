class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:
        def check(unit_digit, X):
            for times in range(1, 11):
                digit = (X * times) % 10
                if (digit == unit_digit):
                    return times
            return -1

        unit_digit = num % 10
        times = check(unit_digit, k)
        if (times == -1):
            return times
        else:
            if (num >= (times * k)):
                return times
            else:
                return -1



sol = Solution()
x = sol.minimumNumbers(58, 9)
print(x)
