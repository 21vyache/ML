#Реалізуйте ще один простий калькулятор, що отримує два числа
# й операцію і виводить результат виконання операції над введеними значеннями.
# Допустимі операції: + - * /

def calc(num1, num2, opp):
    """Simple calc"""
    if opp == '+':
        return num1 + num2
    elif opp == '-':
        return num1 - num2
    elif opp == '*':
        return num1 * num2
    elif opp == '/':
        if num2 != 0:
            return num1 / num2
    else:
        return False


try:
    num1 = float(input("Enter number 1: "))
    num2 = float(input("Enter number 2: "))
    opp = input("Enter operator (+,-,*,/): ")
    result = calc(num1, num2, opp)
    print(f"{num1} {opp} {num2} = {result}")

except ValueError as err:
    print(err)


#test
assert (calc(10, 2, '+') == 12 and calc(10, 2, '-') == 8 and
        calc(10, 2, '*') == 20 and calc(10, 2, '/') == 5)