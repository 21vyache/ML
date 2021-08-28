#2 Дано число N - кількість чисел до вводу та самі числа.
# Вивести максимум серед введених чисел.

def check_max(num1, num2):
    """True, if num1 is greater than num2"""
    return num1 > num2


try:
    count = int(input("Enter the number of numbers to find the maximum among them: "))
    max = None
    for i in range(count):
        num = float(input(f"enter number {i+1} of {count}: "))
        if i == 0:
            max = num
        elif check_max(num, max):
            max = num
    print(f"Max number is {max}")

except ValueError as err:
    print(err)


#test
assert (check_max(5, -5) == True)
assert (check_max(0, 10) == False)
