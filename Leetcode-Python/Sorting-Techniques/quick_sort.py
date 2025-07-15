# In QuickSort we start with a pivot point i.e the first item   
def swap(nums, index1, index2):
    nums[index1], nums[index2] = nums[index2], nums[index1]

# *** Finding the pivot index func() ***
def pivot(nums, pivot_index, end_index):
    swap_index = pivot_index
    
    for i in range(pivot_index+1, end_index+1):
        if nums[i] < nums[pivot_index]:
            swap_index += 1
            swap(nums, swap_index, i)
    # print(nums)
    swap(nums, pivot_index, swap_index)
    # print(nums) 
    return swap_index

# QuickSort func()
def QuickSort(nums:list, left_, right_):
    if left_ < right_:
        pivot_point = pivot(nums,left_,right_)
        QuickSort(nums, left_, pivot_point-1)
        QuickSort(nums, pivot_point+1, right_)

    return nums


def __quick_sort_helper_func__(nums):
    return QuickSort(nums, 0, len(nums)-1)

nums = [4, 6, 1, 7, 3, 2, 5]    
print(__quick_sort_helper_func__(nums=nums))