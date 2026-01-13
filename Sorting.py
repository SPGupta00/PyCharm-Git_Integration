# Selection Sort #

'''def Selection(arr):
    length = len(arr)
    for i in range (length):
        for j in range (i + 1, length):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                
    return arr
print(Selection)

arr = list(map(int, input().split()))'''


# Bubble Sort #
'''
def bubble_sort(arr):
    length = len(arr)
    for i in range (length):
        j = 1
        while (j > 0 and arr[j - 1] > arr[j]):
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1
arr = [4, 6, 8 ,1 , 4, 9]
print(bubble_sort(arr))'''


# arr = [1, 4, 0,0, 5, 6, 0, 7]
# for i in range(len(arr)):
#     if arr[i] == 0:
#         j = i
#         for j in range(j+1, len(arr)):
#             if arr[i] != 0:
#                 arr[i], arr[j] = arr[j], arr[i]
#                 j += 1
#     return arr


'''def largest(arr):
    largest = 0
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    return True
    


print(largest([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))'''

#   Merge Sort   #

# def merge_sort(arr, low, high):
#     if low >= high:
#         return

#     mid = (low + high) // 2
#     merge_sort(arr, low, mid)
#     merge_sort(arr, mid + 1, high)
#     Sort(arr, low, mid, high)


# def Sort(arr, low, mid, high):
#     temp = []
#     left = low
#     right = mid + 1

#     while left <= mid and right <= high:
#         if arr[left] <= arr[right]:
#             temp.append(arr[left])
#             left += 1
#         else:
#             temp.append(arr[right])
#             right += 1

#     while left <= mid:
#         temp.append(arr[left])
#         left += 1

#     while right <= high:
#         temp.append(arr[right])
#         right += 1

#     for i in range(len(temp)):
#         arr[low + i] = temp[i]
#     return arr

# arr = list(map(int, input().split()))
# merge_sort(arr, 0, len(arr) - 1)
# print(arr)


# def merge_sort(arr, low, high):
#     if low >= high:
#         return
#     mid = (low + high) // 2
#     merge_sort(arr, low, mid)
#     merge_sort(arr, mid + 1, high)
#     sort(arr, low, mid, high)

# def sort(arr, low, mid, high):
#     temp = []
#     left = low
#     right = mid + 1
#     while (left <= mid and right <= high):
#         if arr[left] <= arr[right]:
#             temp.append(arr[left])
#             left += 1
#         else:
#             temp.append(arr[right])
#             right += 1
#     while (left <= mid):
#         temp.append(arr[left])
#         left += 1
#     while (right <= high):
#         temp.append(arr[right])
#         right += 1
#     for i in range(low, high + 1):
#         arr[i] = temp[i - low]
#     return arr

# arr = [1, 3, 4, 5, 9, 2, 4, 7, 3]
# low = 0
# high = len(arr) - 1
# merge_sort(arr, low, high)
# print(arr)


#   Quick Sort   #

def quick_sort(arr, low, high):
    if low < high:
        position = sort(arr, low, high)
        quick_sort(arr, low, position - 1)
        quick_sort(arr, position + 1, high)

def sort(arr, low, high):
    pivot = arr[low]
    i = low
    j = high
    while( i < j):
        while(arr[i] <= pivot and i < high):
            i += 1
        while(arr[j] > pivot and j > low):
            j -= 1
        if( i < j):
            arr[i], arr[j] = arr[j], arr[i]
    arr[low], arr[j] = arr[j], arr[low]
    return j

arr = list(map(int, input("Enter array elements separated by space: ").split()))
quick_sort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)