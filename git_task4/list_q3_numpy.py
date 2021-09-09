#3 Дано матрицю N на M. Вивести транспоновану матрицю.


import numpy as np


def input_matrix():
    """Entering a matrix from the keyboard and return numpy 2-d array"""
    try:
        rows = int(input("Enter the number of rows   : "))
        columns = int(input("Enter the number of columns: "))

        input_list = list()
        for row in range(rows):
            for col in range(columns):
                print(f"enter item {col + 1} in row {row + 1}: ", end='')
                item = int(input())
                input_list.append(item)
        matrix = np.array(input_list).reshape(rows, columns)
        return matrix

    except ValueError as err:
        print(err)


def transpose_matrix(matrix):
    """Creating transpose matrix"""

    t_matrix = matrix.transpose()
    return t_matrix


A = input_matrix()
print("Input matrix: ")
print(A)

T = transpose_matrix(A)
print("Transpose matrix:")
print(T)


#test2
A1 = np.array([[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9]])

test_M1 = np.array([[1, 4, 7],
                    [2, 5, 8],
                    [3, 6, 9]])

assert ((transpose_matrix(A1) == test_M1).all())

B1 = np.array([[1, 2, 3],
               [4, 5, 6]])

test_M2 = np.array([[1, 4],
                    [2, 5],
                    [3, 6]])

assert ((transpose_matrix(B1) == test_M2).all())
