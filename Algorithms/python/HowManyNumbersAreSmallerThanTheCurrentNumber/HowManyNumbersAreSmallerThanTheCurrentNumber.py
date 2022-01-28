class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # Solution 1:
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        # nums_sorted = sorted(nums)
        # res = []
        # for num in nums:
        #     res.append(nums_sorted.index(num))
        # return res

        # Solution 2:
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        # res = []
        # for i in range(len(nums)):
        #     count = 0
        #     for j in range(len(nums)):
        #         if nums[j] < nums[i]:
        #             count += 1
        #     res.append(count)
        # return res

        # Solution 3:
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        # res = []
        # for i in range(len(nums)):
        #     count = 0
        #     for j in range(len(nums)):
        #         if nums[j] < nums[i]:
        #             count += 1
        #     res.append(count)
        # return res

        # Solution 4:
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        # res = []
        # for i in range(len(nums)):
        #     count = 0
        #     for j in range(len(nums)):
        #         if nums[j] < nums[i]:
        #             count += 1
        #     res.append(count)
        # return res

        # Solution 5:
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        # res = []
        # for i in range(len(nums)):
        #     count = 0
        #     for j in range(len(nums)):
        #         if nums[j] < nums[i]:

        # Solution 6:
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        res = []
        for i in nums:
            summ = 0
            for j in nums:
                if i>j:
                    summ += 1
            res.append(summ)
        return res