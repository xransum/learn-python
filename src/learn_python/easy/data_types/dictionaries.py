"""Dictionary"""

fruits_dictionary = {
    'cherry': 'red',
    'apple': 'green',
    'banana': 'yellow',
}

isinstance(fruits_dictionary, dict)

# You may access set elements by keys.
fruits_dictionary['apple'] == 'green'
fruits_dictionary['banana'] == 'yellow'
fruits_dictionary['cherry'] == 'red'

# To check whether a single key is in the dictionary, use the in keyword.
'apple' in fruits_dictionary
'pineapple' not in fruits_dictionary

# Change the apple color to "red".
fruits_dictionary['apple'] = 'red'

# Add new key/value pair to the dictionary
fruits_dictionary['pineapple'] = 'yellow'
fruits_dictionary['pineapple'] == 'yellow'

# Performing list(d) on a dictionary returns a list of all the keys used in the dictionary,
# in insertion order (if you want it sorted, just use sorted(d) instead).
list(fruits_dictionary) == ['cherry', 'apple', 'banana', 'pineapple']
sorted(fruits_dictionary) == ['apple', 'banana', 'cherry', 'pineapple']

# It is also possible to delete a key:value pair with del.
del fruits_dictionary['pineapple']
list(fruits_dictionary) == ['cherry', 'apple', 'banana']

# The dict() constructor builds dictionaries directly from sequences of key-value pairs.
dictionary_via_constructor = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])

dictionary_via_constructor['sape'] == 4139
dictionary_via_constructor['guido'] == 4127
dictionary_via_constructor['jack'] == 4098

# In addition, dict comprehensions can be used to create dictionaries from arbitrary key
# and value expressions:
dictionary_via_expression = {x: x**2 for x in (2, 4, 6)}
dictionary_via_expression[2] == 4
dictionary_via_expression[4] == 16
dictionary_via_expression[6] == 36

# When the keys are simple strings, it is sometimes easier to specify pairs using
# keyword arguments.
dictionary_for_string_keys = dict(sape=4139, guido=4127, jack=4098)
dictionary_for_string_keys['sape'] == 4139
dictionary_for_string_keys['guido'] == 4127
dictionary_for_string_keys['jack'] == 4098

