# In QuickSort we start with a pivot point i.e the last ele
# O(n) => pivot func() as it traverses the list
# O(log n) => as you divide the list and then sort recursive call
# O(n^2) => if list is already sorted => bad pivot
# O(n*logn) => avg case w

def quicksort(arr:list):
    
    # Base case: 1 or 0 item in the list
    if len(arr) <= 1:
        return arr
    
    # Setting last ele as pivot / middile ele / first ele
    # Set first ele as pivot
    pivot = arr[0]
    
    
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]
    
    return quicksort(left) + [pivot] + quicksort(right)



nums = [4,5,7,2,1,3,6]   
print('Original list: ', nums) 
nums = quicksort(nums)
print('After Sorting: ',nums)