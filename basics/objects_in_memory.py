# Objects in Memory: How objects work behind the scenes?

# - Programs keep track of how many "references" to the object exist.
# - Reference: Name that refers to the location in memory (i.e., id()) of an object.
# - Example references include variables, attributes, items in any data structures, etc.
# - Variables in Python store references to objects in memory.
# NOTE: When there are no references to the object in the program, the object is deleted from memory --> This process is called "Garbage Collection".

# Object vs Instance:
# - There is a very subtle difference between these terms, and they are often used interchangeable.
# - But you can think of objects as the "physical" existence of the instances in memory, the data that is stored in memory to represent the instances, while instances represent a more theoretical concept.
# - A specific house object represents an instance of the House class in memory.

# Comparing Objects of User-Defined Classes with == operator:
# - Objects created from user-defined classes have to meet two conditions for the expression obj1 == obj2 to evaluate to True.
# -- They have to refer to the same object (obj1 is obj2 has to evaluate to True)
# -- The expression hash(obj1) == hash(obj2) has to evaluate to True
# NOTE:
# - The hash() function maps the object to a unique integer.
# - User-defined classes have __eq__() and __hash__() methods by default; with them, all objects compare unequal (except with themselves) and x.__hash__() returns an appropriate value such that x == y implies both that x is y and hash(x) == hash(y).


class Dog:

    def __init__(self, age):
        self.age = age


a = Dog(5)
b = Dog(5)
print(f"hash of a: {hash(a)}")  # Not Equal
print(f"hash of b: {hash(b)}")  # Not Equal
print(a == a)  # True
print(b == b)  # True
print(a == b)  # False
b = a
print(f"hash of a: {hash(a)}")  # Equal
print(f"hash of b: {hash(b)}")  # Equal
print(a == b)  # True
