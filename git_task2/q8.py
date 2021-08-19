#Дано два числа, що задають інтервал.
#Згенерувати й вивести два випадкових числа у вказаному інтервалі -- ціле й раціональне.

from random import randint, uniform

try:
    begin = int(input("Enter the beginning of the interval: "))
    end = int(input("Enter the end of the interval:"))

    print(f"Random integer: {randint(begin, end)}")
    print(f"Random float: {uniform(begin, end)}")
except ValueError as err:
    print(err)

