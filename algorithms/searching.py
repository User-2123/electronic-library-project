def linear_search(arr, target, key=lambda x: x):
    for index, item in enumerate(arr):
        if key(item) == target:
            return index
    return -1

def binary_search(arr, target, key=lambda x: x):
    # Предполагается, что arr отсортирован
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_val = key(arr[mid])

        if mid_val == target:
            return mid
        elif mid_val < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1