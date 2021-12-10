def quick_sort(arr):
    return quick_sort_helper(arr, 0, len(arr) - 1)


def quick_sort_helper(arr, left, right):
    if left < right:
        pivot_final_resting_position = partition(arr, left, right)
        quick_sort_helper(arr, left, pivot_final_resting_position - 1)
        quick_sort_helper(arr, pivot_final_resting_position + 1, right)
    return arr


def partition(arr, left, right):
    pivot = arr[right]
    i = left - 1
    for j in range(left, right):
        if arr[j] <= pivot:
            i += 1
            swap(arr, i, j)
    swap(arr, i + 1, right)
    return i + 1


def swap(arr, first, second):
    temp = arr[first]
    arr[first] = arr[second]
    arr[second] = temp
