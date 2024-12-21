# Booleans

In Python, a Boolean is a data type that can have one of two values: `True` or `False`. Booleans are often used to make decisions in programs and represent the truth or validity of conditions.

## True and False

In Python, `True` and `False` are reserved keywords that represent Boolean values. They are used to evaluate conditions and make logical decisions.


```python
x = True
y = False

print(x)  # True
print(y)  # False
```

    True
    False
    

## Comparison Operators

Comparison operators are used to compare two values and return a Boolean result.

- `==` (equal): Returns `True` if both values are equal.
- `!=` (not equal): Returns `True` if the values are not equal.
- `>` (greater than): Returns `True` if the left value is greater than the right value.
- `<` (less than): Returns `True` if the left value is less than the right value.
- `>=` (greater than or equal): Returns `True` if the left value is greater than or equal to the right value.
- `<=` (less than or equal): Returns `True` if the left value is less than or equal to the right value.


```python
a = 10
b = 5

print(a == b)  # False (not equal)
print(a != b)  # True (not equal)
print(a > b)   # True (greater than)
print(a < b)   # False (less than)
print(a >= b)  # True (greater than or equal)
print(a <= b)  # False (less than or equal)
```

    False
    True
    True
    False
    True
    False
    

## Logical Operators

Logical operators are used to combine Boolean values or expressions and return a Boolean result.

- `and`: Returns `True` if both conditions are `True`.
- `or`: Returns `True` if at least one of the conditions is `True`.
- `not`: Returns the opposite Boolean value (negation).


```python
x = True
y = False

print(x and y)  # False (True and False)
print(x or y)   # True (True or False)
print(not x)    # False (not True)
```

    False
    True
    False
    

## Boolean Values in Conditions

Booleans are often used in conditional statements to make decisions in programs. For example, in an `if` statement, the code block is executed only if the condition is `True`.


```python
x = 5
if x > 3:
    print("x is greater than 3")
```

    x is greater than 3
    

## Built-in Functions

Python provides built-in functions to work with Booleans, such as `bool()`, which allows you to evaluate an expression or value as a Boolean.


```python
print(bool(0))      # False (0 is considered False)
print(bool(42))     # True (non-zero values are considered True)
print(bool("Hello")) # True (non-empty strings are considered True)
```

    False
    True
    True
    

## Identity Operators

Identity operators are used to compare the memory location of two objects.

- `is`: Returns `True` if both variables are the same object.
- `is not`: Returns `True` if both variables are not the same object.


```python
a = [1, 2, 3]
b = a

print(a is b)   # True (a and b reference the same list object)
print(a is not b)  # False (a and b reference the same list object)
```

    True
    False
    

## Membership Operators

Membership operators are used to test if a sequence is present in an object.

- `in`: Returns `True` if a specified value is found in the sequence.
- `not in`: Returns `True` if a specified value is not found in the sequence.


```python
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)   # True (the sequence contains "banana")
print("orange" not in fruits)  # True ("orange" is not in the sequence)
```

    True
    True
    
