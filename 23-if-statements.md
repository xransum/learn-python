# If Statements

Conditional statements are a fundamental part of programming, allowing you to make decisions in your code based on specific conditions. In Python, you can use `if`, `if-else`, and `if-elif-else` statements to control the flow of your program.

## The `if` Statement

The simplest conditional statement is the `if` statement. It allows you to execute a block of code if a certain condition is met. If the condition is `True`, the code block is executed. If the condition is `False`, the code block is skipped.

**Syntax:**

```python
if condition:
    # Code to execute if the condition is True
```

**Example:**

In the below, the code inside the `if` block is executed because the `age` variable is greater than or equal to 18.


```python
age = 25

if age >= 18:
    print("You are an adult.")
```

## The `if-else` Statement

The `if-else` statement allows you to specify two code blocks: one to execute if the condition is `True`, and another to execute if the condition is `False`.

**Syntax:**

```python
if condition:
    # Code to execute if the condition is True
else:
    # Code to execute if the condition is False
```

**Example:**

In the below, the first `print` statement will be executed because the temperature is not greater than or equal to 30.


```python
temperature = 28

if temperature >= 30:
    print("It's a hot day.")
else:
    print("It's not too hot.")
```

## The `if-elif-else` Statement

When you have multiple conditions to check, you can use the `if-elif-else` statement. It allows you to test several conditions one by one and execute the corresponding code block of the first `True` condition. If none of the conditions are `True`, the code in the `else` block is executed.

**Syntax:**

```python
if condition1:
    # Code to execute if condition1 is True
elif condition2:
    # Code to execute if condition2 is True
else:
    # Code to execute if no conditions are True
```

**Example:**

In the below, the code block under `elif grade >= 70` is executed because it's the first condition that is `True`.



```python
grade = 75

if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
else:
    print("F")
```

## Nested Conditional Statements

You can also nest conditional statements within one another for more complex decision-making.

**Example:**

In this example, the code executes based on the values of `x` and `y`.


```python
x = 10
y = 5

if x > 5:
    if y > 2:
        print("Both conditions are True.")
    else:
        print("The first condition is True, but the second is not.")
else:
    print("The first condition is False.")
```

Conditional statements are essential for controlling the logic of your Python programs. They allow you to create dynamic and responsive applications based on various conditions and inputs.
