#9 Дано 2 числа. Вивести меньше з них.

def min_two_nums(num1, num2):
    """Finding the lesser of two"""
    if num1 <= num2:
        return num1
    else:
        return num2


try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    print(f"The lesser of the two numbers is {min_two_nums(num1, num2)}")

except ValueError as err:
    print(err)


#testing
assert (min_two_nums(-1, 1) == -1)
assert (min_two_nums(10, 3) == 3)