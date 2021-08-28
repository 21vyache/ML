#4 Дано число N. Вивести перші N чисел Фібоначчі.

def fibonacci(number):
    """Calculating Fibonacci number.
    F(n) = F(n-1) + F(n-2) with F(0) = 0 and F(1) = 1"""

    n_1 = 0
    n_2 = 1
    fib = None
    if number >= 0: # Only for positive numbers
        if number == 0:
            fib = 0
        elif number == 1:
            fib = 1
        else:
            for i in range(1, number):
                fib = n_1 + n_2
                n_1 = n_2
                n_2 = fib
        return fib


try:
    count = int(input("Enter the count of Fibonacci numbers: "))
    for i in range(count):
        print(f"{i + 1}\t F{i}={fibonacci(i)}")

except ValueError as err:
    print(err)


#test
assert (fibonacci(0) == 0)
assert (fibonacci(1) == 1)
assert (fibonacci(9) == 34)
