# Operators in Python

Operators are symbols in Python that perform operations on variables and values. They allow you to manipulate and perform calculations on data. Python supports various types of operators, including arithmetic, comparison, logical, and assignment operators. In this guide, we will explore these different types of operators and provide examples to help you understand their usage.

## Arithmetic Operators

Arithmetic operators are used for performing mathematical operations. Python provides the following arithmetic operators:

- Addition (`+`): Adds two numbers.
- Subtraction (`-`): Subtracts the second number from the first.
- Multiplication (`*`): Multiplies two numbers.
- Division (`/`): Divides the first number by the second.
- Modulus (`%`): Returns the remainder of the division.
- Exponentiation (`**`): Raises the first number to the power of the second.
- Floor Division (`//`): Returns the integer part of the division result.

Examples:


```python
x = 10
y = 5

addition_result = x + y         # 15
subtraction_result = x - y      # 5
multiplication_result = x * y   # 50
division_result = x / y         # 2.0
modulus_result = x % y          # 0
exponentiation_result = x ** y  # 100000
floor_division_result = x // y  # 2
```

## Comparison Operators

Comparison operators are used to compare two values. They return a Boolean value (`True` or `False`) based on the comparison. Python provides the following comparison operators:

- **Equal to** (`==`): Returns `True` if the values are equal.
- **Not equal to** (`!=`): Returns `True` if the values are not equal.
- **Greater than** (`>`): Returns `True` if the first value is greater.
- **Less than** (`<`): Returns `True` if the first value is smaller.
- **Greater than** *or* **equal to** (`>=`): Returns `True` if the first value is greater or equal.
- **Less than** *or* **equal to** (`<=`): Returns `True` if the first value is smaller or equal.

Examples:


```python
a = 10
b = 5

is_equal = a == b             # False
is_not_equal = a != b         # True
is_greater = a > b            # True
is_less = a < b               # False
is_greater_or_equal = a >= b  # True
is_less_or_equal = a <= b     # False
```

## Logical Operators

Logical operators are used to combine or manipulate Boolean values. They include:

- Logical **AND** (`and`): Returns `True` if both conditions are `True`.
- Logical **OR** (`or`): Returns `True` if at least one condition is `True`.
- Logical **NOT** (`not`): Reverses the logical state of the condition.

Examples:


```python
p = True
q = False

logical_and_result = p and q  # False
logical_or_result = p or q    # True
logical_not_result = not p    # False
```

## Assignment Operators

Assignment operators are used to assign values to variables. The basic assignment operator is `=`. There are also compound assignment operators that combine an operation with assignment, such as `+=`, `-=`, etc.

**Assignment Operator (`=`)**: Assigns the value on the right to the variable on the left.


```python
x = 5  # x is assigned the value 5
```

**Addition Assignment (`+=`)**: Adds the value on the right to the variable and assigns the result to the variable.


```python
x = 5
x += 3  # x is now 8 (5 + 3)
```

**Subtraction Assignment (`-=`)**: Subtracts the value on the right from the variable and assigns the result to the variable.


```python
x = 10
x -= 4  # x is now 6 (10 - 4)
```

**Multiplication Assignment (`*=`)**: Multiplies the variable by the value on the right and assigns the result to the variable.


```python
x = 3
x *= 2  # x is now 6 (3 * 2)
```

**Division Assignment (`/=`)**: Divides the variable by the value on the right and assigns the result to the variable.


```python
x = 12
x /= 4  # x is now 3.0 (12 / 4)
```

**Modulus Assignment (`%=`)**: Performs modulus division on the variable and assigns the remainder to the variable.


```python
x = 15
x %= 7  # x is now 1 (15 % 7)
```

**Exponentiation Assignment (`**=`)**: Raises the variable to the power of the value on the right and assigns the result to the variable.


```python
x = 2
x **= 3  # x is now 8 (2^3)
```

**Floor Division Assignment (`//=`)**: Performs floor division on the variable and assigns the result to the variable.


```python
x = 11
x //= 3  # x is now 3 (11 // 3)
```

These assignment operators provide a convenient way to modify the value of a variable while performing an operation in a single step.
