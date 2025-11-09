def moveZeroes(nums:list):
    idx = 0
    # shifting the numbers
    for num in nums:
        if num != 0:
            nums[idx] = num
            idx += 1
    # filling with zero's
    for i in range(idx, len(nums)):
        nums[i] = 0
        
    return nums


nums = [1 ,0 ,2 ,3 ,0 ,4 ,0 ,1]
arr = moveZeroes(nums)
print(arr)