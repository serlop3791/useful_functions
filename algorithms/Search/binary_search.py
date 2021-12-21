






























def binary_search(numbers, target):
	left = 0
	right = len(numbers) - 1
	while left <= right:
		mid = (left + right) // 2
		if numbers[mid] == target:
			return mid
		elif numbers[mid] > target:
			right = mid - 1
		else:
			left = mid + 1
	return -1





#     right = len(numbers) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if target == numbers[mid]:
#             return mid
#         elif target < numbers[mid]:
#             right = mid - 1
#         else:
#             left = mid + 1
#     return -1


# def binary_search(numbers, number_to_find):
# 	# Sort the list if it is not already sorted.
# 	# This is a critical step(!) as the rest of the algorithm
# 	# assumes the list is ordered.
# 	# numbers.sort()
# 	sorted_numbers = sorted(numbers)
# 	# Aside: It is possible to achieve an in-place (This means no additional memory required)
# 	# sort in O(nlogn) (This is considered a fast time) time, using quicksort.
# 	# print(len(sorted_numbers))
# 	# print(sorted_numbers)
# 	# Find the midpoint of the list (the number located in the middle of the list).
# 	# Use floor division, we want an integer to use it as an index. We do not want a float.
# 	midpoint_index = len(sorted_numbers) // 2
# 	# print("midpoint_index: " + str(midpoint_index))
# 	midpoint_number = sorted_numbers[midpoint_index]
# 	# print("midpoint_number: " + str(midpoint_number))
# 	# We repeat the following steps, each time on a smaller list:
# 	# calculate new midpoint value, compare against midpoint,
# 	# midpoint will either be less than, equal to, or greater than the number
# 	# we are searching for.
# 	# If midpoint is equal to the number we are searching for, we are done.
# 	# If the midpoint is greater than or less than, we repeat the process
# 	# on either the left half or right half .
# 	# Each time we compare against a midpoint we have effectively reduced the
# 	# size of the list in half.
# 	while len(sorted_numbers) > 0:
# 		# If the number you are searching for is equal to the midpoint, you
# 		# have found the number and can return with its position, value or boolean.
# 		if number_to_find == midpoint_number:
# 			return midpoint_number
# 		elif number_to_find < midpoint_number:
# 			# If the number you are searching for is less than the midpoint,
# 			# search the left half of the list.
# 			# You may ignore the right half of the list.
# 			# As the list is sorted, the elements to the right of
# 			# the midpoint can only be greater and can be safely ignored.
# 			sorted_numbers = sorted_numbers[0:midpoint_index]
# 			midpoint_index = len(sorted_numbers) // 2
# 			midpoint_number = sorted_numbers[midpoint_index]
# 		elif number_to_find > midpoint_number:
# 			# If the number you are searching for is greater than the midpoint,
# 			# search the right half of the list.
# 			# You may ignore the left half of the list.
# 			# As the list is sorted, the elements to the left of
# 			# the midpoint can only be smaller and can be safely ignored.
# 			sorted_numbers = sorted_numbers[midpoint_index+1:len(sorted_numbers)]
# 			midpoint_index = len(sorted_numbers) // 2
# 			midpoint_number = sorted_numbers[midpoint_index]
# 	# We return None to signal that the number was not found in the list
# 	return None

# number must be sorted
# def binary_search(numbers, target):
#     left = 0
#     right = len(numbers) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if target == numbers[mid]:
#             return mid
#         elif target < numbers[mid]:
#             right = mid - 1
#         else:
#             left = mid + 1
#     return -1


def binary_search_recursive(numbers, target, left, right):
	if left > right:
		return -1
	mid_index = (left + right) // 2
	if target == numbers[mid_index]:
		return mid_index
	elif target < numbers[mid_index]:
		return binary_search_recursive(numbers, target, left, mid_index - 1)
	else:
		return binary_search_recursive(numbers, target, mid_index + 1, right)
