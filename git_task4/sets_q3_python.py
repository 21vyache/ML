#3 Написати програму, що дозволить підтримувати список електронних адрес для розсилки.
# Програма повинна дозволяти додавати, перевіряти наявність і видаляти електронні адреси.


def add(email, email_set):
    """Add e-mail address to the system"""
    email_set.add(email)
    return email_set


def find(email, email_set):
    """Check the e-mail address in the system"""
    if email in email_set:
        return True


def list(email_set):
    """Output e-mail addresses in the system"""
    if len(email_set):
        for count, value in enumerate(email_set):
            print(f"{count + 1} - {value}")
    else:
        print("No e-mails")


def delete(email, email_set):
    """Remove email address from the system"""
    if email in email_set:
        email_set.remove(email)
    else:
        print(f"E-mail {email} not in the system")
    return email_set


def menu():
    """Display a list of commands"""
    print("add    <e-mail> - Add e-mail address to the system      ")
    print("find   <e-mail> - Check the e-mail address in the system")
    print("list            - Output e-mail addresses in the system ")
    print("delete <e-mail> - Remove e-mail address from the system  ")
    print("stop            - Stop working in the system            ")


def input_command():
    """Entering and checking user commands"""
    command_list = ["add", "find", "list", "delete", "stop"]
    while True:
        command = input(">>>")
        if command in command_list:
            return command
        else:
            print("Incorrect command")


def email_newsletters():
    """Simple e-mail newsletters system"""
    email_set = set()
    menu()
    while True:
        command = input_command()
        if command == "add":
            email = input()
            add(email, email_set)

        elif command == "find":
            email = input()
            if find(email, email_set):
                print(f"E-mail {email} in the system")
            else:
                print(f"E-mail {email} not in the system")

        elif command == "list":
            list(email_set)

        elif command == "delete":
            email = input()
            email_set = delete(email, email_set)

        elif command == "stop":
            break


email_newsletters()


# Test
test_email_address = {"toto@gmail.com", "сhristian@gmail.com"}
assert (find("toto@gmail.com", test_email_address) == True)
assert (add("mattia@gmail.com", test_email_address) ==
        {"toto@gmail.com", "сhristian@gmail.com", "mattia@gmail.com"})
assert (delete("mattia@gmail.com", test_email_address) ==
        {"toto@gmail.com", "сhristian@gmail.com"})
