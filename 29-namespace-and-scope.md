# Namespace and Scope

Python's concept of namespace and scope is crucial for understanding variable lifetime, variable accessibility, and how different parts of your code interact. In this section, we will explore the concepts of namespace and scope in Python.

## Namespace

A namespace is a container that holds a set of identifiers (variable names) and their corresponding objects (values). In Python, namespaces help in avoiding naming conflicts and organizing variables, functions, classes, and modules.

There are three main types of namespaces:

1. **Local Namespace**: This namespace contains local variables, which are defined within a function or method. The local namespace is temporary and exists only during the execution of the function.

2. **Enclosing Namespace**: This namespace is used for nested functions, where inner functions can access variables from outer functions. Each function has its own local namespace.

3. **Global Namespace**: The global namespace contains variables and functions defined at the top level of a module or script. It exists throughout the entire runtime of the program and is shared across all functions and modules.

## Scope

Scope refers to the region or context where an identifier (variable or function) is accessible. Python has the following scope levels:

1. **Local Scope**: Variables defined within a function are in the local scope and can only be accessed within that function.

2. **Enclosing Scope**: When a function is nested inside another function, it can access variables from the enclosing scope. This allows inner functions to "capture" variables from their containing functions.

3. **Global Scope**: Variables defined at the top level of a module are in the global scope and are accessible to all functions and code within that module.

4. **Built-in Scope**: Python provides a built-in scope that contains commonly used functions and objects such as `print()` and `len()`. These can be accessed from any part of the code without explicit declaration.

## Local Namespace and Scope

In this example, `x` is in the local scope of `outer_function`, and `y` is in the local scope of `inner_function`. The `inner_function` can access `x` from the enclosing scope, demonstrating the concept of enclosing namespaces and scope.


```python
def outer_function():
    x = 10  # Variable in the local scope of outer_function

    def inner_function():
        y = 20  # Variable in the local scope of inner_function
        print("inner_function: ", x + y)  # Accesses x from the enclosing scope

    inner_function()
    print("outer_function: ", x)

outer_function()
```

    inner_function:  30
    outer_function:  10
    

## Global Namespace and Scope

In this example, `a` is in the global scope, and both the `global_example` function and the code outside it can access `a`.


```python
a = 5  # Variable in the global scope

def global_example():
    print("global_example", a)  # Accesses the global variable a

global_example()
print(a)
```

    global_example 5
    5
    

## Best Practices

- Avoid using the same variable names in different namespaces to prevent naming conflicts.
- Use meaningful variable and function names to improve code readability.

Understanding namespaces and scope is fundamental for writing clean and organized Python code. It allows you to manage variables effectively and create modular and maintainable programs.
