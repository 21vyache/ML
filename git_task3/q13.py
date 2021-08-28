#13 Дано число N, список з N чисел, число M і далі список з M чисел.
# Вивести всі числа, які трапляються в обох списках.

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


def total_number(list1, list2):
    """Returns the total numbers in the two lists"""
    total = list()
    for num in list1:
        if num in list2:
            total.append(num)
    return total


print("List 1")
numbers1 = input_list()
print("List 2")
numbers2 = input_list()
print("Entered list 1:\n", numbers1)
print("Entered list 2:\n", numbers2)
print("Total numbers in the two lists:\n", total_number(numbers1, numbers2))


#test
test_l_1 = [1, 2, 3, 4, 5]
test_l_2 = [6, 3, 5, 7, 8]
assert (total_number(test_l_1, test_l_2) == [3, 5])
