def get_factorial(num:int):
    if num in [0 , 1]:
        return 1
    return num * get_factorial(num-1)
print(get_factorial(81))
