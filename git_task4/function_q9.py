#9-function Написати функцію, що отримує два відсортованих списки і об'єднує їх у новий відсортований список.


def sort_two_list(l_num1, l_num2):
    """Combines two sorted lists into one sorted list"""

    sort_list = list()
    # If the lists are sorted in descending order
    if l_num1[-1] < l_num1[0] or l_num2[-1] < l_num2[0]:
        sort_list = sorted(l_num1 + l_num2, reverse=True)
    # If the lists are sorted in ascending order
    else:
        sort_list = sorted(l_num1 + l_num2)
    return sort_list


# Test
list_numbers1 = [1, 2, 3, 4, 5]
list_numbers2 = [6, 7, 8, 9, 10]
#print(sort_two_list(list_numbers1, list_numbers2))
assert (sort_two_list(list_numbers1, list_numbers2) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

list_numbers3 = [10, 9, 8, 7, 6]
list_numbers4 = [5, 4, 3, 2, 1]
#print(sort_two_list(list_numbers3, list_numbers4))
assert (sort_two_list(list_numbers3, list_numbers4) == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
