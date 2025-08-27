# # O(n·k)
def window_arr1(arr:list, k:int):
    sum_ele = []
    i  = 0
    while k <= len(arr):
        sum_ele.append(arr[i:k])
        i  += 1
        k += 1
    return sum_ele

# Better Sliding Window
def window_arr2(arr: list, k:int):
    sub_arr = []
    
    # Base Case
    if len(arr) < k:
        return
    
    slice_wind = arr[:k]
    sub_arr.append(slice_wind)
    
    for i in range(k, len(arr)):
        
        slice_wind = arr[i-k+1 : i+1] 
        
        sub_arr.append(slice_wind)
        
    return sub_arr

arr = [5, 3, 2, 1, 3, 3, 7, 2, 2] # 9
k = 3
print(arr)
print(window_arr1(arr, k))
print(window_arr2(arr, k))
