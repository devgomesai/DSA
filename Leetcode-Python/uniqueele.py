nums = [1, 1, 2, 2, 2, 3, 3, 4]


def get_unique_element(nums: list):
    # Method 1
    n1 = len(set(nums))
    # Method 2
    n = len(nums)
    i = 0
    
    for j in range(1, n):
        
        if (nums[j] != nums[i]):
            
            nums[i+1] = nums[j]
            i += 1
            
    return i + 1, n1

# print(get_unique_element(nums=nums))


arr = [1, 2, 1, 2, 3, 3, 4, 4, 8]  # All elements appear twice except 4


def __get_unique_ele_from__arr__(nums: list):
    ele = 0
    for num in nums:
        ele ^= num
    
    return ele
print(__get_unique_ele_from__arr__(nums=arr))

