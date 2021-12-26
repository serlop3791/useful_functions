from sort_fixture import get_random_nums, get_random_number


def merge_lists(list_one, list_two):
    index_one = 0
    index_two = 0
    while index_one < len(list_one) and index_two < len(list_two):
        if list_one[index_one] > list_two[index_two]:
            list_one.insert(index_one, list_two[index_two])
            index_one += 1
            index_two += 1
        else:
            index_one += 1
    if index_two < len(list_two):
        list_one.extend(list_two[index_two:])
    return list_one


def test_merge_lists():
    list_a = sorted(get_random_nums(get_random_number()))
    print("list_a: " + str(list_a))
    list_b = sorted(get_random_nums(get_random_number()))
    print("list_b: " + str(list_b))
    expected_sorted_list = sorted(list_a[:] + list_b[:])
    sorted_list = merge_lists(list_a, list_b)
    print("expected: " + str(expected_sorted_list))
    print("actual: " + str(sorted_list))
    assert expected_sorted_list == sorted_list


test_merge_lists()
