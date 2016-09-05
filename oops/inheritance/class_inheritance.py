# Default Inheritance: The 'object' class is the parent class of all the classes in Python by default. 

# Inheritance:
# - Inheritance involves defining classes that inherit attributes and methods from other classes.
# - Inheritance helps us to follow the principle of DRY - Don't Repeat Yourself - A software development principle that aims to reduce code repetition. 
# - Classes usually inherit from more general classes that represent more abstract concepts. 
# - We add common functionalities in the parent class. 
# - We add specific functionalities in the child class. OR We customize the existing functionalities from parent class in the child class. 
# - A class can inherit from multiple classes (Multiple Inheritance) AND multiple classes can inherit from the same class (Hierarchical Inheritance). 

# Advantages of Inheritance:
# - Reduce code repetition.
# - Reuse code
# - Improve readability

# Inheritance Terminologies:
# Parent Class (Superclass):
# - The class from which other classes inherit attributes and methods (e.g. Dog).
# Child Class (Subclass):
# - The class that inherits attributes and methods from another class (e.g. Poodle and Schnauzer).


# Scenario-1: If you don't define subclass constructor (__init__() method), then by default, superclass constructor (__init__() method) will be called at the time of subclass instance/object creation and the attributes of superclass are inherited automatically. 
class Polygon1:

    def __init__(self, num_sides, color="Green"):
        self.num_sides = num_sides
        self.color = color


class Triangle1(Polygon1):
    pass


print("Scenario-1:")
triangle1 = Triangle1(3)
print(triangle1.num_sides)  # 3
print(triangle1.color)  # Green
print()


# Scenario-2: If you define subclass constructor (__init__() method), then superclass constructor (__init__() method) should be called explicitly in the subclass constructor (__init__() method). Only then the attributes of superclass are inherited. 
class Polygon2a:

    def __init__(self, num_sides, color):
        self.num_sides = num_sides
        self.color = color


class Triangle2a(Polygon2a):
    
    def __init__(self, base, height):
        # superclass constructor (__init__() method) not called explicitly.
        self.base = base
        self.height = height


print("Scenario-2-a:")
triangle2a = Triangle2a(base=6, height=10)
print(triangle2a.base)  # 6
print(triangle2a.height)  # 10
# print(triangle2a.num_sides) # AttributeError: 'Triangle2a' object has no attribute 'num_sides'
print()


class Polygon2b:

    def __init__(self, num_sides, color):
        self.num_sides = num_sides
        self.color = color


class Triangle2b(Polygon2b):

    NUM_SIDES = 3
    
    def __init__(self, base, height, color):
        # 2 ways to call superclass constructor:
        # 1st way:
        # Syntax: <superclass>.__init__(self, <superclass_constructor_arguments>)
        # Polygon2b.__init__(self, Triangle2b.NUM_SIDES, color)
        # 2nd way:
        # Syntax: super().__init__(<superclass_constructor_arguments>)
        super().__init__(Triangle2b.NUM_SIDES, color)
        self.base = base
        self.height = height


print("Scenario-2-b:")
triangle2b = Triangle2b(6, 10, "Yellow")
print(triangle2b.base) # 6
print(triangle2b.height) # 10
print(triangle2b.num_sides) # 3
print(triangle2b.color) # Yellow
print()

# NOTE: 
# super(): 
# - This is a built-in Python function that is used to refer to the immediate parent class of the current class.
# - super() function returns a temporary object of the immediate parent class for the subclass.
# - In a class hierarchy with single inheritance, super can be used to refer to parent classes without naming them explicitly, thus making the code more maintainable. This use closely parallels the use of super in other programming languages.
