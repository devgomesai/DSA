memo = [None] * 20

counter= 0

def fib(n: int):
    global counter
    counter += 1
    if memo[n] is not None:
        return memo[n]
    
    # base case 
    if n == 0 or n == 1:
        return n
    
    memo[n] = fib(n-1) + fib(n-2)
    
    return memo[n]

n = 14
print('\nFib of ',n,'=',fib(n))
print('\nCounter: ',counter)

''' 
  Output:
  
    Fib of  30 = 832040

    Counter:  59
'''