# Time Complexity : O(n^2)
def SelectionSort(nums: list):
    for i in range(len(nums) - 1): # assuming that i'th index is the min_value
        min_index = i
        for j in range(i+1, len(nums)):
            if nums[j] < nums[min_index]:
                min_index = j
        # on iterating over the list to find min_index if i == min_index that means its already sorted
        if i != min_index:
            # only swap if change in min_index
            nums[j], nums[min_index] = nums[min_index], nums[j]


nums = [4, 2, 6, 5, 1, 3]
print(SelectionSort(nums=nums))