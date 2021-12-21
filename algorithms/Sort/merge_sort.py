# def merge_sort(arr):
#     if len(arr) > 1:
#
#         # Finding the mid of the array
#         mid = len(arr) // 2
#
#         # Dividing the array elements
#         L = arr[:mid]
#
#         # into 2 halves
#         R = arr[mid:]
#
#         # Sorting the first half
#         merge_sort(L)
#
#         # Sorting the second half
#         merge_sort(R)
#
#         i = j = k = 0
#
#         # Copy data to temp arrays L[] and R[]
#         while i < len(L) and j < len(R):
#             if L[i] < R[j]:
#                 arr[k] = L[i]
#                 i += 1
#             else:
#                 arr[k] = R[j]
#                 j += 1
#             k += 1
#
#         # Checking if any element was left
#         while i < len(L):
#             arr[k] = L[i]
#             i += 1
#             k += 1
#
#         while j < len(R):
#             arr[k] = R[j]
#             j += 1
#             k += 1
#     return arr

def merge_sort(numbers):
<<<<<<< Updated upstream
    if len(numbers) == 1:
        return numbers
    mid = len(numbers) // 2
    left_list = merge_sort(numbers[:mid])
    right_list = merge_sort(numbers[mid:])
    return merge(left_list, right_list)

def merge(left_list, right_list):
    sorted_list = []
    while len(left_list) > 0 and len(right_list) > 0:
        if left_list[0] > right_list[0]:
            sorted_list.append(right_list.pop(0))
        else:
            sorted_list.append(left_list.pop(0))
    if len(left_list) > 0:
        sorted_list += left_list
    if len(right_list) > 0:
        sorted_list += right_list
    return sorted_list
=======
	if len(numbers) == 1:
		return numbers
	mid = len(numbers) // 2
	left_list = merge_sort(numbers[:mid])
	right_list = merge_sort(numbers[mid:])
	return merge(left_list, right_list)

def merge(left_list, right_list):
	sorted_list = []
	while len(left_list) > 0 and len(right_list) > 0:
		if left_list[0] > right_list[0]:
			sorted_list.append(right_list[0])
			right_list.pop(0)
		else:
			sorted_list.append(left_list[0])
			left_list.pop(0)
	if len(left_list) > 0:
		sorted_list += left_list
	if len(right_list) > 0:
		sorted_list += right_list
	return sorted_list






















>>>>>>> Stashed changes


'''
def merge_sort(nums):
    if len(nums) == 1:
        return nums
    mid = len(nums) // 2
    left_list = merge_sort(nums[:mid])
    right_list = merge_sort(nums[mid:])
    return merge(left_list, right_list)


def merge(left_list, right_list):
    sorted_list = []
    # While there are elements in both lists
    while len(left_list) > 0 and len(right_list) > 0:
        if left_list[0] > right_list[0]:
            sorted_list.append(right_list[0])
            right_list.pop(0)
        else:
            sorted_list.append(left_list[0])
            left_list.pop(0)

    # One of the two lists may now be empty.
    # We don't know which so we shall code for both scenarios.
    # If both lists are empty we will simply return with
    # the new array.
    while len(left_list) > 0:
        sorted_list.append(left_list[0])
        left_list.pop(0)

    while len(right_list) > 0:
        sorted_list.append(right_list[0])
        right_list.pop(0)

    return sorted_list
<<<<<<< Updated upstream
'''
=======
'''
>>>>>>> Stashed changes
