def avg_of_list(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum/len(arr)

def avg_list(arr):
    s = sum(arr)
    l = len(arr)
    return s/l

arr = list(map(int, input("Enter array elements (space-separated): ").split()))
print(avg_of_list(arr))
print(avg_list(arr))