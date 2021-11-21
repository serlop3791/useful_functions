# Find the midpoint of the list (the number located in the middle of the list).
# Use floor division, we want an integer to use it as an index. We do not want a float.
# midpoint_index = len(sorted_numbers) // 2


# List of length 0, 1, 2, 3, 4, 5
one_list = [1]
one_midpoint_index = len(one_list) // 2
print("list of length 1 midpoint index " + str(one_midpoint_index)) # This is 0
two_list = [1, 2]
two_midpoint_index = len(two_list) // 2
print("list of length 2 midpoint index " + str(two_midpoint_index)) # This is 1
three_list = [1, 2, 3]
three_midpoint_index = len(three_list) // 2
print("list of length 3 midpoint index " + str(three_midpoint_index)) # This is 1
four_list = [1, 2, 3, 4]
four_midpoint_index = len(four_list) // 2
print("list of length 4 midpoint index " + str(four_midpoint_index)) # This is 2
five_list = [1, 2, 3, 4, 5]
five_midpoint_index = len(five_list) // 2
print("list of length 5 midpoint index " + str(five_midpoint_index)) # This is 2
six_list = [1, 2, 3, 4, 5, 6]
six_midpoint_index = len(six_list) // 2
print("list of length 6 midpoint index " + str(six_midpoint_index)) # This is 3
