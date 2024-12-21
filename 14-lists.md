# Lists

In Python, a list is a collection of items that can be of different types, such as integers, strings, or even other lists. Lists are ordered and mutable, which means you can change their content. Lists are defined by enclosing items in square brackets (`[]`) and separating them with commas.


```python
my_list = [1, 2, 3, "apple", "banana", "cherry"]
```

## Accessing List Items

You can access items in a list by referring to their index number. Python uses 0-based indexing, so the first item has an index of 0, the second item has an index of 1, and so on.


```python
fruits = ["apple", "banana", "cherry"]
print(fruits[1])  # Accesses the second item, which is "banana"
```

    banana
    

## Negative Indexing

You can also use negative indexing to access items from the end of the list. The last item has an index of -1, the second to last item has an index of -2, and so on.


```python
fruits = ["apple", "banana", "cherry"]
print(fruits[-1])  # Accesses the last item, which is "cherry"
```

    cherry
    

## Slicing Lists

You can specify a range of indexes by using the colon (`:`) operator. This is known as slicing. The result will be a new list containing the specified items.


```python
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
subset = fruits[1:4]  # Creates a new list with items from index 1 to 3
print(subset)  # Output: ["banana", "cherry", "date"]
```

    ['banana', 'cherry', 'date']
    

## Changing List Items

You can change the value of a specific item by referring to its index number and assigning a new value.


```python
fruits = ["apple", "banana", "cherry"]
fruits[1] = "kiwi"
print(fruits)  # Changes the second item to "kiwi"
```

    ['apple', 'kiwi', 'cherry']
    

## List Length

To get the number of items in a list, you can use the `len()` function.


```python
fruits = ["apple", "banana", "cherry"]
count = len(fruits)
print(count)  # Prints the number of items (3)
```

    3
    

## Adding Items

You can add items to the end of a list using the `append()` method or insert items at a specific position using the `insert()` method.


```python
fruits = ["apple", "banana", "cherry"]
fruits.append("date")  # Adds "date" to the end of the list
fruits.insert(1, "kiwi")  # Inserts "kiwi" at index 1
```

## Removing Items

You can remove items from a list using methods like `remove()`, `pop()`, or `del`.


```python
fruits = ["apple", "banana", "cherry", "tomatoe"]
fruits.remove("banana")  # Removes "banana" from the list
fruits.pop(0)  # Removes the item at index 0 (the first item)
del fruits[1]  # Deletes the item at index 1 (the second item)
```

## List Comprehensions

List comprehensions provide a concise way to create lists based on existing lists. They allow you to apply an expression to each item in a list and create a new list from the results.


```python
numbers = [1, 2, 3, 4, 5]
squared = [x**2 for x in numbers]  # Creates a new list with squared values
print(squared)  # Output: [1, 4, 9, 16, 25]
```

    [1, 4, 9, 16, 25]
    

## Built-in List Methods

Python provides a variety of built-in methods to manipulate lists. Here are some commonly used methods:

- `append()`: Adds an item to the end of the list.
- `insert()`: Inserts an item at a specified position.
- `remove()`: Removes the first occurrence of a specific item.
- `pop()`: Removes an item at a specified position or the last item.
- `clear()`: Removes all items from the list.
- `reverse()`: Reverses the order of items in the list.
- `sort()`: Sorts the items in the list.


```python
numbers = [3, 1, 4, 2, 5]
numbers.sort()  # Sorts the list in ascending order
print(numbers)  # Output: [1, 2, 3, 4, 5]
```

    [1, 2, 3, 4, 5]
    
