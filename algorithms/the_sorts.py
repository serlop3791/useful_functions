import random


def get_random_nums(size):
    return [random.randint(0, 10) for num in range(size)]


def selection_sort(nums):
    # has unsorted and sorted virtual sections
    # searches unsorted section for next min number
    # adds selected element to sorted section
    for i in range(len(nums)):
        min_index = i
        for j in range(i + 1, len(nums)):
            if nums[min_index] > nums[j]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]
    return nums


def bubble_sort(nums):
    # two nested for loops
    # the inner loop swaps adjacent numbers
    # can break early using flag if array is already sorted
    has_swap = False
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] > nums[j]:
                has_swap = True
                nums[i], nums[j] = nums[j], nums[i]
        if not has_swap:
            return nums
    return nums


def insertion_sort(nums):
    # Has sorted and unsorted virtual sections.
    # Has a nested while loop that is traversing backwards
    # from right to left and controlled by j - 1.
    # The outermost loop start at position 1, not 0,
    # because we compare with the previous item in list.
    # It also has some weird shifting of numbers by one position
    # to the right.
    for i in range(1, len(nums)):
        number_to_insert = nums[i]
        j = i - 1
        while j >= 0 and number_to_insert < nums[j]:
            nums[j + 1] = nums[j]
            j = j - 1
        nums[j + 1] = number_to_insert
    return nums


def my_sort(nums):
    return bubble_sort(nums)


def test_code():
    unsorted_list = get_random_nums(10)
    print('original unsorted list: ' + str(unsorted_list))
    sorted_list = sorted(unsorted_list)
    print('sorted list: ' + str(sorted_list))
    my_sorted_list = my_sort(sorted_list)
    print('my sorted list: ' + str(my_sorted_list))
    assert sorted_list == my_sorted_list


test_code()
