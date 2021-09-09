#2 Дано число N. Створити й вивести двовимірний масив розмірністю N на N,
# у якого на основній діагоналі розташовані одиниці, а всі інші значення дорівнюють нулю.

import numpy as np


def identity_matrix(dimension):
    """Creating identity matrix and return numpy 2-d array"""

    i_matrix = np.identity(dimension)
    return i_matrix


try:
    dimension = int(input("Enter the matrix dimension: "))
    A = identity_matrix(dimension)
    print(A)

except ValueError as err:
    print(err)


#test

test_M1 = np.array([[1, 0],
                    [0, 1]])

assert ((identity_matrix(2) == test_M1).all())

test_M2 = np.array([[1, 0, 0],
                    [0, 1, 0],
                    [0, 0, 1]])

assert ((identity_matrix(3) == test_M2).all())
