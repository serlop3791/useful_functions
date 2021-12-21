
def insertion_sort(numbers):
    for i in range(1, len(numbers)):
        number_to_insert = numbers[i]
        j = i - 1
        while j >= 0 and number_to_insert < numbers[j]:
            numbers[j+1] = numbers[j]
            j = j - 1
        numbers[j + 1] = number_to_insert
    return numbers























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


# def insertion_sort(nums):
# Has sorted and unsorted virtual sections.
# Has a nested while loop that is traversing backwards
# from right to left and controlled by j - 1.
# The outermost loop start at position 1, not 0,
# because we compare with the previous item in list.
# It also has some weird shifting of numbers by one position
# to the right.
# for i in range(1, len(nums)):
#     number_to_insert = nums[i]
#     j = i - 1
#     while j >= 0 and number_to_insert < nums[j]:
#         nums[j + 1] = nums[j]
#         j = j - 1
#     nums[j + 1] = number_to_insert
# return nums

'''
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
'''


def xinsertion_sort(nums):
    for i in (range(1, len(nums))):
        number_to_insert = nums[i]
        j = i - 1
        while j >= 0 and number_to_insert < nums[j]:
            nums[j + 1] = nums[j]
            j = j - 1
        nums[j + 1] = number_to_insert
    return nums
