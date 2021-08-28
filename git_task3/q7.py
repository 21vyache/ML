#7 Дано число N.
# Після чого в порядку обходу вводяться N пар координат многокутника на площині.
# Знайти периметр цього многокутника.

def side_length(x1, y1, x2, y2):
    """Calculating the lengths of the sides by the Pythagoras formula"""
    length = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
    return length


try:
    vertices = int(input("Enter the number of vertices of the polygon: "))
    if vertices >= 3:
        perimeter = 0
        #Variables for storing initial and previous pairs of coordinates
        x_initial = x_previous = 0
        y_initial = y_previous = 0
        for i in range(vertices):
            print(f"x coordinate of the vertex {i + 1}: ", end='')
            x_current = float(input())
            print(f"y coordinate of the vertex {i + 1}: ", end='')
            y_current = float(input())

            if i == 0: #In the first step keep the initial coordinates
                x_initial = x_previous = x_current
                y_initial = y_previous = y_current

            elif i == vertices - 1:
                perimeter += side_length(x_current, y_current, x_previous, y_previous)
                #Calculating the length of the closing side and add to var. perimeter
                perimeter += side_length(x_current, y_current, x_initial, y_initial)

            else:
                perimeter += side_length(x_current, y_current, x_previous, y_previous)
                x_previous = x_current
                y_previous = y_current
        print(f"The perimeter of a polygon is equal to {perimeter}")

    else:
        print("Incorrect input.")

except ValueError as err:
    print(err)


#test
x_begin = 0
y_begin = 3
x_end = 4
y_end = 0
assert (side_length(x_begin, y_begin, x_end, y_end) == 5)
