from heapq import heappush, heappop
from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        heap = []

        for idx, row in enumerate(mat):
            heappush(heap, (sum(row), idx))

        return [heappop(heap)[1] for _ in range(k)]

