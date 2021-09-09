#2 Написати програму, що інтерактивно отримує на ввід числа
# і для кожного повідомляє чи зустрічалося воно на вводі вже раніше.

def check_number(number, numbers):
    """Checks if there is a number in the given set"""
    if number in numbers:
        return True


try:
    numbers = set()
    while True:
        inp = input("enter number: ")
        if inp == "q":
            break
        elif not(inp.isalpha()):
            number = float(inp)
            if check_number(number, numbers):
                print(f"number {number} already been (q to exit)")
            else:
                print(f"number {number} is new       (q to exit)")
                numbers.add(number)

except ValueError as err:
        print(err)


# Test
set_test_numbers = {1, 2, 3, 4, 5}
assert (check_number(1, set_test_numbers) == True)
assert (not(check_number(7, set_test_numbers) == False))
