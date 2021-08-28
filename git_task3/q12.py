#12 Дано число N і список з N чисел. Вивести всі числа, що зустрічаються у списку лише раз.

def input_list():
    """Returns the entered list of items"""
    try:
        count = int(input("Enter the number of elements: "))
        numbers = list()
        for i in range(count):
            num = float(input(f"Enter number {i+1} of {count}: "))
            numbers.append(num)
        return numbers
    except ValueError as err:
        print(err)


def single_values(list_numbers):
    """Returns numbers that occur only once in the list"""

    single = list()
    for i in list_numbers:
        if list_numbers.count(i) == 1:
            single.append(i)
    return single


numbers = input_list()
print("Entered list:\n", numbers)
print("Numbers that occur only once in the list:\n", single_values(numbers))


#test
test_l = [1, 1, 3, 5, 5, 7, 8, 8, 9, 10]
assert (single_values(test_l) == [3, 7, 9, 10])
