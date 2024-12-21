# For Loops

## Introduction

A "for loop" is a fundamental control structure in Python that allows you to repeat a block of code a specified number of times or over the elements of an iterable (e.g., lists, strings, dictionaries). It is a powerful tool for automating repetitive tasks and iterating through collections of data.

## Basic "for" Loop Syntax

The basic syntax of a "for loop" in Python is as follows:

```python
for variable in iterable:
    # Code to be repeated
```

- `variable`: A variable that takes on the values of the elements in the iterable one by one.
- `iterable`: The collection you want to loop through, such as a list, string, or range.

## Iterating Through a List

You can use a "for loop" to iterate through the elements of a list:


```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
```

This code will print each fruit in the list on a new line:

```
apple
banana
cherry
```

## Using the "range" Function

The `range()` function generates a sequence of numbers that you can use with a "for loop" to perform a specific number of iterations.


```python
for i in range(5):
    print(i)
```

This code will print the numbers from 0 to 4.

```
0
1
2
3
4
```

## "for" Loop with Strings

You can loop through the characters of a string using a "for loop":


```python
text = "Hello, Python"

for char in text:
    print(char)
```

This code will print each character of the string:

```
H
e
l
l
o
,
 
P
y
t
h
o
n
```

## Nested "for" Loops

You can also use nested "for loops" to iterate through multiple sequences simultaneously:


```python
adjectives = ["red", "green", "blue"]
nouns = ["apple", "tree", "sky"]

for adj in adjectives:
    for noun in nouns:
        print(adj, noun)
```

This code will generate combinations of adjectives and nouns:

```
red apple
red tree
red sky
green apple
green tree
green sky
blue apple
blue tree
blue sky
```

## Conclusion

"for loops" are essential for repetitive tasks, and they are widely used in Python for data processing, automation, and more. By mastering "for loops," you can efficiently work with collections of data and solve various programming challenges.
