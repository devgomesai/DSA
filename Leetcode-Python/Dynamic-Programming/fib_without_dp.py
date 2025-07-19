# Dynamic Programming
counter = 0


def fib(n):
    global counter
    counter += 1
    if n == 0 or n == 1:
        return n
    return fib(n-1) + fib(n-2)
    
    
    
n = 30
print('\nFib of ',n,'=',fib(n))
print('\nCounter: ',counter)

''' 
  Output:
  
    Fib of  30 = 832040

    Counter:  2692537
'''

