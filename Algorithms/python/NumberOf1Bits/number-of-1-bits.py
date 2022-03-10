class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += n & 1
            n >>= 1
        return count


if __name__ == "__main__":
    solution = Solution()
    print(solution.hammingWeight(11))