
# Input: nums = [3,4,7,2,-3,1,4,2], k = 7
# Output: [[3,4], [7], [7,2,-3,1], [1,4,2]]

def subarray_sum(arr: list, target: int):
    sub_array = []
    
    n = len(arr)
    # start pointer 
    for i in range(n):
        # initially sum is 0
        curr_sum = 0
        # Traverse from i index to end
        for j in range(i, n):
            # just add to sum if sum > target we ignore that i and j (skip that sum)
            curr_sum += arr[j]
            # check 
            if curr_sum == target:
                print("Start Index where we got the sum: ", i)
                sub_array.append(arr[i:j+1])
            
    return sub_array
            
            

    
# nums = [3,4,7,2,-3,1,4,2]
nums = [3,4,7,8,9,10,11,12]
k = 7
print(subarray_sum(nums, k))