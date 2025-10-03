arr = [-2,1,-3,4,-1,2,1,-5,4]

# **Brute force**
# def get_all_sub_arrays(nums: list):
#     max_sum = float('-inf')
#     all_arrays = []
#     n = len(nums)
#     for i in range(n):
#         for j in range(i, n+1):
#             if len(nums[i:j]) != 0: 
#                 if max_sum < sum(nums[i:j]):
#                     max_sum = sum(nums[i:j])
#                 all_arrays.append(nums[i:j])
#     return all_arrays, max_sum


# **Better**
# def get_all_sub_arrays(nums: list):
    
#     max_sum = float('-inf')
#     all_arrays = []
    
#     n = len(nums)
#     for i in range(n): # 0 , 1, 2, 3, 4
#         sum_arr = 0
#         temp_arr = []
#         for j in range(i, n): # 0->0, 0->1, 0->2, 0->3, 0->4
            
#             sum_arr += nums[j]
#             temp_arr.append(nums[j])
#             all_arrays.append(temp_arr.copy())
            
#             if sum_arr > max_sum:
#                 max_sum = sum_arr
                
#     return all_arrays, max_sum

def get_all_sub_arrays(nums: list):
    n = len(nums)
    max_sum = float('-inf')
    sum_ = 0
    
    ans_start = -1
    ans_end = -1
    
# arr = [-2,1,-3,4,-1,2,1,-5,4]
    
    for i in range(n):
        
        if sum_ == 0:
            start = i
            
        sum_ += nums[i]
        
        if sum_ > max_sum:
            max_sum = sum_
            ans_start = start
            ans_end = i
            
        if sum_ < 0:
            sum_ = 0
            
    return max_sum, ans_start, ans_end

    
max_sum, s, e = get_all_sub_arrays(nums=arr)
# print("The Sub-Array's are: ", total_subarrys)
print("The Max sum: ", max_sum)
print("Sub-array: ",arr[s:e+1])