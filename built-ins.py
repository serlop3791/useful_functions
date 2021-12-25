# List built-ins
test_list = [1, 2, 3, 4, 5]


# Adds elements at end of list
def append():
    test_list.append(6)

# Removes all elements from the list
def clear():
    test_list.clear()

# Returns a copy of the list. This is a shallow copy. The slice syntax
# way of copying is also shallow.
def copy():
    copy_list = test_list.copy()

