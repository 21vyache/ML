#10 Реалізувати функцію sign(x).

def sign(number):
    """Returns a number that indicates the sign of x:
     -1 if x is negative; 0 if x equals 0; or 1 if x is positive"""
    if number > 0:
        return 1
    elif number < 0:
        return -1
    else:
        return 0


try:
    number = float(input("Enter a number: "))
    print(f"Sign function {number} is {sign(number)}")

except ValueError as err:
    print(err)


#testing
assert (sign(-10) == -1 and sign(10) == 1 and sign(0) == 0)