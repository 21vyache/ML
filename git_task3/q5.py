#5 Дано число N. Вивести послідовність чисел Фібоначчі, що менші від N.

def fibonacci_lim(limit):
    """Calculating Fibonacci numbers to a given limit.
    F(n) = F(n-1) + F(n-2) with F(0) = 0 and F(1) = 1"""

    n_1 = 0
    n_2 = 1
    fib_num = 0
    fib_list = list()
    if limit > 0: # Only for positive numbers
        while True:
            fib_num = n_1
            n_1 = n_2
            n_2 = fib_num + n_2
            if fib_num < limit:
                fib_list.append(fib_num)
            else:
                break
    return fib_list


try:
    limit = int(input("Enter limit of Fibonacci numbers: "))
    print(fibonacci_lim(limit))

except ValueError as err:
    print(err)

# testing
assert (fibonacci_lim(10) == [0, 1, 1, 2, 3, 5, 8])
assert (fibonacci_lim(100) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89])
