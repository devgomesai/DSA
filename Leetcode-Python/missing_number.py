def missing_number(nums:list):
    # cause I know the end
    max_ele = max(nums)
    
    # get the sum of numbers in order including the missing number
    total_sum = sum(range(1, max_ele+1))
    
    # get the sum of numbers in the arr (the arr where the number is missing)
    arr_sum = sum(nums)
    
    # get the abs diff
    return abs(total_sum - arr_sum)

arr =  [1,2,4,5]
print(missing_number(arr))