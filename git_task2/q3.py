#3 Дано число. Вивести попереднє й наступне відносного нього.

def next_number(num):
    """Return the next number"""
    return num + 1


def previous_number(num):
    """Return the previous number"""
    return num - 1


try:
    num = int(input("Enter a number: "))
    print(f"The next number for the number {num} is {next_number(num)}")
    print(f"The previous number for the number {num} is {previous_number(num)}")

except ValueError as err:
    print(err)


#test
assert(next_number(179) == 180 and previous_number(179) == 178)