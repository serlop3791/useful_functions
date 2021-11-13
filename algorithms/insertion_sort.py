import random


def get_random_nums(size):
    return [random.randint(0, 10) for num in range(size)]


unsorted_list = get_random_nums(10)
print(unsorted_list)
sorted_list = sorted(unsorted_list)
print(sorted_list)
print(unsorted_list)
