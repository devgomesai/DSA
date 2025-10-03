#  O(n·k)
def window_arr1(arr:list, k:int):
    sub_arr = []
    i  = 0
    while k <= len(arr):
        sub_arr.append(arr[i:k])
        i  += 1
        k += 1
    return sub_arr

# Better Sliding Window
def window_arr2(arr: list, k:int):
    sub_arr = []
    
    # Base Case
    if len(arr) < k:
        return arr
    
    sub_arr.append(arr[:k])
    #              (3, 9)
    for i in range(k, len(arr)):
        
        sub_arr.append(arr[i-k+1 : i+1] )
        
    return sub_arr

arr = [5, 3, 2, 1, 3, 3, 7, 2, 2] # 9
k = 4
print("Original Array: ",arr)
print(window_arr1(arr, k))
print(window_arr2(arr, k))
