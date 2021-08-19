#Дано коефіцієнти a, b, c квадратного рівняння ax^2+bx+c=0.
# Знайти корені рівняння.

import cmath
import math


def quadratic_equation(a, b, c):
    """Finding roots of a quadratic equation"""

    root1 = None
    root2 = None
    # Calculation discriminant: b^2 - 4ac
    d = b**2 - 4 * a * c

    if d == 0:
        root1 = -b / (2 * a)
    else:
        if d > 0:
            root_d = math.sqrt(d)
        else: #root is complex number
            root_d = cmath.sqrt(d)
        root1 = (-b + root_d) / (2 * a)
        root2 = (-b - root_d) / (2 * a)
    return root1, root2


try:
    a = float(input("coefficient a: "))
    b = float(input("coefficient b: "))
    c = float(input("coefficient c: "))

    if a != 0:
        print(f"{a}x2 + {b}x + {c} = 0")
        x1, x2 = quadratic_equation(a, b, c)
        print(f"x1 = {x1} and x2 = {x2}")
    else:
        print("Incorrect data")

except ValueError as err:
    print(err)


#test
assert (quadratic_equation(-4, 28, -49) == (3.5, None))
assert (quadratic_equation(1, -2, -3) == (3, -1))