#10 Дано число N і список з N чисел. Вивести список у зворотному порядку.

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


def revers_list(list_numbers):
    """Returns the list in reverse order"""
    return list_numbers[ : :-1]


numbers = input_list()
print("Entered list")
print(numbers)
print("Revers list")
print(revers_list(numbers))


#test
test_l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
assert (revers_list(test_l) == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
