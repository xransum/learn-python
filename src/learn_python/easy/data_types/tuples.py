
"""Tuples"""
fruits_tuple = ("apple", "banana", "cherry")

isinstance(fruits_tuple, tuple)
fruits_tuple[0] == "apple"
fruits_tuple[1] == "banana"
fruits_tuple[2] == "cherry"

# You cannot change values in a tuple.
try:
    # pylint: disable=unsupported-assignment-operation
    fruits_tuple[0] = "pineapple"
except Exception as err:
    print(err)

# It is also possible to use the tuple() constructor to make a tuple (note the double
# round-brackets).
# The len() function returns the length of the tuple.
fruits_tuple_via_constructor = tuple(("apple", "banana", "cherry"))

isinstance(fruits_tuple_via_constructor, tuple)
len(fruits_tuple_via_constructor) == 3

# It is also possible to omit brackets when initializing tuples.
another_tuple = 12345, 54321, 'hello!'
another_tuple == (12345, 54321, 'hello!')

# Tuples may be nested:
nested_tuple = another_tuple, (1, 2, 3, 4, 5)
nested_tuple == ((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))

# As you see, on output tuples are always enclosed in parentheses, so that nested tuples are
# interpreted correctly; they may be input with or without surrounding parentheses, although
# often parentheses are necessary anyway (if the tuple is part of a larger expression). It is
# not possible to assign to the individual items of a tuple, however it is possible to create
# tuples which contain mutable objects, such as lists.

# A special problem is the construction of tuples containing 0 or 1 items: the syntax has some
# extra quirks to accommodate these. Empty tuples are constructed by an empty pair of
# parentheses; a tuple with one item is constructed by following a value with a comma (it is
# not sufficient to enclose a single value in parentheses). Ugly, but effective. For example:
empty_tuple = ()
# pylint: disable=len-as-condition
len(empty_tuple) == 0

# pylint: disable=trailing-comma-tuple
singleton_tuple = 'hello',  # <-- note trailing comma
len(singleton_tuple) == 1
singleton_tuple == ('hello',)

# The following example is called tuple packing:
packed_tuple = 12345, 54321, 'hello!'

# The reverse operation is also possible.
first_tuple_number, second_tuple_number, third_tuple_string = packed_tuple
first_tuple_number == 12345
second_tuple_number == 54321
third_tuple_string == 'hello!'

# This is called, appropriately enough, sequence unpacking and works for any sequence on the
# right-hand side. Sequence unpacking requires that there are as many variables on the left
# side of the equals sign as there are elements in the sequence. Note that multiple assignment
# is really just a combination of tuple packing and sequence unpacking.

# Swapping using tuples.
# Data can be swapped from one variable to another in python using
# tuples. This eliminates the need to use a 'temp' variable.
first_number = 123
second_number = 456
first_number, second_number = second_number, first_number

first_number == 456
second_number == 123

