# Time Complexity : O(n^2)
def SelectionSort(nums: list):
    n = len(nums)
    for i in range(n): # assuming that i'th index is the min_value
        min_index = i # setting the ith as min_idx
        for j in range(i+1, n): # check from next of it if value at that index is smaller then set as min
            if nums[j] < nums[min_index]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]
    return nums

nums = [4, 2, 6, 5, 1, 3]
print(SelectionSort(nums=nums))