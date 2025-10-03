from typing import List
# ** Bruth Force Approach ** => O(n)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        ele_dict = {}

        for ele in nums:
            if ele not in ele_dict.keys():
                ele_dict[ele] = 0   
            ele_dict[ele] += 1
            
        for key, val in ele_dict.items():
            if val > n // 2:
                return key
            else:
                continue

# __import__("atexit").register(lambda : open("display_runtime.txt", "w").write("0"))
# ** Optimal Approach ** =>  Moore's Voting Algorithm (max => ele > N / 2 )
def findMajority(arr):  
    n = len(arr)
    candidate = -1
    votes = 0
    
    # Finding majority candidate
    for i in range(n):
        if (votes == 0):
            candidate = arr[i]
            votes = 1
        else:
            if (arr[i] == candidate):
                votes += 1
            else:
                votes -= 1
    count = 0
    # Checking if majority candidate occurs more than n/2
    # times
    for i in range (n):
        if (arr[i] == candidate):
            count += 1
            
    if (count > n // 2):
        return candidate
    else:
        return -1
    
print(findMajority([2, 2, 1, 1, 2, 2, 2]))
            
