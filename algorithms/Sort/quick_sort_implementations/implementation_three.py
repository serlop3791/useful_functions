def quick_sort(arr, low, high):
    if low < high:
        # get partitioning index
        # arr[partition_index] is at the right place
        partition_index = partition(arr, low, high)
        # call merge sort on left and right
        # left
        quick_sort(arr, low, partition_index - 1)
        # right
        quick_sort(arr, partition_index + 1, high)
    return arr


# This function takes last element as pivot, places
# the pivot element at its correct position in sorted
# array, and places all smaller (smaller than pivot)
# to left of pivot and all greater elements to right
# of pivot
def partition(arr, low, high):
    # last element is selected as pivot
    pivot = arr[high]
    # index of smaller element
    # to keep track of the partitioning frontier
    # There are 3 cases encountered here.
    # 1.
    # if an element encountered is smaller than our pivot,
    # the element is moved to the left of our partitioning frontier
    # to do that we expand our frontier.
    # 2.
    # if an element encountered is greater than our pivot,
    # the element is moved to the right of our partitioning
    # frontier. We don't expand our frontier, we continue
    # the traversal of the unsorted section within the
    # partitioning section.
    # 3.
    # if an element encountered is smaller than our pivot, but
    # the element encountered is not adjacent to the partitioning
    # frontier, we must swap the element encountered with the element that
    # is immediately to the right of the partitioning frontier. The element
    # adjacent to the partitioning frontier is one we have visited before
    # and is guaranteed to be greater than our pivot so the swapping is okay.
    # After we swap, we are in the clear to expand our partitioning frontier.
    # So we expand it to bring the new element to the left of the frontier.
    i = low - 1

    for j in range(low, high):
        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:
            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    # final swap
    # move the pivot to its appropriate location
    # the appropriate location is the position just before the
    # frontier
    # the pivot element is guaranteed to be sorted.
    # it is the only element in the array guaranteed to be at
    # its final position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    # the value returned is the pivot index aka the partition index
    # as seen by line above, it is the final sorted position of the pivot
    return i + 1
