#4 Написати програму, що для заданого списку слів підрахує
# кількість входжень кожного зі слів у цей список.


def word_count(word_list):
    """Counting the number of repetitions of each word in the list,
     and returns the  key-word/value-count dictionary."""

    w_count = dict()
    for word in word_list:
        w_count[word] = word_list.count(word)
    return w_count


word_list = ['Python', 'consistently', 'ranks', 'as', 'one', 'of', 'the', 'most', 'popular', 'programming', 'languages']
print(word_count(word_list))

# Test
output_dict = {'Python': 1,
               'consistently': 1,
               'ranks': 1,
               'as': 1,
               'one': 1,
               'of': 1,
               'the': 1,
               'most': 1,
               'popular': 1,
               'programming': 1,
               'languages': 1}

assert (word_count(word_list) == output_dict)
