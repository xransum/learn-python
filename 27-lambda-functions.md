# Lambda Functions

## Introduction

Lambda functions, also known as anonymous functions, are a concise way to create small, anonymous functions in Python. They are particularly useful when you need a simple function for a short period without the need to define a full function using the `def` keyword. Lambda functions are often used for operations like sorting, filtering, and mapping. In Python, you create lambda functions using the `lambda` keyword.

## Syntax

The basic syntax for a lambda function is as follows:

```python
lambda arguments: expression
```

- `lambda`: The keyword used to create a lambda function.
- `arguments`: The input parameters or arguments to the function.
- `expression`: The operation to be performed using the arguments and returned as the result.

## Example 1: Basic Lambda Function

Here's a simple example of a lambda function that adds two numbers:


```python
add = lambda x, y: x + y

result = add(5, 3)
print("Sum:", result)
```

Output:

```
Sum: 8
```

In this example, the lambda function `lambda x, y: x + y` takes two arguments `x` and `y` and returns their sum.

## Example 2: Using Lambda with Built-in Functions

You can use lambda functions with built-in functions like `map()`, `filter()`, and `sorted()` for concise and readable code.

### `map()`: Applying a Function to Multiple Elements


```python
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))

print("Squared:", squared)
```

Output:

```
Squared: [1, 4, 9, 16, 25]
```

In this example, we use a lambda function to square each element in the `numbers` list.

### `filter()`: Filtering Elements Based on a Condition


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print("Even Numbers:", even_numbers)


Output:

```
Even Numbers: [2, 4, 6, 8]
```

The lambda function filters out the even numbers from the list.

### `sorted()`: Sorting a List


```python
names = ["Alice", "Bob", "Charlie", "David", "Eve"]
sorted_names = sorted(names, key=lambda name: len(name))

print("Sorted Names:", sorted_names)
```

Output:

```
Sorted Names: ['Bob', 'Eve', 'Alice', 'David', 'Charlie']
```

Here, we sort the list of names based on their lengths using a lambda function as the sorting key.

## Conclusion

Lambda functions provide a compact way to create simple functions for specific tasks. They are especially useful when you need a small function temporarily. By understanding the syntax and examples of lambda functions, you can use them effectively in your Python code.
