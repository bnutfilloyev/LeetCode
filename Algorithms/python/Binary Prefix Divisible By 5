class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        for i in range(1,len(nums)):
            nums[i]+=nums[i-1]*2
            nums[i-1]=(nums[i-1]%5==0)
        nums[-1]=(nums[-1]%5==0)
        return nums
