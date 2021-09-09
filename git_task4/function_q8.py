#8-function Написати функцію, яка використовує функції із попереднього завдання,
# і для заданого кола повертає відформатований рядок з його описом.
#   Enter radius of the circle: 10
#       Diameter of the circle = 20.00 units
#       Circumference of the circle = 62.83 units
#       Area of the circle = 314.16 sq. units


from function_q7 import *


def parameters_circle(circle_radius):
    """Calculation of circle parameters: Diameter, Circumference, Area"""
    print(f"Diameter of the circle      = {circle_diameter(circle_radius)} units")
    print(f"Circumference of the circle = {circumference(circle_radius):.2f} units")
    print(f"Area of the circle          = {circle_area(circle_radius):.2f} sq.units")


#test
test_radius = 10
parameters_circle(test_radius)
