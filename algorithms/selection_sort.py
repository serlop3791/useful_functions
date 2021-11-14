import random


def get_random_nums(size):
    return [random.randint(0, 10) for num in range(size)]


def selection_sort(nums):
    # has sorted and unsorted sections like insertionsort
    # searches the unsorted section to find the next min (or max) number to insert
    # it doesn't have shifting like insert sort
    # we keep track of the min num index and update it when we have found a smaller number
    # we perform a swap after we have finished search for the next min (or max) number
    for i in range(len(nums)):
        min_num_index = i
        for j in range(i + 1, len(nums)):
            if nums[min_num_index] > nums[j]:
                min_num_index = j
        nums[i], nums[min_num_index] = nums[min_num_index], nums[i]
    return nums


def my_sort(nums):
    return selection_sort(nums)


def test_code():
    unsorted_list = get_random_nums(10)
    print('original unsorted list: ' + str(unsorted_list))
    sorted_list = sorted(unsorted_list)
    print('sorted list: ' + str(sorted_list))
    my_sorted_list = my_sort(unsorted_list)
    print('my sorted list: ' + str(my_sorted_list))
    assert sorted_list == my_sorted_list


test_code()
