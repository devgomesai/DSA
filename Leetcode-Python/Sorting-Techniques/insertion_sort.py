def InsertionSort(nums:list): # select second ele compare with left ele and if less than swap then next (same)
    for i in range(1, len(nums)):
        temp = nums[i]
        j = i-1
        while temp < nums[j] and j > -1:
            nums[j+1] = nums[j]
            nums[j] = temp
            j -= 1  
    return nums     


nums = [4, 2, 6, 5, 1, 3] # 6 ele => for sorting the largest ele we need n-1 comparison i.e 5
print(InsertionSort(nums=nums))