#8 Дано число N і список з N чисел.
# Для кожного числа зі списку вивести його відношення до середнього арифметичного цього списку
# (менше, дорівнює, більше).


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


def arithmetic_mean(list_numbers):
    """Calculation of the arithmetic mean: sum of a collection of numbers
    divided by the count of numbers in the collection"""
    count = len(list_numbers)
    sum = 0
    for i in range(count):
        sum += list_numbers[i]
    return sum / count


numbers = input_list()
mean = arithmetic_mean(numbers)
print("Numbers  Relation  Ar. mean")
for i in range(len(numbers)):
    if numbers[i] == mean:
        print(f"{numbers[i]} \t\t = \t\t {mean}")
    elif numbers[i] > mean:
        print(f"{numbers[i]} \t\t > \t\t {mean}")
    elif numbers[i] < mean:
        print(f"{numbers[i]} \t\t < \t\t {mean}")


#test
assert (arithmetic_mean([1, 2, 3]) == 2)
