arr = [65, 9 ,75, 58 ,78, 61, 18]

def get_highest_value(arr:list):
    max_ = arr[0]
    for i in range(1,len(arr)):
        if max_ < arr[i]:
            max_ = arr[i]
    return max_

print(get_highest_value(arr))