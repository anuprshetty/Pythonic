# Alias:
# - Alias in real world: Used to indicate an additional name that a person sometimes uses.
# - Alias in programming world: Two or more references to the same memory address in the program. 
a = [3, 5, 6]
b = a # Aliasing --> a, b are aliases. 
# Disadvantages:
# - We might mutate an object unintentionally through an alias. 


# Mutation:

# Mutable Objects:
# Advantages:
# - Memory efficient. Because reuse existing objects instead of making new copies for each change.
# - Helpful to represent real-world objects that are mutable by nature.
# Disadvantages:
# - Using mutable objects in a program might introduce bugs. Because you might unintentionally mutate an object in the program. 

# Immutable Objects:
# Advantages:
# - Safer from bugs. Since they can't be modified, they are less likely to introduce bugs. 
# - Easier to understand. Because we know their exact value, without any hidden or unexpected changes. 
# Disadvantages:
# - Less efficient. Because you need to create a new copy of the object to make any changes, which can be costly. 
a = (1, 2, 3, 4)
print(a) # (1, 2, 3, 4)
print(id(a)) # Not Equal
# tupple a = tupple a[:2] + tupple (7, ) + tupple a[2:]
a = a[:2] + (7, ) + a[2:]
print(a) # (1, 2, 7, 3, 4)
print(id(a)) # Not Equal

# Common bugs in mutation:
# 1. Deleting dictionary elements
def remove_even_values(dictionary):
    for key, value in dictionary.items(): # RuntimeError: dictionary changed size during iteration
        if value % 2 == 0:
            del dictionary[key]

dictionary = {"1": 1, "2": 2, "3": 3, "4": 4}
# remove_even_values(dictionary)

# 2. Be careful with Mutable Data Types as Default Arguments
# why you should avoid using mutable data types such as lists as default arguments?
# - Default arguments are initialized when the methods are initially processed, so there is only one copy of each default argument. 
# - They are not created when you call the method, they are created when the program starts to run.


# Cloning:
# Cloning is creating an exact copy of the object that is completely independent from the original object. 
a = [3, 5, 6]
b = a[:] # Cloning --> NOTE: Shallow Copy

# Common bugs in mutation solved by cloning:
# 1. Deleting dictionary elements
def remove_even_values(dictionary):
    for key, value in dictionary.copy().items(): # Cloning --> NOTE: Shallow Copy
        if value % 2 == 0:
            del dictionary[key]

dictionary = {"1": 1, "2": 2, "3": 3, "4": 4}
print(dictionary)
remove_even_values(dictionary)
print(dictionary)

# Shallow Copy vs Deep Copy of an Object (e.g. lists, tuples, dictionaries, custom objects, and others):

# Shallow Copy:
# - When you make a shallow copy of an object, you are making a new object in memory, a new reference, but the content of the object will still point to the same objects.
a = [2, 4, 5]
b = a[:] # Shallow Copy
dictionary = {"1": 1, "2": 2, "3": 3, "4": 4}
dictionary_copy = dictionary.copy() # Shallow Copy
import copy
x = [6, 7, 8]
y = copy.copy(x) # Shallow Copy

# Deep Copy:
# - With a deep copy, in addition to creating a copy of the "container" object, you also create a copy of the elements contained in the object.
x = [6, 7, 8]
y = copy.deepcopy(x) # Deep Copy
