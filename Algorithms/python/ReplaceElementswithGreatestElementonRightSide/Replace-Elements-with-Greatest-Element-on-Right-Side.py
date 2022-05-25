from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # for i in range(1, len(arr)):
        #     arr[i - 1] = max(arr[i:])
        #
        # arr[-1] = -1
        # return arr

        m=arr[-1]
        for i in range(len(arr)-2,-1,-1):
            temp=max(m,arr[i])
            arr[i]=m
            m=temp

        arr[-1]=-1

        return arr
