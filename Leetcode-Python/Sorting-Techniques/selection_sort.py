def SelectionSort(nums: list): # the list gets sorted from front
    for i in range(len(nums)-1):
        min_index = i
        for j in range(i+1, len(nums)):
            if nums[j] < nums[min_index]:
                min_index = j
        if i != min_index:
            nums[i], nums[min_index] = nums[min_index], nums[i]  
    return nums



nums = [4, 2, 6, 5, 1, 3]
print(SelectionSort(nums=nums))