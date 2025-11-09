# from functools import lru_cache

# @lru_cache
# def fib(n):
#     if n in (1, 0):
#         return n
#     return fib(n-1) + fib(n-2)

# print(fib(34))

# Create a dict and cal fibonacci
def fibonacci(n:int, state={}):
    
    if n in state:
        return state[n]
    
    if n <= 1:
        return n
    
    state[n] = fibonacci(n-1) + fibonacci(n-2)
    
    return state[n]

print(fibonacci(45))