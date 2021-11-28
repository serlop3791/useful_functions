#
# def selection_sort(nums):
#     # has unsorted and sorted virtual sections
#     # searches unsorted section for next min number
#     # adds selected element to sorted section
#     for i in range(len(nums)):
#         min_index = i
#         for j in range(i + 1, len(nums)):
#             if nums[min_index] > nums[j]:
#                 min_index = j
#         nums[i], nums[min_index] = nums[min_index], nums[i]
#     return nums
#


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
