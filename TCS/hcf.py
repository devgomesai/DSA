# def gcd(a:int, b:int):
#     if b == 0:
#         return a
#     return gcd(b, a%b)

# print(gcd(24, 12))

from typing import Any
import math

# HCF = product of two numbers / LCM
def get_divisble(n:int):
    
    n_s = int(math.sqrt(n))
    result = []
    for i in range(1, n_s+1):
        if n % i == 0: # if remainder is 0
            result.append(i) # add the divisor 
            
            if i != n // i: # check if not same as 
                result.append(n//i) # add q
    print("Divisible numbers for (%d): "%n,sorted(result))
    return sorted(result), n

def gcd(a1: tuple, a2: tuple):
    common = set[Any](a1[0]) & set[Any](a2[0])
    return max(common) if common else None

n1 = int(input("Enter n1: "))
n2 = int(input("Enter n2: "))

gcd_val =  gcd(get_divisble(n1), get_divisble(n2))
print("GCD: %s" %gcd_val)
print("LCM: %d" %((n1*n2) // gcd_val))