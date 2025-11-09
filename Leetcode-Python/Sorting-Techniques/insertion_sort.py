# Time Complexity : O(n^2)
def InsertionSort(nums:list): # select second ele compare with left ele and if less then swap (same)
    for i in range(1, len(nums)):
        # storing purpose only then on swap used
        temp = nums[i] # 2  
        # i = j+1
        j = i-1
        while temp < nums[j] and j > -1:
            nums[j+1] = nums[j]
            nums[j] = temp
            j -= 1
    return nums


nums = [4, 2, 6, 5, 1, 3] # 6 ele => for sorting the largest ele we need n-1 comparison i.e 5
print(InsertionSort(nums=nums))


