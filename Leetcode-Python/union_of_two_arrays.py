def union_of_two_arrs(nums1: list, nums2: list):
    
    s1 = set(nums1)
    s2 = set(nums2)
    union_list = list( s1 | s2)
    return union_list

print(union_of_two_arrs([1,2,3,4,5], [2,3,4,4,5]))
