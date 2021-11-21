import random


class Setup:
	def __init__(self, number_to_search_for):
		self.random_nums = []
		self.range_start = 0
		self.range_end = 5
		self.size = 10
		self.number_to_insert = number_to_search_for
		self.set_random_nums()
	
	def set_random_nums(self):
		nums = [random.randint(self.range_start, self.range_end) for _ in range(self.size)]
		nums.append(self.number_to_insert)
		random.shuffle(nums)
		self.random_nums = nums
	
	def get_numbers(self):
		return self.random_nums


def linear_search(numbers, number_to_find):
	for i in range(0, len(numbers)):
		if numbers[i] == number_to_find:
			return i
	return -1


def test():
	number_to_search_for = random.randint(6, 20)
	setup = Setup(number_to_search_for)
	numbers = setup.get_numbers()
	print("Searching for:" + str(number_to_search_for))
	print("In this list:" + str(numbers))
	print("location at index:" + str(linear_search(numbers, number_to_search_for)))


test()
