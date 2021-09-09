"""You are given a table, in which every key is a stringified number,
and each corresponding value is an array of characters, e.g.
{  "1": ["A", "B", "C"],
   "2": ["A", "B", "D", "A"],}

Create a function that returns a table with the same keys,
but each character should appear only once among the value-arrays, e.g.
{  "1": ["C"],
   "2": ["A", "B", "D"],}

Rules
Whenever two keys share the same character, they should be compared numerically,
and the larger key will keep that character.
That's why in the example above the array under the key "2" contains "A" and "B", as 2 > 1.
If duplicate characters are found in the same array, the first occurance should be kept."""


def dictionary_dif_val(dictionary):
    """Different dictionary values"""

    # Creating a list of keys, sorted from greater to lesser by their numerical value
    list_keys_str = list(dictionary.keys())             # Extracting dictionary keys
    list_keys_int = [int(key) for key in list_keys_str] # Convert keys to a numeric value
    list_keys_int.sort(reverse=True)
    list_keys_str = [str(key) for key in list_keys_int] # Convert keys to strings value

    out_dict = dict()
    total_value_buffer = list()         # List to store all unique values

    for key in list_keys_str:           # Cycle through a sorted list of keys
        local_value_buffer = list()     # List for storing unique values for each character array

        # Go through each array of characters, in descending order of the numerical value of the key
        for val in dictionary[key]:
            # Add values that have not previously occurred in the previous and current character array
            if (val not in local_value_buffer) and (val not in total_value_buffer):
                local_value_buffer.append(val)

        out_dict[key] = local_value_buffer
        # Add unique character values for this key to the total buffer
        total_value_buffer.extend(out_dict[key])

    return out_dict


# test 1
d0 = {"1": ["A", "B", "C"],
      "2": ["A", "B", "D", "A"]}

d0_output = {'1': ['C'],
             '2': ['A', 'B', 'D']}

assert (dictionary_dif_val(d0) == d0_output)

# test 2
d1 = {"1": ["C", "F", "G"],
      "2": ["A", "B", "C"],
      "3": ["A", "B", "D"]}

d1_output = {'1': ['F', 'G'],
             '2': ['C'],
             '3': ['A', 'B', 'D']}

assert (dictionary_dif_val(d1) == d1_output)

# test 3
d2 = {"1": ["A"],
      "2": ["A"],
      "3": ["A"]}

d2_output = {'1': [],
             '2': [],
             '3': ['A']}

assert (dictionary_dif_val(d2) == d2_output)

# test 4
d3 = {"432": ["A", "A", "B", "D"],
      "53": ["L", "G", "B", "C"],
      "236": ["L", "A", "X", "G", "H", "X"],
      "11": ["P", "R", "S", "D"]}

d3_output = {'432': ['A', 'B', 'D'],
             '53': ['C'],
             '236': ['L', 'X', 'G', 'H'],
             '11': ['P', 'R', 'S']}

assert (dictionary_dif_val(d3) == d3_output)

# test 5
print(d0)
print(dictionary_dif_val(d0))
print(d1)
print(dictionary_dif_val(d1))
print(d2)
print(dictionary_dif_val(d2))
print(d3)
print(dictionary_dif_val(d3))
