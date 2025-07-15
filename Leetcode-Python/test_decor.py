import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        
        # Call the function with args and kwargs
        result = func(*args, **kwargs)
        
        # Debug prints
        print('*args   :', args)
        print('**kwargs:', kwargs)
        
        end_time = time.time()
        print(f'Function {func.__name__!r} took: {end_time - start_time:.4f} sec')
        return result

    return wrapper

@timer
def example_func(num, **kwargs):
    return f"The sun is {sum(range(kwargs['num1']))}, extra args = {kwargs}"

# Call with both positional and keyword args
print(example_func(1000000, num1=78888, name="Jonathan", debug=True))
