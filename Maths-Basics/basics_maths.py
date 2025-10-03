# % => remainder
# / => quotient
# // => floor division
import math
# d = 2

# print(n % d)
# print(n / d)
# print(n // d)

# Count the number of digits
n = 4563

def get_count_of_digits(n:int):
    
    cnt = int(math.log10(n)+1)
    
    return cnt
    
# print(int(math.log10(n)+1))

# get the digits and print in the reverse order
def reverse_of_a_number(n):
    # n = 79
    revNum = 0 
    count = 0
    while n > 0:
        count += 1
        l = n % 10 # 9
        revNum = (revNum * 10) + l # 9
        n = n // 10 # 7
    print("Reverse Number: ", revNum)
    print("Number of Digits: ", count)
    return revNum

# Check Palindrome
def check_palindrome(n):
    return reverse_of_a_number(n) == n

#  Armstrong Number

#   Example 1:
#                 Input:N = 153
               
#                 Output:True
                
#                 Explanation: 1^3+5^3+3^3= 1 + 125 + 27 = 153

def isArmstrong(n): # each digit with the power of the total len
    n1 = n
    sum_ = 0
    power = len(str(n))
    while n > 0:
        l = n % 10
        sum_ +=  l ** power
        n = n // 10
        
    return n1 == sum_

def get_all_divisors(n):
    # Refer the image.png
    list_ = []
    # Optimal Way: SQRT(n)
    sqrt_n = int(math.sqrt(n))
    print(sqrt_n)
    # 6
    for i in range(1,  sqrt_n + 1):
        # 36 % (1,2,3,4,5,6) => [1,2,3,4,6]
        if n % i == 0:
            list_.append(i) # divisors
            # i => (1,2,3,4)  36 // i => [36,18,12,9]   
            # why no 6 => 6 != 36 // 6 = 6 : 6 != 6 False already done so
            if i != n // i: 
                list_.append(n//i) # quotient
            
    return sorted(list_)

def checkPrime(n):
    # A number that has exactly 2 factors (1 and n)
    # as 1 is not prime 
    # n = 5
    if n <= 1:
        return False
    
    sqrt_ = int(math.sqrt(n)) # 2
    count = 0 # total numbers divisible
    for i in range(1, sqrt_+1):
        if n % i == 0:
            count += 1
            if n // i != i:
                count += 1
    
    if count == 2:  
        return True
    
    return False

def gcd(n1, n2):
    # Time Complexity:  O(log(min(a,b)))
    # GCD = Greatest Common Divisor
    #            OR
    # HCF = Highest Common Factor
    # ----------------------------
    # n1 = 9                n2 = 12
    # Factors : n1 = {1, 3, 9}
    # Factors : n2 = {1, 2, 3, 4, 6, 12}
    # GCD(n1, n2)  = {3}
    
    while n2 != 0:
        n1, n2 = n2, n1 % n2
    return abs(n1)

print(gcd(20, 15))
    