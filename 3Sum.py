def threeSum(nums):
    arr = []
    nums.sort()
    l = len(nums)
    for i in range(l):
        j = i + 1
        k = l - 1
        while j < k:
            sum = nums[i] + nums[j] + nums[k]
            if  sum == 0  :
                arr.append([nums[i] , nums[j] , nums[k]])
                k -= 1
                j += 1
            elif sum < 0:
                k -= 1
            else:
                j += 1
    return set(arr)

nums = [0,0,0,0]
print(threeSum(nums))