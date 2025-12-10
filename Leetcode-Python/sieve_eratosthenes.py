def sieve_eratosthenes(n: int):
    
    res = [True] * (n + 1)
    # prime number starts from 2
    p = 2
    # 0 and 1 are not prime so set them to false
    res[0], res[1] = False, False
    
    # loop through till sqr of number is <= n
    while p * p <= n:
        # if True i.e prime
        if res[p]:
            # set its multiple as False i.e not prime
            for i in range(p*p, n+1, p):
                res[i] = False
        # move to next i i.e 3,...
        p += 1
        
    result = [i for i in range(0, len(res)) if res[i]]
    
    return result

print(sieve_eratosthenes(10))