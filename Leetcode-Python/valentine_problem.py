# You're at a Valentine's Day party alone.
# Everyone else is in couples, and each couple has the same ID number.
# You, however, have a unique ID number written on your back, so you can't see it.
# Given a list of all the ID numbers, can you write code to find your unique ID number?

members = [11, 11, 22, 33, 22, 33, 44, 5, 44]
# so 5 is your unique id number

# Approach 1: Bit wise Operator  ( ^ ) :- XOR Operator
def find_unique_id(ids_:list):
    uniq_id = 0
    
    for id in ids_:
        uniq_id ^= id
        
    return uniq_id
    
    
number = find_unique_id(ids_= members)
print(number)
# Approach 2: Using Count Frequency 
def find_unique_id_(ids_:list):
    
    hashmap = {}
    
    for id in ids_:
        hashmap[id] = hashmap.get(id, 0) + 1
        
    
    for key, val in hashmap.items():
        if val == 1:
            return key
    

number = find_unique_id_(ids_= members)
print(number)



