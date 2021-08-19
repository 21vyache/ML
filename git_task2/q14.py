#14 Дано одну літеру. Визначити чи є вона голосною або приголосною

def check_is_vowels(letter):
    # Vowels a e i o u (-y)
    l = letter.lower()
    if l == 'a' or l == 'e' or l == 'i' or l == 'o' or l == 'u':
        return True


letter = input("enter one letter(en): ")
if letter.isalpha() and len(letter) == 1:
    if check_is_vowels(letter):
        print(f"Letter -{letter}- is vowels")
    else:
        print(f"Letter -{letter}- is consonants")
else:
    print("Invalid input")


#test
assert (check_is_vowels('a'))
assert (not(check_is_vowels('b')))
