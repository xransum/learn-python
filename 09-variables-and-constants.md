# Variables & Constants

In Python, variables and constants are fundamental components used to store and manage data. Understanding how to declare and use them is essential for writing Python programs. We'll cover variables, naming conventions, and the role of constants in this section.

## Variables

A variable is a named container used to store data values. It allows you to assign a name to a specific piece of data, making it easier to work with and manipulate. To declare a variable in Python, you simply choose a name and use the assignment operator `=` to associate a value with that name.

Here's how you declare a variable:


```python
variable_name = 42
```

In the example above, we've declared a variable named `variable_name` and assigned it the value `42`.

## Naming Conventions

Python has naming conventions to make your code more readable and maintainable:

- Use lowercase letters for variable names (e.g., `my_variable`, `count`).
- Use uppercase letters for constants (e.g., `PI`, `MAX_VALUE`).
- Use underscores to separate words in multi-word variable names (e.g., `user_name`, `total_amount`).

## Constants

A constant is a variable with a fixed value that does not change during the execution of your program. While Python does not have a built-in constant type, it is a common practice to use uppercase variable names to indicate constants.

For example, to define a constant named `PI`, you can use all uppercase letters:


```python
PI = 3.14159
```

In some circumstances, when your code gets a bit more complex, descriptiveness in your variable names and constants would help with code readability.


```python
VALUE_OF_PI = 3.14159
```

Constants are used to represent values that should remain unchanged throughout the program, such as mathematical constants or configuration settings.

By understanding variables, naming conventions, and constants, you can effectively manage data in your Python programs.
