#7-function Написати набір функцій для розрахунку наступних характеристик кола:
# діаметр, довжина й площа. Коло задається радіусом.


from math import pi, pow


def circle_diameter(circle_radius):
    """Circle diameter D=2r"""
    return 2 * circle_radius


def circumference(circle_radius):
    """Circle circumference length C=2πr"""
    return 2 * pi * circle_radius


def circle_area(circle_radius):
    """Circle area A=πr2"""
    return pi * pow(circle_radius, 2)


#test
test_radius = 10
assert (circle_diameter(test_radius) == 20)
assert (circumference(test_radius) == 62.83185307179586)
assert (circle_area(test_radius) == 314.1592653589793)
