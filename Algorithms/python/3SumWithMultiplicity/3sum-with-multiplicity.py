from typing import List


class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        ans = 0
        arr.sort()
        for i in range(len(arr)):
            if i > 0 and arr[i] == arr[i - 1]:
                continue
            l, r = i + 1, len(arr) - 1
            while l < r:
                s = arr[i] + arr[l] + arr[r]
                if s == target:
                    ans += r - l + 1

                    while l < r and arr[l] == arr[l + 1]:
                        l += 1
                    while l < r and arr[r] == arr[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif s < target:
                    l += 1
                else:
                    r -= 1
        return ans

