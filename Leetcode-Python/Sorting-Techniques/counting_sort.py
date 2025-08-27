def counting_sort(arr: list):
    n = len(arr)
    # Get the max ele 
    maxx = max(arr)
    
    # based on that create an empty count list
    counts = [0] * (maxx + 1)
    
    for x in arr:
        counts[x] += 1
    
    print(f"Count from 0 - maxx {maxx}")
    print("c:",counts)

    i = 0
    for c in range(maxx + 1):
        while counts[c] > 0:
            arr[i] = c
            i += 1
            counts[c] -= 1

arr = [5, 3, 2, 1, 3, 3, 7, 2, 2]
counting_sort(arr)
print(arr)