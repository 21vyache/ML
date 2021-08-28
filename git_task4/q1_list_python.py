#1 Дано число N і M. Далі вводяться N рядків по M чисел.
# Вивести M чисел, що відповідають значенням сум відповідних стовпчиків.


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


def sum_columns_matrix(matrix):
    """Matrix column summation"""

    rows = len(matrix)          # Number of rows is equal to the number of list items
    columns = len(matrix[0])    # Number of columns is equal to the number items in list items
    sum_list = list()

    for col in range(columns):
        sum = 0
        for row in range(rows):
            sum += matrix[row][col]
        sum_list.append(sum)
    return sum_list


A = input_matrix()
print_matrix(A)
S = sum_columns_matrix(A)
print(S)


#test
A1 = [[1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]]

assert (sum_columns_matrix(A1) == [12, 15, 18])

B1 = [[1, 2, 3],
      [4, 5, 6]]

assert (sum_columns_matrix(B1) == [5, 7, 9])