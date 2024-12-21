# Numbers

In Python, you can work with various types of numbers, including integers and floating-point numbers. This document explores the basics of working with numbers, arithmetic operations, type conversion, and some built-in functions related to numbers.

## Integers

Integers (int) are whole numbers without a fractional part. You can perform various mathematical operations with integers in Python.


```python
x = 5  # Assign an integer
y = 3  # Assign another integer
```

### Arithmetic Operations

Python supports the following arithmetic operations for integers:

- Addition (`+`)
- Subtraction (`-`)
- Multiplication (`*`)
- Division (`/`)
- Modulus (remainder) (`%`)
- Exponentiation (`**`)
- Floor division (integer division) (`//`)


```python
sum_result = x + y  # Addition
print(sum_result)

diff_result = x - y  # Subtraction
print(diff_result)

prod_result = x * y  # Multiplication
print(prod_result)

div_result = x / y  # Division
print(div_result)

mod_result = x % y  # Modulus (remainder)
print(mod_result)

exp_result = x ** y  # Exponentiation
print(exp_result)

floor_div_result = x // y  # Floor division (integer division)
print(floor_div_result)
```

    8
    2
    15
    1.6666666666666667
    2
    125
    1
    

## Floating-Point Numbers

Floating-point numbers (float) are numbers with a decimal point or in exponential form. They are suitable for representing real numbers in scientific computations.


```python
a = 3.14  # Assign a float
b = 2.0  # Assign another float
```

### Arithmetic Operations

Floating-point numbers support the same arithmetic operations as integers.


```python
sum_float = a + b  # Addition
print(sum_float)

diff_float = a - b  # Subtraction
print(diff_float)

prod_float = a * b  # Multiplication
print(prod_float)

div_float = a / b  # Division
print(div_float)

exp_float = a ** b  # Exponentiation
print(exp_float)
```

    5.140000000000001
    1.1400000000000001
    6.28
    1.57
    9.8596
    

### Type Conversion

You can convert numbers between integer and float data types using built-in functions.


```python
int_to_float = float(x)  # Convert integer to float
float_to_int = int(b)  # Convert float to integer

print(type(int_to_float))
print(type(float_to_int))
```

    <class 'float'>
    <class 'int'>
    

### Built-in Number Functions

Python provides several built-in functions for working with numbers:

- `abs()`: Returns the absolute value of a number.
- `round()`: Rounds a floating-point number to the nearest integer.
- `max()`: Returns the largest of the input values.
- `min()`: Returns the smallest of the input values.


```python
abs_result = abs(-10)  # Absolute value
print(abs_result)

round_result = round(3.6)  # Round to the nearest integer
print(round_result)

max_result = max(5, 7, 2)  # Maximum value
print(max_result)

min_result = min(5, 7, 2)  # Minimum value
print(min_result)
```

    10
    4
    7
    2
    

### Mathematical Functions

Python's `math` module provides a wide range of mathematical functions. To use these functions, you need to import the `math` module.


```python
import math

# Examples
sqrt_result = math.sqrt(16)  # Square root
print(sqrt_result)

log_result = math.log(2)  # Natural logarithm
print(log_result)

cos_result = math.cos(math.pi)  # Cosine function
print(cos_result)
```

    4.0
    0.6931471805599453
    -1.0
    
