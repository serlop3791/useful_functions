from quick_sort_implementations import implementation_one as one
from quick_sort_implementations import implementation_two as two
from quick_sort_implementations import implementation_three as three
from quick_sort_implementations import implementation_four as four
from quick_sort_implementations import implementation_five as five


# def _quicksort(arr):
#     return quick_sort(arr, 0, len(arr) - 1)
# def quick_sort(arr, left, right):
#     if left < right:
#         Find the position of pivot
# pivot_final_resting_position = partition(arr, left, right)
# Recursively call left and right subarray to the pivot
# quick_sort(arr, left, pivot_final_resting_position - 1)
# quick_sort(arr, pivot_final_resting_position + 1, right)
# return arr
# Helper function to perform the partition
# def partition(arr, left, right):
# Here we make the right most element as pivot
# middle = (left + right) // 2
# pivot = arr[middle]
# We re-arrange the array such that
# The elements smaller than the pivot are at left to the pivot
# And The elements greater than the pivot are at right to the pivot
# i = left - 1
# for j in range(left, right):
#     if arr[j] <= pivot:
#         i += 1
# swap(arr, i, j)
# The pivot comes to its correct position
# swap(arr, i + 1, right)
# Return the pivot's final resting position
# return i + 1
# Helper function to swap elements at 2 different array indices
# def swap(arr, first, second):
#     arr[first], arr[second] = arr[second], arr[first]
#
# def quicksort(nums):
#     return quicksort(nums)

# def quick_sort(arr, begin, end):
#     if begin < end:
#         partition_index = partition(arr, begin, end)
#         quick_sort(arr, begin, partition_index - 1)
#         quick_sort(arr, partition_index + 1, end)
#
# def partition(arr, begin, end):
#     pivot = arr[begin]
#     pivot_index = begin


# return two.quick_sort(0, len(nums)-1, nums)
# return one.quick_sort(nums)
# return two.quick_sort(0, len(nums) - 1, nums)
# return three.quick_sort(nums, 0, len(nums)-1)
# return four.quick_sort(nums)
# return five.quick_sort(0, len(nums)-1, nums)

def _quicksort(nums):
    return quick_sort(nums, 0, len(nums) - 1)


<<<<<<< Updated upstream
def quick_sort(arr, left, right):
    if left < right:
        pivot_index = partition(arr, left, right)
        quick_sort(arr, left, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, right)
    return arr
=======
def partition(arr, begin, end):
    pivot = arr[begin]
    pivot_index = begin
    return 0
>>>>>>> Stashed changes


def partition(arr, left, right):
    pivot = arr[right]
    partition_frontier = left - 1
    for j in range(left, right):
        if arr[j] < pivot:
            partition_frontier = partition_frontier + 1
            arr[j], arr[partition_frontier] = arr[partition_frontier], arr[j]
    arr[partition_frontier + 1], arr[right] = arr[right], arr[partition_frontier + 1]
    return partition_frontier + 1




# def quick_sort(arr, left, right):
#     if left < right:
#         partition_index = partition(arr, left, right)
#         quick_sort(arr, left, partition_index - 1)
#         quick_sort(arr, partition_index + 1, right)
#     return arr
#
#
# def partition(arr, left, right):
#     pivot = arr[right]
#     partition_frontier = left - 1
#     for j in range(left, right):
#         if arr[j] < pivot:
#             partition_frontier = partition_frontier + 1
#             arr[partition_frontier], arr[j] = arr[j], arr[partition_frontier]
#     arr[partition_frontier + 1], arr[right] = arr[right], arr[partition_frontier + 1]
#     return partition_frontier + 1
