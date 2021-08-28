#11 Дано число N і список з N чисел. Далі на вхід задаються пари чисел A,B>=0.
# Для кожної пари вивести значення списку з індексами від A включно до B не включно.
# Завершити роботу коли буде введено два нулі. Врахувати випадок коли A>B.

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


def slice_list(start, stop, list_numbers):
    """Returns the  slice list"""
    if start < stop:
        return list_numbers[start:stop:1]
    elif start > stop:
        return list_numbers[start:stop:-1]


numbers = input_list()
print("Entered list:\n", numbers)
try:
    while True:
        print("(Exit if A and B is 0)")
        A = int(input("Enter index A: "))
        B = int(input("Enter index B: "))
        if A == 0 and B == 0:
            break
        elif A <= len(numbers) and B <= len(numbers):
            print("Slice list:\n", slice_list(A, B, numbers))
        else:
            print("Out of range")

except ValueError as err:
    print(err)


#test
test_l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
assert (slice_list(0, 5, test_l) == [1, 2, 3, 4, 5])
assert (slice_list(10, 6, test_l) == [10, 9, 8])
