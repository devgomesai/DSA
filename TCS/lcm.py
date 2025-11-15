import math
from typing import Any
# LCM = product of two numbers / HCF

def get_divisble(n:int):
    
    n_s = int(math.sqrt(n))
    result = []
    for i in range(1, n_s+1):
        if n % i == 0: # if remainder is 0
            result.append(i) # add the divisor 
            
            if i != n // i: # check if not same as 
                result.append(n//i)
    print("%d: " %n,sorted(result), "\n")
    return sorted(result), n


def lcm(a1: tuple, a2: tuple):
    common = set[Any](a1[0]) & set[Any](a2[0])
    return int(a1[1] * a2[1] / max(common)) # max(common) = HCF

print("LCM: ",lcm(get_divisble(12), get_divisble(24)))