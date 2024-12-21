# Keywords and Identifiers

In Python, keywords are reserved words that have special meanings and purposes within the language. Identifiers, on the other hand, are names given to variables, functions, classes, modules, or other objects in your code. Understanding keywords and creating meaningful identifiers is essential for writing Python code effectively.

## Python Keywords

Python has a set of predefined keywords that cannot be used as identifiers. Attempting to use a keyword as an identifier will result in a syntax error. Here are some of Python's keywords:

- `and`
- `as`
- `if`
- `while`
- `for`
- `class`
- `def`
- `import`
- `from`
- `return`
- `not`
- `in`

You can view the full list of keywords using the following code:


```python
import keyword

print(keyword.kwlist)
```

    ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
    

## Creating Identifiers

Identifiers are names you give to variables, functions, classes, or other objects in Python. Here are the rules for creating valid identifiers:

- Identifiers can consist of letters (both uppercase and lowercase), digits, and underscores (_).
- Identifiers must start with a letter (a-z, A-Z) or an underscore (_).
- Identifiers are case-sensitive, meaning `myVar` and `myvar` are considered different identifiers.
- You cannot use Python keywords as identifiers.

## Examples of Identifiers

A couple examples for identifiers that are good practice.


```python
variable_name = 42
```


```python
my_var = "Hello"
```


```python
class_name = "MyClass"
```


```python
function_2 = lambda x: x * 2
```

## Invalid Identifiers

When it comes to identifiers it's best practices to avoid using numbers in your identifiers, however it's an even bigger no-no to have them starting with a number. You can run the following code to see the error that is throw when you set an identifier starting with a number.


```python
# Invalid identifiers (due to starting with a digit)
2nd_variable = 10
```


      Cell In[8], line 2
        2nd_variable = 10
         ^
    SyntaxError: invalid syntax
    


In addition, akin to assigning identifiers with numbers, assigning them using one of the above keywords will also throw the same error.


```python
# Invalid identifiers (using a Python keyword)
while = True
```


      Cell In[9], line 2
        while = True
              ^
    SyntaxError: invalid syntax
    


## Best Practices for Identifiers

To make your code more readable and maintainable, follow these naming conventions and best practices for identifiers:

- Use descriptive names that reflect the purpose of the variable or function.
- Use lowercase letters for variable and function names (e.g., `my_variable`, `calculate_result`).
- Use uppercase letters for constants (e.g., `PI`, `MAX_VALUE`).
- Use underscores to separate words in multi-word identifiers (e.g., `user_name`, `calculate_total_amount`).

By understanding Python keywords and following identifier conventions, you'll write more organized and error-free code.
