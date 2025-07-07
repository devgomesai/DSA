def get_number_factorial(num:int):
    if num in [0, 1]:
        return 1
    return num * get_number_factorial(num-1)

print(get_number_factorial(67))
    