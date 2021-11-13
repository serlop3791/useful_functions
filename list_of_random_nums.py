import random


# def get_random_nums(size):
#     nums = []
#     i = 0
#     while i < size:
#         nums.append(random.randint(0, 10))
#         i += 1
#     return nums

# def get_random_nums(size):
#     nums = []
#     for i in range(size):
#         nums.append(random.randint(0, 10))
#     return nums

def get_random_nums(size):
    return [random.randint(0, 10) for num in range(size)]
