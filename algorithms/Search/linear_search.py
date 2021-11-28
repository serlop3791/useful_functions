def linear_search(numbers, number_to_find):
	for i in range(len(numbers)):
		if numbers[i] == number_to_find:
			return i
	return -1
