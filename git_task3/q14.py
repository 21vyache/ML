#14 Реалізуйте CRM систему, яка повинна приймати й обробляти запити наступних видів:
#a. Додати працівника з іменем <name> у систему. add<name>
#b. Перевірити чи є працівник з іменем <name> у системі.find <name>
#c. Вивести список всіх працівників.list
#d. Видалити працівника з іменем <name> із системи.delete <name>
#e. Завершити роботу системи.stop stop


def add(name, employees_list):
    """Add an employee with (name) to the system"""
    employees_list.append(name)
    return employees_list


def find(name, employees_list):
    """Check if the employee with (name) is in the system"""
    if name in employees_list:
        return True


def list(employees_list):
    """Output a list of all employees"""
    if len(employees_list):
        for i in range(len(employees_list)):
            print(f"{i+1} - {employees_list[i]}")
    else:
        print("No employee")

def delete(name, employees_list):
    """Remove an employee with (name) from the system"""
    if name in employees_list:
        employees_list.remove(name)
    else:
        print(f"Employee {name} not in the system")
    return employees_list


def menu():
    """Display a list of commands"""
    print("add <name>    - Add an employee with (name) to the system")
    print("find <name>   - Check if the employee with (name) is in the system")
    print("list          - Output a list of all employees")
    print("delete <name> - Remove an employee with (name) from the system")
    print("stop          - Stop working in the system")


def input_command():
    """Entering and checking user commands"""
    command_list = ["add", "find", "list", "delete", "stop"]
    while True:
        command = input(">>>")
        if command in command_list:
            return command
        else:
            print("Incorrect command")


def crm():
    """Simple CRM system"""
    employees = []
    command = None
    menu()
    while True:
        command = input_command()
        if command == "add":
            name = input()
            employees = add(name, employees)

        elif command == "find":
            name = input()
            if find(name, employees):
                print(f"Employee {name} in the system")
            else:
                print(f"Employee {name} not in the system")

        elif command == "list":
            list(employees)

        elif command == "delete":
            name = input()
            employees = delete(name, employees)

        elif command == "stop":
            break


crm()

#test
test_employees = ["Lewis", "Valtteri"]
assert (find("Lewis", test_employees) == True)
assert (add("Niko", test_employees) == ["Lewis", "Valtteri", "Niko"])
assert (delete("Niko", test_employees) == ["Lewis", "Valtteri"])
