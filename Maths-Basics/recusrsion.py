# Q1. Print "Hello" n times
def hello_r(n):
    
    if n == 0:
        return 
    
    print('Hello')
    
    hello_r(n-1)
    
# hello_r(4)

# Q2 Print 1-N
def print_n(i, n):
    
    if i > n:
        return
    
    print(i)
    
    print_n(i+1, n)
    
# print_n(1,4)

# Q3. Print n terms of N - 1
def print_n_(i):
    
    if i < 1:
        return
    
    print(i)
    
    print_n_(i-1)
    
# print_n_(4)

# Q4. Sum of first N number

def sum_n(n, sum):
    
    if n == 0:
        return sum
    
    return sum_n(n-1,sum + n)
    
# print(sum_n(5,0))


# Q5. Factorial of N
def fact_r(n):
    if n in (0,1):
        return 1
    return n * fact_r(n-1)
    
# print(fact_r(0))

# Q6. Reverse an Array : recursive
def reverse_arr_r(arr, i, j):
    
    # Base case : reverse done
    if i >= j:
        return arr
    
    # swap
    arr[i], arr[j] = arr[j], arr[i]
    
    # recursive call on next swap
    return reverse_arr_r(arr, i+1, j-1)

def reverse_arr_single_p(arr, i):
    
    if i >= len(arr)/2:
        return arr
    
    # swap
    arr[i], arr[len(arr)-i-1] = arr[len(arr)-i-1], arr[i]
    
    return reverse_arr_single_p(arr, i+1)
    



arr = [1,2,3,4,5,6]
# print(reverse_arr_single_p(arr[:], 0))
# print(reverse_arr_r(arr[:], i=0, j=len(arr)-1))

# Q7. Palindrome
def check_palindrome(s, i):
    
    if i >= len(s)/2:
        return True
    
    if s[i] != s[len(s)-i-1]:
        return False
    
    return check_palindrome(s, i+1)
    
    
s = "madam"
print(check_palindrome(s, 0))

# # Q8.  Fibonacci Series

def fib_r(n):
    if n in (0,1):
        return n
    return fib_r(n-1) + fib_r(n-2)
    
    
print(fib_r(5))

