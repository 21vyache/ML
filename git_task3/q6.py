#6 """Написати програму, що будує таблицю відповідності між градусами за Цельсієм і Фаренгейтом.
# Дано початкове значення у градусах Цельсія, кінцеве значення і крок.
# Вивести таблицю відповідностей."""

def celsius_to_fahrenheit(t_celsius):
    """Temperature conversion from degrees Celsius to degrees Fahrenheit
    Tf = 9*Tc/5 + 32"""

    t_fahrenheit = (9 * t_celsius / 5) + 32
    return t_fahrenheit


try:
    print("Build a correspondence table between degrees Celsius and Fahringeit.")
    initial = int(input("Enter the initial value in degrees Celsius : "))
    final = int(input("Enter the final value in degrees Celsius   : "))
    step = int(input("Enter construction step                    :"))
    for i in range(initial, final+1, step):
        print(f"{i}\u2103 \t {celsius_to_fahrenheit(i)}\u2109")

except ValueError as err:
    print(err)


#test
assert (celsius_to_fahrenheit(0) == 32)
assert (celsius_to_fahrenheit(25) == 77)
