"""#15 Write a function that accepts two square (N x N) matrices (two dimensional arrays),
and returns the product ot the two. Only square matrices will be given.

How to multiply two square matrices:
We are given two matrices, A and B, of size 2 x 2
(note: tests are not limited to 2 x 2).
Matrix C, the solution, will be equal to the product of A and B. To fill in cell [0][0] of matrix C,
you need to compute: A[0][0] * B[0][0] + A[0][1] * B[1][0].

More general: To fill in cell [n][m] of matrix C,
you need to first multiply the elements in the nth row of matrix A
by the elements in the mth column of matrix B, then take the sum of all those products.
This will give you the value for cell [m][n] in matrix C."""


def input_matrix():
    """Entering a matrix from the keyboard"""
    try:
        dimension = int(input("Enter the matrix dimension: "))
        matrix = list(list() for x in range(dimension))
        for row in range(dimension):
            for col in range(dimension):
                print(f"enter item {col + 1} in row {row + 1}: ", end='')
                item = int(input())
                matrix[row].append(item)
        return matrix

    except ValueError as err:
        print(err)


def print_matrix(matrix):
    """Matrix output on the screen"""

    # Number of lines/columns is equal to the number of list items (for square matrices)
    dimension = len(matrix)
    for i in range(dimension):
        for j in range(dimension):
            print(matrix[i][j], end='\t')
        print()
    print()


def multiply_matrix(A, B):
    """Multiplication of two square matrices A and B"""

    # Number of lines/columns is equal to the number of list items (for square matrices)
    dimension = len(A)
    C = list(list() for x in range(dimension))

    for row in range(dimension):         # rows of the resulting matrix
        for col in range(dimension):     # columns of the resulting matrix
            sum = 0
            for k in range(dimension):
                sum += A[row][k] * B[k][col]
            C[row].append(sum)
    return C


print("Enter matrix M1")
M1 = input_matrix()
print_matrix(M1)
print("Enter matrix M2")
M2 = input_matrix()
print_matrix(M2)
print("Multiply matrix M1xM2")
M = multiply_matrix(M1, M2)
print_matrix(M)


#test
A = [[1, 2],
     [3, 4]]

B = [[5, 6],
     [7, 8]]

assert (multiply_matrix(A, B) == [[19, 22],
                                  [43, 50]])

A1 = [[1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]]

B1 = [[10, 11, 12],
      [13, 14, 15],
      [16, 17, 18]]

assert (multiply_matrix(A1, B1) == [[84, 90, 96],
                                    [201, 216, 231],
                                    [318, 342, 366]])
