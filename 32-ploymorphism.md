# Polymorphism

Polymorphism is an essential concept in object-oriented programming, allowing objects of different classes to be treated as if they were objects of a common base class. In Python, polymorphism is achieved through the use of inheritance and method overriding.

## Inheritance and Base Class

Polymorphism begins with inheritance, where you create a base class and derive subclasses from it. In Python, you can inherit from a base class like this:


```python
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"
```

In this example, `Animal` is the base class, and `Dog` and `Cat` are subclasses. They all have a method called `speak()`, which is overridden in the subclasses.

## Polymorphic Behavior

With our classes set up, we can now achieve polymorphism by treating objects from different classes uniformly. Consider the following code:


```python
def animal_sound(animal):
    print(animal.speak())

dog = Dog()
cat = Cat()

animal_sound(dog)  # Output: "Woof!"
animal_sound(cat)  # Output: "Meow!"
```

Here, the `animal_sound` function takes an `animal` object as an argument. This function doesn't need to know if the object passed is a `Dog` or a `Cat`. It simply calls the `speak()` method on the object, and the overridden method in the respective subclass is executed.

## The Power of Polymorphism

Polymorphism makes your code more flexible and extensible. You can add new subclasses without modifying existing code. For instance, let's introduce a `Duck` class:


```python
class Duck(Animal):
    def speak(self):
        return "Quack!"
```

You can now use polymorphism with the `Duck` class without changing the `animal_sound` function:


```python
duck = Duck()
animal_sound(duck)  # Output: "Quack!"
```

## Abstract Base Classes

In Python, you can also use abstract base classes to define methods that must be overridden by subclasses. This enforces polymorphism. For example, you can create an abstract base class for animals:


```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass
```

Any class that inherits from `Animal` must implement the `speak` method, ensuring consistent polymorphic behavior.

## Built-in Polymorphism

Polymorphism is not limited to user-defined classes. Python's built-in types and functions also embrace polymorphism. For instance, the `len()` function can be used with different sequences:


```python
print(len([1, 2, 3]))  # Output: 3
print(len("Hello"))    # Output: 5
```

The same function `len()` works with lists and strings, demonstrating polymorphic behavior.
