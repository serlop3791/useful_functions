def quick_sort(nums):
    elements = len(nums)
    # Base case
    if elements < 2:
        return nums
    # Position of the partitioning element
    # We are choosing leftmost element
    current_position = 0
    # Partitioning loop
    for i in range(1, elements):
        if nums[i] <= nums[0]:
            # Partitioning frontier expanded
            current_position += 1

            # Swapping
            # element at position i with element at current_position
            # Current position is used to delimit the partitioning frontier
            # i is used to traverse the partitioning section of the array
            temp = nums[i]
            nums[i] = nums[current_position]
            nums[current_position] = temp

    # Brings pivot to it's appropriate position
    temp = nums[0]
    nums[0] = nums[current_position]
    nums[current_position] = temp

    # Sorts the elements to the left of pivot
    left = quick_sort(nums[0:current_position])
    # Sorts the elements to the right of pivot
    right = quick_sort(nums[current_position + 1:elements])

    # Merging everything together
    arr = left + [nums[current_position]] + right

    return arr



