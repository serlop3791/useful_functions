import random


def get_random_nums(size):
    upper_range = random.randint(5, 1000)
    return [random.randint(0, upper_range) for _ in range(size)]


def get_random_number():
    return random.randint(0, 10)
