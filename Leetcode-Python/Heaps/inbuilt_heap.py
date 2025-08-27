import heapq

arr = [-4, 3 ,1, 0, 2, 5, 10, 8, 12, 9]

# Min Heap
heapq.heapify(arr)

# get the min value => the root node
print(heapq.heappop(arr))


def heap_sort(arr):
    
    heapq.heapify(arr)
    n = len(arr)
    new_arr = [0] * n
    
    for i in range(n):
        min_val = heapq.heappop(arr)
        new_arr[i] = min_val
        
    return new_arr

print(heap_sort(arr))