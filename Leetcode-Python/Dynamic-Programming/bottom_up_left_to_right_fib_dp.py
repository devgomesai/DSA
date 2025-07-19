

counter = 0

def fib(n):
    global counter
    fib_list = [0, 1]
    for index in range(2, n+1):
        counter += 1
        fib_list.append(fib_list[index-1] + fib_list[index-2])
    
    return fib_list[n], fib_list, counter


n = 30
value, list_, c = fib(n)
print('\nFib of ',n,'=',value)
print("\nfib_list: ",list_)
print("\nCounter ", c)