#3 Дано знак “+” або “*”, число N і N чисел.
# Вивести суму або добуток введених чисел залежно від заданого знаку.

def adding(numbers):
    """Returns the sum of the entered numbers"""
    sum = 0
    for num in numbers:
        sum += num
    return sum


def multiplication(numbers):
    """Returns the product of the entered numbers"""
    mul = 1
    for num in numbers:
        mul *= num
    return mul


try:
    operator = input("Enter the operation (+ or *): ")
    count = int(input("Enter the number of numbers: "))

    numbers = []
    for i in range(count):
        num = float(input(f"enter number {i + 1} of {count}: "))
        numbers.append(num)

    if operator == '+':
        print(f"The sum of the elements is {adding(numbers)}")
    elif operator == '*':
        print(f"The product of the elements is {multiplication(numbers)}")
    else:
        print("Unknown operator")

except ValueError as err:
    print(err)


#test
testing_numbers = [1, 2, 3, 4, 5]
assert (adding(testing_numbers) == 15)
assert (multiplication(testing_numbers) == 120)
