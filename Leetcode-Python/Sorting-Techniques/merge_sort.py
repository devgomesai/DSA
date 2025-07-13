# Big O: 
# Space Complexity: O(n)
# Time Complexity : O(log n) + O(n) = O(n log n)
# Breaking it is O(log n) and then combining them is O(n)


def merge(list1: list, list2: list):
    combined = []
    i = 0 
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            j += 1
    # append the list that still has elements
    while i < len(list1):
        combined.append(list1[i])
        i += 1
    
    while j < len(list2):
        combined.append(list2[j])
        j += 1
        
    return combined

def MergeSort(nums: list):
    
    # 2. Base Case: when len(the_list) is 1
    if len(nums) == 1:
        return nums
    
    # 1. Break the list in half
    mid = int(len(nums) / 2)
    left, right = MergeSort(nums[:mid]), MergeSort(nums[mid:])
    
    # 3. Use merge() to push lists together
    return merge(left, right)
    
nums = [4, 2, 6, 5, 1, 3]
print(MergeSort(nums))
