# 0  a         g    => ag 
# 1  b     f   h    => bfh
# 2  c  e      i    => cei
# 3  d              => d
# Last String = agbfhceid

s = "abcdefghi"
numRows = 4

s1 = len(s)

# one bucket per row
arr = [""] * numRows  

i = 0          # current index in string
row = 0        # current row
down = True    # direction

while i < s1:
    # logic to add to the str
    arr[row] += s[i]
    i += 1

    # up and down dir
    if down:
        row += 1
        if row == numRows - 1:   # hit bottom, go up
            down = False
    else:
        row -= 1
        if row == 0:             # hit top, go down
            down = True
print(arr)

result = "".join(arr)
print(result)  # agbfhceid


