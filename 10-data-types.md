# Data Types

In Python, data types are crucial as they define the type of data a variable can hold. Understanding data types is fundamental for writing robust and efficient Python code. Python provides a variety of built-in data types that serve different purposes. In this section, we will explore the fundamental data types and introduce you to some common data structures.

## Numeric Data Types

**Integer (int):** Integers are whole numbers, both positive and negative, without a fractional part. They can be defined using a simple assignment, like `x = 42`.


```python
x = 10
y = 12345667789
```

**Floating-Point (float):** Floating-point numbers represent real numbers and can include a decimal point. For example, `y = 3.14` defines a floating-point variable.


```python
pi = 3.14159
```

## Text Data Type

**String (str):** Strings are used to represent text data. You can enclose a string in single (' ') or double (" ") quotes. For instance, `name = "Alice"` defines a string variable.

Single-quotes:


```python
name = 'Bob'
```

Double-quotes:


```python
name = "Bob"
```

Multi-line single-quotes:


```python
name = '''Bob
Marley'''
```

Multi-line double-quotes:


```python
name = """Bob
Marley"""
```

## Boolean Data Type

**Boolean (bool):** Booleans represent either `True` or `False` values. They are often used for conditions and comparisons. For example, `flag = True` sets a boolean variable to `True`.

True boolean value:


```python
flag = True
```

False boolean value:


```python
flag = False
```

## Common Data Structures

**List:** A list is an ordered collection of elements. It can contain items of different data types. To define a list, you can use square brackets:


```python
my_list = [1, "apple", True]
```

**Tuple:** A tuple is similar to a list but is immutable, meaning its elements cannot be changed after creation. You can define a tuple using parentheses, like:


```python
my_tuple = (1, "banana", False)
```

**Dictionary:** A dictionary is a collection of key-value pairs. You can create a dictionary using curly braces and colons:


```python
my_dict = {"name": "Bob", "age": 30}
```

**Set:** A set is an unordered collection of unique elements. You can define a set using curly braces, for instance:


```python
my_set = {1, 2, 3}
```

## Type Checking

In Python, you can check the data type of a variable using the `type()` function. For example:


```python
x = 42
print(type(x))
```

    <class 'int'>
    

You can do this with nearly everything that is assignable to a variable or declarable.


```python
name = "Alice"
print(type(name))
```

As an example, here's what it looks like for all of the types:


```python
print(type(1337))
print(type(3.1415))
print(type('Bob'))
print(type(True))
print(type([1, "apple", True]))
print(type((1, "banana", False)))
print(type({"name": "Bob", "age": 30}))
print(type({1, 2, 3}))
```

    <class 'int'>
    <class 'float'>
    <class 'str'>
    <class 'bool'>
    <class 'list'>
    <class 'tuple'>
    <class 'dict'>
    <class 'set'>
    

Understanding data types allows you to work with different kinds of data and perform operations specific to each data type. It's a fundamental concept in Python programming.
