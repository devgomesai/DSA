# In QuickSort we start with a pivot point i.e the first item   
# O(n) => pivot func() as it traverses the list
# O(log n) => as you divide the list and then sort recursive call
# O(n^2) => if list is already sorted

def swap(nums, index1, index2):
    nums[index1], nums[index2] = nums[index2], nums[index1]

# *** Finding the pivot index func() ***
def pivot(nums, pivot_index, end_index):
    # initially we assume pivot as idx = 0
    swap_index = pivot_index
    
    for i in range(pivot_index+1, end_index+1):
        if nums[i] < nums[pivot_index]:
            swap_index += 1
            swap(nums, swap_index, i)
            # print(nums)
    swap(nums, pivot_index, swap_index)
    # print(nums) 
    return swap_index # this is your mid_idx (pivot_point)

# QuickSort func()
def QuickSort(nums:list, left_, right_):
    if left_ < right_:
        pivot_point = pivot(nums,left_,right_)
        QuickSort(nums, left_, pivot_point-1)
        QuickSort(nums, pivot_point+1   , right_)


def __quick_sort_helper_func__(nums):
    QuickSort(nums, 0, len(nums)-1)

nums = [1,2,4,3,5,6,7]   
print('Original list: ', nums) 
__quick_sort_helper_func__(nums=nums)
print('After Sorting: ',nums)