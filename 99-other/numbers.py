
"""Integer type

Int, or integer, is a whole number, positive or negative,
without decimals, of unlimited length.
"""

positive_integer = 1
negative_integer = -3255522
big_integer = 35656222554887711

isinstance(positive_integer, int)
isinstance(negative_integer, int)
isinstance(big_integer, int)


"""Boolean

Booleans represent the truth values False and True. The two objects representing the values
False and True are the only Boolean objects. The Boolean type is a subtype of the integer type,
and Boolean values behave like the values 0 and 1, respectively, in almost all contexts, the
exception being that when converted to a string, the strings "False" or "True" are returned,
respectively.
"""

true_boolean = True
false_boolean = False

true_boolean
not false_boolean

isinstance(true_boolean, bool)
isinstance(false_boolean, bool)

# Let's try to cast boolean to string.
str(true_boolean) == "True"
str(false_boolean) == "False"



"""Float type

Float, or "floating point number" is a number, positive or negative,
containing one or more decimals.
"""

float_number = 7.0
# Another way of declaring float is using float() function.
float_number_via_function = float(7)
float_negative = -35.59

float_number == float_number_via_function
isinstance(float_number, float)
isinstance(float_number_via_function, float)
isinstance(float_negative, float)

# Float can also be scientific numbers with an "e" to indicate
# the power of 10.
float_with_small_e = 35e3
float_with_big_e = 12E4

float_with_small_e == 35000
float_with_big_e == 120000
isinstance(12E4, float)
isinstance(-87.7e100, float)



"""Complex Type"""

complex_number_1 = 5 + 6j
complex_number_2 = 3 - 2j

isinstance(complex_number_1, complex)
isinstance(complex_number_2, complex)
complex_number_1 * complex_number_2 == 27 + 8j



"""Basic operations"""

# Addition.
2 + 4 == 6

# Multiplication.
2 * 4 == 8

# Division always returns a floating point number.
12 / 3 == 4.0
12 / 5 == 2.4
17 / 3 == 5.666666666666667

# Modulo operator returns the remainder of the division.
12 % 3 == 0
13 % 3 == 1

# Floor division discards the fractional part.
17 // 3 == 5

# Raising the number to specific power.
5 ** 2 == 25  # 5 squared
2 ** 7 == 128  # 2 to the power of 7

# There is full support for floating point; operators with
# mixed type operands convert the integer operand to floating point.
4 * 3.75 - 1 == 14.0
