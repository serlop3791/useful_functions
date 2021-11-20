import random


def get_random_nums(size):
    return [random.randint(0, 10) for num in range(size)]


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
def bubble_sort(nums):
    # has_swap = False
    for i in range(0, len(nums) - 1):
        has_swap = False
        for j in range(0, len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                has_swap = True
        if not has_swap:
            return nums
    return nums


def my_sort(nums):
    return bubble_sort(nums)


def test_sort():
    unsorted_list = get_random_nums(5)
    print('original unsorted list: ' + str(unsorted_list))
    sorted_list = sorted(unsorted_list)
    print('sorted list: ' + str(sorted_list))
    my_sorted_list = my_sort(unsorted_list)
    print('my sorted list: ' + str(my_sorted_list))
    assert sorted_list == my_sorted_list


test_sort()
