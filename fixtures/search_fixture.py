import random


class Utility:
    def __init__(self, range_start, range_end, size, number_to_search_for):
        self.random_nums = []
        self.range_start = range_start
        self.range_end = range_end
        self.size = size
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

    def get_random_numbers(self):
        return self.random_nums
