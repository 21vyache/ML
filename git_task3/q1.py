#1 Написати програму, яка зчитує число,
# виводить його квадратний корінь і приймає наступне число.
# Програма повинна припинити роботу коли їй буде введено від’ємне число.

def square_root(number):
    """Calculating the square root"""
    return number**0.5


try:
    while True:
        number = int(input("Enter a number (negative to exit): "))
        if number >= 0:
            print(f"The square root of {number} is {square_root(number)}")
        else:
            break
except ValueError as err:
    print(err)


#test
assert (square_root(9) == 3)
assert (square_root(25) == 5)
