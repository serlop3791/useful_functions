



def bubble_sort(nums):
    is_sorted = True
    for i in range(0, len(nums) - 1):
        for j in range(0, len(nums) - i - 1):
            if nums[j] > nums[j+1]:
                is_sorted = False
                nums[j], nums[j+1] = nums[j+1], nums[j]
        if is_sorted:
            return nums
    return nums


















#
# def bubble_sort(nums):
#     # two nested for loops
#     # the inner loop swaps adjacent numbers
#     # can break early using flag if array is already sorted
#     has_swap = False
#     for i in range(len(nums)):
#         for j in range(i + 1, len(nums)):
#             if nums[i] > nums[j]:
#                 has_swap = True
#                 nums[i], nums[j] = nums[j], nums[i]
#         if not has_swap:
#             return nums
#     return nums
#


# def bubble_sort(arr):
#     n = len(arr)
#
#     # Traverse through all array elements
#     for i in range(n - 1):
#         # range(n) also work but outer loop will repeat one time more than needed.
#
#         # Last i elements are already in place
#         for j in range(0, n - i - 1):
#
#             # traverse the array from 0 to n-i-1
#             # Swap if the element found is greater
#             # than the next element
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#     return arr

# def bubble_sort(nums):
#     for i in range(0, len(nums) - 1):
#         for j in range(0, len(nums) - i - 1):
#             if nums[j] > nums[j + 1]:
#                 nums[j], nums[j + 1] = nums[j + 1], nums[j]
#     return nums

# Implement bubble_sort
'''
def bubble_sort(nums):
    has_swap = False
    for i in range(0, len(nums) - 1):
        # has_swap = False
        for j in range(0, len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                has_swap = True
        if not has_swap:
            return nums
    return nums
'''


def xbubble_sort(nums):
    is_sorted = True
    for i in range(0, len(nums) - 1):
        for j in range(0, len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                is_sorted = False
        if is_sorted:
            return nums
    return nums
