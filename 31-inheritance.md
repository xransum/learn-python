# Inheritance

Inheritance is one of the fundamental concepts in object-oriented programming (OOP). It allows you to create a new class (derived or child class) based on an existing class (base or parent class). In Python, you can achieve inheritance easily, and it's a powerful mechanism for code reuse and building more specialized classes.

## Understanding the Base Class

Before we delve into inheritance, let's create a base class to work with. A base class is the class from which another class inherits properties and behaviors. We'll call it `Animal` and give it some basic attributes and methods:


```python
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        pass
```

In this example, the `Animal` class has an `__init__` method to initialize `name` and `species`, and a `speak` method that we'll leave empty for now.

## Creating a Derived Class

To create a derived class, you define a new class with the base class in parentheses. The derived class inherits attributes and methods from the base class.


```python
class Dog(Animal):
    def speak(self):
        return f"{self.name} barks!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} meows!"
```

In this step, we've created two derived classes, `Dog` and `Cat`, that inherit from the `Animal` class. Each of these classes overrides the `speak` method to provide its own implementation.

## Using Inherited Classes

Now, let's use our derived classes to create instances and invoke methods:


```python
dog = Dog("Buddy", "Dog")
cat = Cat("Whiskers", "Cat")

print(dog.speak())  # Output: Buddy barks!
print(cat.speak())  # Output: Whiskers meows!
```

In this step, we've created instances of the `Dog` and `Cat` classes and called the `speak` method. Each instance correctly calls the overridden method from its own class.

## Accessing Base Class Methods

You can also access methods from the base class using the derived class. For example, you might want to call the `__init__` method of the `Animal` class:


```python
class Horse(Animal):
    def speak(self):
        return f"{self.name} neighs!"

    def print_info(self):
        return f"{self.name} is a {self.species}"

horse = Horse("Thunder", "Horse")

print(horse.speak())       # Output: Thunder neighs!
print(horse.print_info())  # Output: Thunder is a Horse
```

In this step, we've created a `Horse` class that overrides the `speak` method and introduces a new method `print_info`. By calling `__init__` and other methods from the base class, you can reuse code effectively.

## Multiple Inheritance

Python supports multiple inheritance, meaning a class can inherit from multiple base classes. Here's an example:


```python
class Bird:
    def speak(self):
        return f"{self.name} chirps!"

class Parrot(Dog, Bird):
    pass

parrot = Parrot("Polly", "Parrot")

print(parrot.speak())  # Output: Polly barks!
```

In this step, we've created a `Parrot` class that inherits from both `Dog` and `Bird`. This is an advanced concept, but it shows the flexibility of inheritance in Python.
