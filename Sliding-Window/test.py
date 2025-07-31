# nums = [2,7,11,15], target = 9
# seen = {2: 0}
# return [0, 1]
from typing import List
def two_sum(nums:List[int], target:int):
    seen = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        else:
            seen[num] = i
            
            
            