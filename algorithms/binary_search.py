import random


class Setup:
	def __init__(self, number_to_search_for):
		self.random_nums = []
		self.range_start = 0
		self.range_end = 10
		self.size = 20
		self.number_to_insert = number_to_search_for
		self.set_random_nums()
	
	def set_random_nums(self):
		nums = [random.randint(self.range_start, self.range_end) for _ in range(self.size)]
		# Remove any existing instances of the number we are searching for.
		# This is to make sure there is only a single instance of the number
		# we are searching for in our list.
		# If we are searching for the number 5 and
		# our list has multiple 5s how can we know our algorithm is correct?
		filtered_nums = list(filter(lambda num: num != self.number_to_insert, nums))
		filtered_nums.append(self.number_to_insert)
		# We randomize the numbers again as we just inserted the number we are searching for
		# to the end of the list.
		random.shuffle(filtered_nums)
		self.random_nums = filtered_nums

	def get_numbers(self):
		return self.random_nums


def binary_search(numbers, number_to_find):
	# Sort the list if it is not already sorted.
	# This is a critical step(!) as the rest of the algorithm
	# assumes the list is ordered.
	# numbers.sort()
	sorted_numbers = sorted(numbers)
	# Aside: It is possible to achieve an in-place (This means no additional memory required)
	# sort in O(nlogn) (This is considered a fast time) time, using quicksort.
	# print(len(sorted_numbers))
	# print(sorted_numbers)
	# Find the midpoint of the list (the number located in the middle of the list).
	# Use floor division, we want an integer to use it as an index. We do not want a float.
	midpoint_index = len(sorted_numbers) // 2
	# print("midpoint_index: " + str(midpoint_index))
	midpoint_number = sorted_numbers[midpoint_index]
	# print("midpoint_number: " + str(midpoint_number))
	# We repeat the following steps, each time on a smaller list:
	# calculate new midpoint value, compare against midpoint,
	# midpoint will either be less than, equal to, or greater than the number
	# we are searching for.
	# If midpoint is equal to the number we are searching for, we are done.
	# If the midpoint is greater than or less than, we repeat the process
	# on either the left half or right half .
	# Each time we compare against a midpoint we have effectively reduced the
	# size of the list in half.
	while len(sorted_numbers) > 0:
		# If the number you are searching for is equal to the midpoint, you
		# have found the number and can return with its position, value or boolean.
		if number_to_find == midpoint_number:
			return midpoint_number
		elif number_to_find < midpoint_number:
			# If the number you are searching for is less than the midpoint,
			# search the left half of the list.
			# You may ignore the right half of the list.
			# As the list is sorted, the elements to the right of
			# the midpoint can only be greater and can be safely ignored.
			sorted_numbers = sorted_numbers[0:midpoint_index]
			midpoint_index = len(sorted_numbers) // 2
			midpoint_number = sorted_numbers[midpoint_index]
		elif number_to_find > midpoint_number:
			# If the number you are searching for is greater than the midpoint,
			# search the right half of the list.
			# You may ignore the left half of the list.
			# As the list is sorted, the elements to the left of
			# the midpoint can only be smaller and can be safely ignored.
			sorted_numbers = sorted_numbers[midpoint_index+1:len(sorted_numbers)]
			midpoint_index = len(sorted_numbers) // 2
			midpoint_number = sorted_numbers[midpoint_index]
	# We return None to signal that the number was not found in the list
	return None

def test():
	number_to_search_for = random.randint(0, 5)
	setup = Setup(number_to_search_for)
	numbers = setup.get_numbers()
	print("Searching for number: " + str(number_to_search_for))
	print("In this list: " + str(numbers))
	number = binary_search(numbers, number_to_search_for)
	if number is not None and number != -1 and number == number_to_search_for:
		print("Found number: " + str(number))
	else:
		print("Number not found.")

test()
