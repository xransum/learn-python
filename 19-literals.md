# Literals

In Python, literals represent fixed values that are used in expressions or assignments. Understanding different types of literals is fundamental for writing Python code. Let's explore the main types of literals in Python:

## Numeric Literals

Numeric literals are used to represent numerical values. Python supports various numeric types:

- **Integers**: Integer literals are whole numbers. They can be positive or negative.
- **Floating-Point Numbers**: Floating-point literals represent real numbers and include a decimal point.

### Examples of Numeric Literals

An integer literal:


```python
integer_literal = 42
```

A floating-point literal:


```python
float_literal = 3.14159
```

## String Literals

String literals are used to represent sequences of characters, such as text. Python supports single-quoted ('), double-quoted ("), and triple-quoted (''' or """) strings.

### Examples of String Literals

Single-quoted string:


```python
single_quoted = 'Hello, World!'
```

Double-quoted string:


```python
double_quoted = "Python Programming"
```

Triple-quoted string (useful for multiline strings):


```python
multiline_string = '''This is a
multiline string.'''
```

## Boolean Literals

Boolean literals represent truth values. In Python, these are `True` and `False`.

### Examples of Boolean Literals

True boolean:


```python
is_python_fun = True
```

False boolean:

is_learning = False

## Special Literals

Python includes two special literals:

- `None`: Represents a null or undefined value.
- `Ellipsis` (`...`): Typically used as a placeholder for code yet to be written.

### Examples of Special Literals

A value that is empty:


```python
empty_value = None
```

Placeholder code:


```python
some_undone_code = ...
```

## Raw String Literals

Raw string literals are used when you want to treat backslashes as literal characters instead of escape characters.

### Examples of Raw String Literals

A raw string of a filepath, where `\U` and `\Y` are not render as escape characters:


```python
raw_string = r'C:\Users\YourName'
```

## Bytes and Bytearray Literals

Bytes and bytearray literals represent sequences of bytes. Bytes are immutable, while bytearrays are mutable.

### Examples of Bytes and Bytearray Literals

Bytes literal:


```python
bytes_literal = b'Hello'
```

Bytearray literal:


```python
bytearray_literal = bytearray([72, 101, 108, 108, 111])
```

Understanding these literals is essential for working with different data types and writing Python code effectively. You can use these literals in various contexts, such as assignments, expressions, and function parameters.
