# Comments

Comments are essential for documenting your code and providing explanations for yourself and other developers who may read your code. Python allows you to include comments that are not executed as part of your program. They are there for clarification and can make your code more understandable.

## Single-Line Comments

A single-line comment starts with the `#` character and extends to the end of the line. Anything following the `#` is treated as a comment and is ignored by the Python interpreter.


```python
# This is a single-line comment
print("Hello, World")  # This comment is at the end of the line
```

    Hello, World
    

## Multi-Line Comments

Python does not have a specific syntax for multi-line comments like some other languages. Instead, you can create multi-line comments by using triple-quotes (`'''` or `"""`) as delimiters. The text within these delimiters is considered a comment.


```python
'''
This is a multi-line comment.
You can write multiple lines within triple-quotes.
'''
print("Hello, World")
```

    Hello, World
    

For transparency sake, this is also what it would look like using double-quotes (`"""`).


```python
"""
This is a multi-line comment.
You can write multiple lines within triple double-quotes.
"""
print("Hello, World")
```

    Hello, World
    

## Commenting Out Code

You can use comments to temporarily disable or "comment out" lines of code. This can be helpful for debugging or testing without removing the code.


```python
# This line of code is commented out.

print("This code is NOT commented out!")
# print("This code is commented out.")
```

    This code is NOT commented out!
    

## Best Practices for Comments

- Use comments to explain complex parts of your code or to provide context.
- Keep your comments concise and to the point.
- Avoid excessive commenting on straightforward code that is already self-explanatory.
- Maintain consistency in your commenting style across your codebase.

Including meaningful comments in your code is a good practice that helps others understand your code and aids in your own future reference.
