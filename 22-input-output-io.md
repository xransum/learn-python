# Input and Output (I/O)

Input and output (I/O) are fundamental concepts in programming. They allow your Python programs to interact with users by accepting input and displaying output. Python provides various functions and methods for handling I/O operations, making it versatile for both basic and advanced input and output tasks.

## User Input

To obtain user input in Python, you can use the `input()` function. It reads a line of text entered by the user and returns it as a string. Here's a simple example:


```python
user_input = input("Enter your name: ")
print("Hello, " + user_input + "!")
```

In this example, `input("Enter your name: ")` displays a prompt to the user, and the entered text is stored in the `user_input` variable.

## Output

Python offers several ways to display output, but one of the most common is using the `print()` function. You can use it to output text and variables, with optional formatting.


```python
name = "John"
age = 30

print("Name:", name)
print("Age:", age)
```

    Name: John
    Age: 30
    

With the expected output being:

```
Name: John
Age: 30
```

## Formatted Output

You can format output using placeholders in the `print()` function. The `%` operator is used to insert values into the string.


```python
name = "Alice"
age = 25

print("Name: %s, Age: %d" % (name, age))
```

Here, `%s` is a placeholder for a string, and `%d` is for an integer. The values are provided in a tuple after the `%` operator.

## f-strings (Python 3.6+)

A more modern way to format output is by using f-strings, introduced in Python 3.6. They are concise and offer improved readability:


```python
name = "Bob"
age = 40

print(f"Name: {name}, Age: {age}")
```

The output is the same as the previous example:

```
Name: Bob, Age: 40
```

Python's I/O operations make it easy to interact with users and display information in various formats. Understanding these concepts is essential for creating functional and user-friendly applications.
