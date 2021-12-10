def quick_sort(start, end, array):
    if start < end:
        partition_index = partition(start, end, array)
        quick_sort(start, partition_index - 1, array)
        quick_sort(partition_index + 1, end, array)
    return array


def partition(start, end, array):
    # choosing the pivot and partitioning frontier
    # note - make sure to use start as the pivot
    # instead of end as the pivot.
    pivot = array[start]
    # the partitioning frontier starts at 0 and not -1
    i = 0
    # start index of traversing pointer is 1 instead of 0, the
    # pivot is at 0, range end is excluded but we want to consider
    # the last element too since our pivot is the leftmost element,
    # not the rightmost
    for j in range(1, end+1):
        if array[j] <= pivot:
            # sorting the section
            # updating the partitioning frontier
            # and swapping as needed
            i += 1
            array[i], array[j] = array[j], array[i]

    # updating the pivot's resting sorted location
    # and returning the final index of the pivot
    array[start], array[i] = array[i], array[start]
    return i


    # if start < end:
    #     pivot_final_resting_position = partition(start, end, array)
    #     quick_sort(start, pivot_final_resting_position - 1, array)
    #     quick_sort(pivot_final_resting_position + 1, end, array)
    # return array

# def partition(start, end, array):
# pivot = array[end]
# To keep track of the partitioning frontier
# i = start - 1
# for j in range(start, end):
#     if array[j] <= pivot:
# You gotta bump up your partitioning frontier
# i = i + 1
# You gotta swap the newly discovered element
# smaller than the pivot so that it falls to
# the left of the partitioning frontier
# array[i], array[j] = array[j], array[i]
# Final swap is performed to bring your pivot to its
# sorted position.
# array[i+1], array[end] = array[end], array[i+1]

# return i+1 not i, why?
# look at the line above, the final resting position of the pivot is
# i+1. The starting index of the pivot was end but now it is i+1
# The element at position i is the last element that falls within
# the partitioning frontier
# return i+1
