#4 Знайти сторону квадрата по його площі.

def square_side(area):
    """Determining the side of a square by its area"""
    if area > 0:
        return area ** 0.5


try:
    area = float(input("Enter the area of the square: "))
    side = square_side(area)
    print(f"The side of the square is {side}")

except ValueError as err:
    print(err)


#test
assert (square_side(25) == 5)