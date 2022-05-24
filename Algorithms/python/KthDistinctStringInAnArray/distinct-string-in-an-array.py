from collections import Counter
from typing import List


class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        ct = Counter(arr)

        for item, value in ct.items():
            if value == 1:
                if k != 1:
                    k -= 1
                    continue

                return item
        return ""