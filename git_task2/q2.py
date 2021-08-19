#2 Задано 3 числа. Вивести їх суму.

def sum_of_three_numbers(num1, num2, num3):
    """Calculating the sum of three numbers"""
    return num1 + num2 + num3


try:
    print("Enter three numbers.")
    num1 = float(input("number 1: "))
    num2 = float(input("number 2: "))
    num3 = float(input("number 3: "))
    total_sum = sum_of_three_numbers(num1, num2, num3)
    print(f"Sum of three numbers is {total_sum}.")

except ValueError as err:
    print(err)


#test
assert (sum_of_three_numbers(10, 20, 30) == 60)