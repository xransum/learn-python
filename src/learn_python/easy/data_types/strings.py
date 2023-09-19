# String with double quotes.
name_1 = "John"

# String with single quotes.
name_2 = 'John'

# Strings using either double or single quotes
# are treatsd the samd
name_1 == name_2  # True

# Both are same type str
isinstance(name_1, str)  # True, name_1 is type str
isinstance(name_2, str)  # True, name_2 is type str

# When opening and closing a string using one type
#  of quote, to use either quotes within the string,
#  you must use an escape \ before the character.
# However, this doesn't apply when mixing them.
single_quote_in_single_quote = 'hasn\'t'
single_quote_in_double_quote = "hasn't"
double_quote_in_double_quote = "They said \"Hello\" today"
double_quote_in_single_quote = 'They said "Hello" today'

print(single_quote_in_single_quote)  # hasn't
print(single_quote_in_double_quote)  # hasn't

single_quote_string == double_quote_string  # True

# The escape character \n, stands for newline.
# When you print to termnial a \n, it will break the
#  output, putting everything following the \n on
#  its own line.
multiline_string = 'First\n  Second\nThird'

print(multiline_string)
# First
#   Second
# Third

multiline_string == 'First\n  Second\nThird'  # True


# String are like lists of characters, each character
#  has a unique position (i.e. index).
# Each character can be called by it's "positional
#  value" in the string using "variable[index]".
# The first index always starts with 0.
word = "Pickles!"
first_char = word[0]  # P
second_char = word[1]  # i

# To get last you can use -1, where every increment
# of -1 is 1 more character from the end.
# -1: last char
# -7: seven chars from end
last_char = word[-1]  # !
fourth_from_last = word[-4]  # l


# Strings can also be sliced for segments, given a
# start and end index delimited by a colon (:).
# Given [0:4], it includes the first char up to, but
# NOT including char at index 4.
word[0:2]  # "Pi"
word[2:-1]  # "ckles!"

