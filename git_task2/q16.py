"""16 A comfortable word is a word which can type always alternating the hand you type with
(asuming you type using a QWERTY keyboard and fingers as shown in the image below).
That being said, create a function which receives a word and returns true/True
if it's a comfortable word and false/False otherwise.
The word will alvays be a string consisting of only ascii letters from a to z.
To avoid problevs with image availability, here's the lists of lettets for each hand:
Left: q, w, e, r, t, a, s, d, f, g, z, x, c, v, b
Right: y, u, i, o, p, h, j, k, l, n, m"""

def is_comfortable(word):
    """Checking comfortable word"""
    right = ['y', 'u', 'i', 'o', 'p', 'h', 'j', 'k', 'l', 'n', 'm']
    previous = False
    current = False
    l_word = word.lower()

    if l_word[0] in right:
        previous = True

    for i in range(1, len(l_word)):
        if l_word[i] in right:
            current = True
        else:
            current = False

        if previous == current:
            return False
        else:
            previous = current
    return True


try:
    word = input("Enter the word: ")
    if word.isalpha() and len(word) >= 2:
        if is_comfortable(word):
            print(f"Word {word} is comfortable")
        else:
            print(f"Word {word} is not comfortable")
    else:
        print("Incorrect data")

except ValueError as err:
    print(err)


#testing
assert (is_comfortable("yams") == True)
assert (is_comfortable("test") == False)