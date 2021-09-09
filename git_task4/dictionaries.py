"""Dictionaries Телефонний довідник.
Напишіть програму, що буде реалізовувати простий телефонний довідник.
При запуску програми довідник порожній.

Далі у користувача повинна бути можливість інтерактивно виконувати наступні операції, вводячи їх з клавіатури:
- insert <Name> <Number> - додати в телефонний довідник новий запис про користувача і його номер телефону.
- delete <Name> - видалити з телефонного довідника користувача і його номер телефону.
- get <Name> - дізнатися номер телефону по імені користувача.

<Name> - рядок із символів англійського алфавіту в верхньому або нижньому регістрі без роздільників.
<Number> - рядок з цифр.

Імена не повторюються. Кожному імені може відповідати рівно один номер телефону.
Зберігати дані між запусками програми не потрібно.
"""


def insert(name, number, phone_dict):
    """Add a user phone"""
    phone_dict[name] = number
    return phone_dict


def get(name, phone_dict):
    """Find out the user's phone number"""
    if name in phone_dict:
        return name, phone_dict[name]


def list(phone_dict):
    """List of users' phones"""
    if len(phone_dict):
        for key, value in phone_dict.items():
            print(f"{key} - {value}")
    else:
        print("No users' phones")


def delete(name, phone_dict):
    """Delete a name"""
    if name in phone_dict:
        del phone_dict[name]
    else:
        print(f"Name {name} not in the system")
    return phone_dict


def menu():
    """Display a list of commands"""
    print("insert <name> <number> - Add a user phone                ")
    print("get    <name>          - Find out the user's phone number")
    print("list                   - List of users' phones           ")
    print("delete <name>          - Delete a user                   ")
    print("stop                   - Stop working in the system      ")


def input_command():
    """Entering and checking user commands"""
    command_list = ["insert", "get", "list", "delete", "stop"]
    while True:
        command = input(">>>")
        if command in command_list:
            return command
        else:
            print("Incorrect command")


def phone_book():
    """Simple phone book system"""
    phone_dict = dict()
    menu()
    while True:
        command = input_command()
        if command == "insert":
            answer_string_list = input().split()
            if len(answer_string_list) == 2:

                # Determine the sequence of name and number
                name = number = None
                if answer_string_list[0].isalpha() and answer_string_list[1].isnumeric():
                    name = answer_string_list[0]
                    number = answer_string_list[1]
                elif answer_string_list[0].isnumeric() and answer_string_list[1].isalpha():
                    name = answer_string_list[1]
                    number = answer_string_list[0]

                insert(name, number, phone_dict)
            else:
                print("Incorrect name or number")

        elif command == "get":
            name = input()
            answer = get(name, phone_dict)
            if answer:
                print(f"User {answer[0]} - {answer[1]}")
            else:
                print(f"User {name} not in the system")

        elif command == "list":
            list(phone_dict)

        elif command == "delete":
            name = input()
            phone_dict = delete(name, phone_dict)

        elif command == "stop":
            break


phone_book()

# Test
test_phone_dict = {"lando": 1111, "daniel": 2222, "zack": 3333}

assert (get("zack", test_phone_dict) == ("zack", 3333))
assert (insert("ron", 4444, test_phone_dict) ==
        {"lando": 1111, "daniel": 2222, "zack": 3333, "ron": 4444})
assert (delete("ron", test_phone_dict) ==
        {"lando": 1111, "daniel": 2222, "zack": 3333})
