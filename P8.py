def selector_sort_ascending(arr):
    length = len(arr)
    for i in range(length):
        for j in range( i + 1, length):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

    return arr

def selector_sort_descending(arr):
    length = len(arr)
    for i in range(length):
        for j in range( i + 1, length):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

    return arr

arr = list(map(int, input("Enter array elements (space-separated): ").split()))
print(selector_sort_ascending(arr))
print(selector_sort_descending(arr))