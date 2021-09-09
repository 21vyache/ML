#1-sets Написати програму, що для заданого списку чисел визначає скільки в ньому унікальних значень.

def count_unique_values(list_numbers):
    """Counting the number of unique values in a given list"""
    return len(set(list_numbers))


list_numbers = [6, 2, 8, 1, 1, 3, 1, 4, 8, 9]
print(f"In list: \n{list_numbers}\nunique values: {count_unique_values(list_numbers)}")


# Test
assert (count_unique_values(list_numbers) == 7)
