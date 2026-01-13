def rtst(arr, k):
    length = len(arr)
    k = k % length
    temp = arr[:k]
    for i in range(k, length):
        arr[i - k] = arr[i ]

arr = [1, 2, 3, 4, 5, 6]
