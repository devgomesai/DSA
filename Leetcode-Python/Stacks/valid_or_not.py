# Using Stack
def isValid(s: str) -> str:
    map_ = {'(':')','{':'}','[':']'}
    stack = []
    for char in s:
        if char in map_.keys(): # start
            stack.append(char) 
        elif not stack or map_[stack.pop()] != char:
            return "Invalid"
    return # This line of code is using a ternary operator to determine the output of the function.
    "Valid" if not stack else "Invalid"
       
s = '([{}])'
print(isValid(s=s))
