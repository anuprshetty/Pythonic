# Getters and Setters are members(methods) of a class.
# Methods are like functions associated to a specific object or class. They are like functionality that the object can perform.
# Getters and Setters let us get and set the value of a non-public attribute.
# They protect the attributes by providing an indirect way to access them and modify them.
# We can make an attribute non-public and still provide a way to work with it indirectly.

# Getters:
# syntax: get_<attribute>
# Ex: get_name
class Movie:
    def __init__(self, title, rating):
        self._title = title
        self.rating = rating

    def get_title(self):
        return self._title

    def set_title(self, title):
        if isinstance(title, str) and title.isalpha():
            self._title = title
        else:
            print("Invalid title")

movie = Movie("Pursuit of HappYness", 10)
print(movie.get_title())

# Setters:
# Advantage: With setters, we can validate the new value before assigning it to the attribute.
# syntax: set_<attribute>
# Ex: set_name
movie.set_title("Inception")
print(movie.get_title())

# NOTE:
# We will commonly see Getters and Setters in programming langauges like Java. But in python, we use something called Properties.
# Properties --> Pythonic way of working with Non-Public attributes, Getters and Setters.

# Properties:
class Dog:
    def __init__(self, age):
        self._age = age

    # Getter
    def get_age(self):
        return self._age

    # Setter
    def set_age(self, age):
        if isinstance(age, int) and 0 < age <= 30:
            self._age = age
        else:
            print("Invalid age")

    # Deleter
    def del_age(self):
        del self._age

    # Property
    # Prototype: class property(fget=None, fset=None, fdel=None, doc=None)
    # Returns property object or property attribute.
    age = property(get_age, set_age, del_age, "This is the docstring of property attribute. By default, it will be the docstring of the getter method.")


dog = Dog(5)
print(dog.age)
dog.age = 2
print(dog.age)
dog.age = -6 # Invalid age
print(dog.age)
del dog.age
# print(dog.age) # AttributeError: 'Dog' object has no attribute '_age'
# print(dog._age) # AttributeError: 'Dog' object has no attribute '_age'

# NOTE: When we define a property in Python, we can use the same syntax to access and modify the attributes just as they were public attributes. But we are still using the intermediaries such as Getter, Setter and Deleter. The getter, setter and deleter will be called behind the scenes for their corresponding operation.

# Go to decorators.py
