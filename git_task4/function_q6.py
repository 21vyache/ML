#6-function Написати функцію, яка отримує список натуральних чисел і повертає новий список,
# в якому містяться лише парні числа з початкового списку.


def even_list(numbers_list):
    """Finding and return even numbers"""
    even = list()
    for number in numbers_list:
        if number % 2 == 0:
            even.append(number)
    return even


#test
test_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
assert (even_list(test_list) == [0, 2, 4, 6, 8, 10])
