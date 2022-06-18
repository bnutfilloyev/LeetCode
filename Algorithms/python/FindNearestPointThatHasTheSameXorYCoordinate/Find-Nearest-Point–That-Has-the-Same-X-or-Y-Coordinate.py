from typing import List


class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        dist = -1
        index = -1
        for i, j in enumerate(points):
            xi, yi = j
            if x == xi or y == yi:
                temp = abs(x - xi) + abs(y - yi)
                if dist == -1 or temp < dist:
                    dist = temp
                    index = i
        return index
