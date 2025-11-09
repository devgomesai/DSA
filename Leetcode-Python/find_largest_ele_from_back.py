nums = [13,4,7,2,-3,1,4,2]
# 8  (0 => 7) {0, 1, 2, 3, 4, 5, 6, 7}


def get_largest_ele(nums:list):
    # length of the arr => nums
    n = len(nums) 
    largest_ele = nums[n-1]
    print(largest_ele)
    # comaparing from back
    for i in range(n-2, -1, -1):
        if nums[i] > largest_ele:
            largest_ele = nums[i]
    
    return largest_ele
        
    
print(get_largest_ele(nums=nums))