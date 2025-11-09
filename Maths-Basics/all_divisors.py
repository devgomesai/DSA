import math

def get_all_divs(n: int):
    list_ = []
    sqrt_num = int(math.sqrt(n))
    
    for i in range(1, sqrt_num+1):
        # get all the divisors (complete devisible)
        if n % i == 0:
            list_.append(i)
            # get all the quotient if remainder is 0
            if i != n // i: # 6 * 6 == 36 (so we add this condition)
                list_.append(n//i)
                
    return sorted(list_)
n = int(input("Enter a number: "))
print(get_all_divs(n= n) )