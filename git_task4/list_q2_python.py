#2 Дано число N. Створити й вивести двовимірний масив розмірністю N на N,
# у якого на основній діагоналі розташовані одиниці, а всі інші значення дорівнюють нулю.


def identity_matrix(dimension):
    """Creating identity matrix"""

    rows = dimension
    columns = dimension
    matrix = [[0] * columns for i in range(rows)]
    for row in range(rows):
        for col in range(columns):
            if row == col:
                matrix[row][col] = 1
    return matrix


def print_matrix(matrix):
    """Matrix output on the screen"""

    rows = len(matrix)          # Number of rows is equal to the number of list items
    columns = len(matrix[0])    # Number of columns is equal to the number items in list items

    for row in range(rows):
        for col in range(columns):
            print(matrix[row][col], end='\t')
        print()
    print()


try:
    dimension = int(input("Enter the matrix dimension: "))
    A = identity_matrix(dimension)
    print_matrix(A)

except ValueError as err:
    print(err)


#test
assert (identity_matrix(2) == [[1, 0],
                               [0, 1]])

assert (identity_matrix(3) == [[1, 0, 0],
                               [0, 1, 0],
                               [0, 0, 1]])
