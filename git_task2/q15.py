#15 Дано довжини трьох сторін трикутника.
#   Визначити чи є трикутник рівностороннім або рівнобедреним.

def is_triangle(a, b, c):
    """Checking the existence of a triangle"""
    if a + b > c and a + c > b and b + c > a:
        return True


def is_equilateral_triangle(a, b, c):
    """True if the triangle is equilateral"""
    if a == b == c:
        return True


def is_isosceles_triangle(a, b, c):
    """True if the triangle is isosceles"""
    if a == b or a == c or b == c:
        return True


try:
    print("Enter the sides of the triangle")
    a = float(input("side a: "))
    b = float(input("side b: "))
    c = float(input("side c: "))

    if is_triangle(a, b, c):
        if is_equilateral_triangle(a, b, c):
            print("Equilateral triangle")
        elif is_isosceles_triangle(a, b, c):
            print("Isosceles triangle")
        else:
            print("Another type of triangle")
    else:
        print("It's not a triangle.")

except ValueError as err:
    print(err)


#test
assert (is_triangle(3, 4, 5))
assert (is_equilateral_triangle(5, 5, 5))
assert (is_isosceles_triangle(5, 5, 9))