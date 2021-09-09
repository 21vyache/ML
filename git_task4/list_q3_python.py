#3 Дано матрицю N на M. Вивести транспоновану матрицю.


def input_matrix():
    """Entering a matrix from the keyboard"""
    try:
        rows = int(input("Enter the number of rows   : "))
        columns = int(input("Enter the number of columns: "))

        matrix = list(list() for x in range(rows))
        for row in range(rows):
            for col in range(columns):
                print(f"enter item {col + 1} in row {row + 1}: ", end='')
                item = int(input())
                matrix[row].append(item)
        return matrix

    except ValueError as err:
        print(err)


def print_matrix(matrix):
    """Matrix output on the screen"""

    rows = len(matrix)          # Number of rows is equal to the number of list items
    columns = len(matrix[0])    # Number of columns is equal to the number items in list items

    for row in range(rows):
        for col in range(columns):
            print(matrix[row][col], end='\t')
        print()
    print()


def transpose_matrix(matrix):
    """Creating transpose matrix"""

    rows = len(matrix)        # Number of rows is equal to the number of list items
    columns = len(matrix[0])  # Number of columns is equal to the number items in list items

    transpose = list(list() for i in range(columns))
    for row in range(rows):
        for col in range(columns):
            transpose[col].append(matrix[row][col])

    return transpose


A = input_matrix()
print("Input matrix: ")
print_matrix(A)

T = transpose_matrix(A)
print("Transpose matrix:")
print_matrix(T)


#test2
A1 = [[1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]]

assert (transpose_matrix(A1) == [[1, 4, 7],
                                 [2, 5, 8],
                                 [3, 6, 9]])

B1 = [[1, 2, 3],
      [4, 5, 6]]

assert (transpose_matrix(B1) == [[1, 4],
                                 [2, 5],
                                 [3, 6]])
