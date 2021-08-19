#1 Користувач вводить ім’я. Привітайтесь з ним по імені й зі знаком оклику в кінці.

def hello_func(name):
    """Simple greeting function"""
    return f"Hello, {name}!"


name = input("Enter your name: ")
print(hello_func(name))


#test
assert (hello_func("Python") == "Hello, Python!")