arr = [1, 2, -4, -5]

def rearange_arr_ele(arr):
    """
    The function rearranges the elements of an array such that positive numbers are followed by negative
    numbers.
    
    :param arr: The function `rearange_arr_ele` takes a list `arr` as input and rearranges its elements
    such that all positive numbers appear first followed by negative numbers. The function separates
    positive and negative numbers into two separate lists, then alternates between adding elements from
    each list to the final result list until
    :return: The function `rearange_arr_ele` takes a list `arr` as input, separates the positive and
    negative elements into two separate lists, and then rearranges the elements in the output list `ans`
    by alternating between positive and negative elements. The function returns the rearranged list
    `ans`.
    """
    

    positive = []
    negative = []
    
    
    ans = []
    
    for ele in arr:
        if ele < 0:
            negative.append(ele)
        else:
            positive.append(ele)
    
    i = 0 # for even
    j = 0 # odd list
    
    while i < len(positive) and j < len(negative):
        
        ans.append(positive[i])
        i += 1

        ans.append(negative[j])
        j += 1
        
    
    while i < len(positive):
        ans.append(positive[i])
        i += 1
        
    while j < len(negative):
        ans.append(negative[j])
        j += 1
        
    return ans


print(rearange_arr_ele(arr=arr))