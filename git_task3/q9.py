#9 Дано число N і список з N чисел. Вивести всі числа, що більші від обох своїх сусідніх у списку.

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


def greater_both_adjacent(list_numbers):
    """Returns a list of numbers that are greater from both adjacent numbers in the list"""
    count = len(list_numbers)
    greater = list()

    for i in range(1, count - 1):   # skip the first and last element in the list
        if list_numbers[i] > list_numbers[i-1] and list_numbers[i] > list_numbers[i+1]:
            greater.append(list_numbers[i])
    return greater


numbers = input_list()
print("Entered list")
print(numbers)
print("List of numbers that are greater from both adjacent numbers in the list")
print(greater_both_adjacent(numbers))


#test
test_l = [1, 2, 3, 2, 1, 5, 0, 10]
assert (greater_both_adjacent(test_l) == [3, 5])
