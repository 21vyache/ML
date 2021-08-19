#5 Задано 3 сторони -трикутника. Знайти його периметр і площу.

def is_triangle(a, b, c):
    """Checking the existence of a triangle"""
    if a + b > c and a + c > b and b + c > a:
        return True


def triangle_perimeter(side_a, side_b, side_c):
    """Calculating the perimeter of a triangle"""
    return side_a + side_b + side_c


def triangle_area(side_a, side_b, side_c):
    """Calculating the area of a triangle using the Heron formula"""
    #s is the semi-perimeter
    s = triangle_perimeter(side_a, side_b, side_c) / 2
    t_area = (s*(s - side_a)*(s - side_b)*(s - side_c)) ** 0.5
    return t_area


try:
    print("Enter the sides of the triangle")
    a = float(input("side a: "))
    b = float(input("side b: "))
    c = float(input("side c: "))

    if is_triangle(a, b, c):
        perimeter = triangle_perimeter(a, b, c)
        print(f"The perimeter of the triangle is {perimeter}")

        area = triangle_area(a, b, c)
        print(f"The area of the triangle is {area}")
    else:
        print("It's not a triangle.")

except ValueError as err:
    print(err)


#test
assert (triangle_perimeter(3, 4, 5) == 12 and triangle_area(3, 4, 5) == 6)
assert (triangle_perimeter(8, 15, 17) == 40 and triangle_area(8, 15, 17) == 60)
assert (is_triangle(3, 4, 5))