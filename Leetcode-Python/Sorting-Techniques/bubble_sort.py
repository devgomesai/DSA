# Time Complexity : O(n^2)
def BubbleSort(nums:list): # the list gets sorted from back
    # decrements the comparison of ele by sorting from end last_ele = 5 comparison , second_last = 4 comparison (last last ele is sorted) ...
    for i in range(len(nums)-1, 0, -1): # start from back
        for j in range(i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
            # print(nums)
    return nums
    
    
nums = [4, 2, 6, 5, 1, 3] # 6 ele => for sorting the largest ele we need n-1 comparison i.e 5
print(BubbleSort(nums=nums))