# Time Complexity : O(n^2)
def BubbleSort(nums:list): # the list gets sorted from back
    # decrements the comparison of ele by sorting from end last_ele = 5 comparison , second_last = 4 comparison (last last ele is sorted) ...
    for i in range(len(nums)-1, 0, -1): # back type loop
        for j in range(i): # 0 -> 4
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums

# def BubbleSort(nums: list):
#     n = len(nums)
#     flag = True
#     while flag:
#         flag = False
#         for i in range(1, n):
#             if nums[i-1] > nums[i]:
#                 flag = True
#                 nums[i-1], nums[i] = nums[i], nums[i-1]
#     return nums

    
nums = [4, 2, 6, 5, 1, 3] # 6 ele => for sorting the largest ele we need n-1 comparison i.e 5
print(BubbleSort(nums=nums))
