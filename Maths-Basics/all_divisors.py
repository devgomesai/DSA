n = 153
import math



def get_all_divs(n: int):
    list_ = []
    sqrt_num = int(math.sqrt(n))
    
    for i in range(1, sqrt_num+1):
        # get all the divisors (complete devisible)
        if n % i == 0:
            list_.append(i)
            
            # get the quotient
            if i != n // i:
                list_.append(n//i)
                
    print(sorted(list_))
    
get_all_divs(n=n)