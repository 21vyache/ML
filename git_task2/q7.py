#7 Реалізуйте простий калькулятор, що отримує два числа
# й виводить результати застосування стандартних математичних операцій над ними.

def adding(num1, num2):
    """Summing two numbers"""
    return num1 + num2


def subtraction(num1, num2):
    """Subtracting two numbers"""
    return num1 - num2


def multiplication(num1, num2):
    """Multiplying two numbers"""
    return num1 * num2


def division(num1, num2):
    """Division of two numbers"""
    if num2 != 0:
        return num1 / num2


try:
    num1 = float(input("Enter number 1: "))
    num2 = float(input("Enter number 2: "))
    print(f"{num1} + {num2} = {adding(num1, num2)}")
    print(f"{num1} - {num2} = {subtraction(num1, num2)}")
    print(f"{num1} * {num2} = {multiplication(num1, num2)}")
    print(f"{num1} / {num2} = {division(num1, num2)}")
except ValueError as err:
    print(err)


#testing
assert (adding(10, 2) == 12 and subtraction(10, 2) == 8
        and multiplication(10, 2) == 20 and division(10, 2) == 5)