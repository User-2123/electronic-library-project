def bubble_sort(arr, key=lambda x: x):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if key(arr[j]) > key(arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def quick_sort(arr, key=lambda x: x):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        pivot_val = key(pivot)
        
        left = [x for x in arr if key(x) < pivot_val]
        middle = [x for x in arr if key(x) == pivot_val]
        right = [x for x in arr if key(x) > pivot_val]
        
        return quick_sort(left, key) + middle + quick_sort(right, key)