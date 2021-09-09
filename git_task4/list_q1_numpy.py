#1 Дано число N і M. Далі вводяться N рядків по M чисел.
# Вивести M чисел, що відповідають значенням сум відповідних стовпчиків.


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


def sum_columns_matrix(matrix):
    """Matrix column summation and return numpy 2-d array"""

    column_sums = matrix.sum(axis=0)
    return column_sums


A = input_matrix()
print(A)
S = sum_columns_matrix(A)
print(S)


#test
A1 = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

assert ((sum_columns_matrix(A1) == np.array([12, 15, 18])).all())

B1 = np.array([[1, 2, 3],
               [4, 5, 6]])

assert ((sum_columns_matrix(B1) == np.array([5, 7, 9])).all())
