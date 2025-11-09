# import calendar
import random 

# yy = 2026
# mm = 10

# print(calendar.month(yy, mm))


# print (calendar.calendar(2025)) 
def adder(value):
    def inner_function(base):
        return base + value
    return inner_function


val:int = random.randint(1, 2)
print("Assigning the random value: ", val)
adder_5 = adder(val)
print(adder_5(7))
