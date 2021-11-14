import random


def get_random_nums(size):
    return [random.randint(0, 10) for num in range(size)]


# def insertion_sort(nums):
#     for i in range(1, len(nums)):
#         number = nums[i]
#         j = i - 1
#         # print('i ' + str(i) + ' j ' + str(j) + ' nums: ' + str(nums))
#         while j >= 0 and number < nums[j]:
#             # print('comparing number: ' + str(number) + ' and nums[j]: ' + str(nums[j]))
#             nums[j + 1] = nums[j]
#             # print('shifting has occurred, number not yet inserted: ')
#             # print(nums)
#             j = j - 1
#         # print("progress... nums: " + str(nums))
#         # pos = j + 1
#         # print('Will insert number to position: ' + str(pos))
#         nums[j + 1] = number
#         # print('Number was inserted: ')
#         # print(nums)
#     return nums

def insertion_sort(nums):
    # sorted and unsorted sections
    # j - 1 controls inner while loop
    # first item is at position 1
    for i in range(1, len(nums)):
        num_to_insert = nums[i]
        j = i - 1
        while j >= 0 and num_to_insert < nums[j]:
            # shift numbers one position up to make room for the number to insert
            nums[j + 1] = nums[j]
            # update j, we are traversing from right to left and will need
            # to stop when we reach the beginning of the array
            j = j - 1
        # we have successfully shifted all numbers greater than num_to_insert
        # one position to the right but have not yet inserted num_to_insert
        # let us insert it now
        nums[j + 1] = num_to_insert
    return nums

def my_sort(nums):
    return insertion_sort(nums)


def test_code():
    unsorted_list = get_random_nums(10)
    print('original unsorted list: ' + str(unsorted_list))
    sorted_list = sorted(unsorted_list)
    print('sorted list: ' + str(sorted_list))
    my_sorted_list = my_sort(unsorted_list)
    print('my sorted list: ' + str(my_sorted_list))
    assert sorted_list == my_sorted_list


test_code()
