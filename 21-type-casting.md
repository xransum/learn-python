# Type Casting

In Python, type casting (or type conversion) refers to changing the data type of a value from one type to another. This is a common operation when you want to perform arithmetic operations, manipulate data, or interact with different types of variables. There are two main types of type casting: implicit and explicit.

This example illustrates the purpose for type casting, here this tries to combine a string with an int:


```python
num_str = "10"
num_int = 11
result = num_str + num_int
```

As shown, we get the error `TypeError: can only concatenate str (not "int") to str`, meaning we cannot combine two values of dissimilar data types. Type casting allows for us to be able to ensure both sides of the operation are of the same type to ensure these errors are not throw in our logic.

## Implicit Type Casting

Implicit type casting, also known as type coercion, occurs automatically when Python converts one data type to another to perform a specific operation. For example, when you add an integer and a floating-point number, Python implicitly converts the integer to a float to carry out the addition.

The following will illustrate implicit type casting:


```python
x = 5        # integer
y = 2.5      # float
result = x + y
print(result)
```

In this case, Python automatically converts the integer `x` to a float before adding it to `y`.

## Explicit Type Casting

Explicit type casting, on the other hand, requires you to manually convert a value from one data type to another using built-in functions. Python provides several functions for explicit type casting:

`int()`: Converts a value to an integer.


```python
num_a = int("42")  # 42
num_b = int(3.14)  # 3
```

`float()`: Converts a value to a float.


```python
num_a = float("42")  # 42.0
num_b = float(99)    # 99.0
```

`str()`: Converts a value to a string.


```python
str_a = str(42)        # "42"
str_b = str(3.14)      # "3.14"
```

`tuple()`: Converts a value to a tuple.


```python
tuple_a = tuple(["a", "b", "c"])  # ("a", "b", "c")
tuple_b = tuple("def")            # ("d", "e", "f")
tuple_c = tuple({"g", "h", "i"})  # ("g", "h", "i")
```

`list()`: Converts a value to a list.


```python
list_a = list(("a", "b", "c"))  # ["a", "b", "c"]
list_b = list("def")            # ["d", "e", "f"]
list_c = list({"g", "h", "i"})  # ["g", "h", "i"]
```

`dict()`: Converts a value to a dict.


```python
dict_a = dict([("foo", "bar")]) # {"foo": "bar"}
```

Here's an example that illustrates explicit type casting:

## Type Casting Functions

Python provides built-in functions for type casting, as mentioned earlier. You can use these functions to convert between different data types, ensuring your data is in the required format for specific operations.

For example, if you receive user input as a string and need to perform mathematical calculations, you can use type casting to convert the input to a numeric data type (e.g., `int` or `float`) before performing the calculations.

Type casting is a powerful feature in Python that allows you to work with data in various forms and manipulate it as needed for your applications.

By understanding both implicit and explicit type casting, you can effectively manage data types in your Python programs.
