# 3 different collections that allow to store multiple values in a signle variable.
# List
# Heterogeneous Data Structure - Elements CAN BE of different data types.
# Mutable - We can modify (Add, Remove)
# Can have duplicate values
# Keep the order of the elements
l = ["Anup", 34, 6.7]
# Tuple
# Heterogeneous Data Structure - Elements CAN BE of different data types.
# Immutable - We can not modify (Add, Remove)
# Can have duplicate values
# Keep the order of the elements
t = ("Ram", 56, 2.5) 
# Set
# Heterogeneous Data Structure - Elements CAN BE of different data types.
# Mutable - We can modify (Add, Remove)
# Can NOT have duplicate values
# DON'T Keep the order of the elements. Order is not guaranteed. Order can change at any moment.
s = {"Bob", 45, 9.6} 


print(l)
print(t)
print(s)


# Accessing List and Tuple elements.
# By using Subscript Notation
print(l[0])
print(t[1])


# List Operations.
# Update List elements.
# By using Subscript Notation
l[1] = 20
print(l)
# Add elements to list
l.append("Anup")
print(l)
l.remove("Anup") # removes only first occurrence.
print(l)


# Set Operations.
print(s)
s.add("Alice")
print(s)
s.add("Alice") # If you try to add an existing element one more time, set will ignore that element and it won't throw an error.
print(s)
s.discard("Bob") # Removes the element from the set.
print(s)
s.discard("Bob") # discard() function don't throw an error if the element to be removed is not present in the set.
print(s)

# Advanced set operations.
friends = {"Anup", "Ram", "Sham", "Bob", "Alice"}
abroad_friends = {"Anup", "Sham"}
# set difference
local_friends = friends.difference(abroad_friends)
# set union
friends = local_friends.union(abroad_friends)
print(friends)
print(abroad_friends)
print(local_friends)

art = {"Anup", "Ram", "Sham"}
science = {"Anup", "Sham", "Bob", "Alice"}
# set intersection
art_science = art.intersection(science)
print(art)
print(science)
print(art_science)

# Set symmetric_difference
# The symmetric difference of two sets A and B is the set of elements that are in either A or B, but not in their intersection.
a_set = {1, 2, 4, 8}
b_set = {4, 5, 8, 9, 7}
elements_in_a_or_b_but_not_in_both = a_set.symmetric_difference(b_set)
print(a_set)
print(b_set)
print(elements_in_a_or_b_but_not_in_both) # {1, 2, 5, 7, 9}


# Empty set
# Empty set creation
empty_set = set()
print(empty_set) # Prints an empty set. i.e., set()

var = 2
print(var) # 2
print(type(var)) # <class 'int'>
var = 2,
print(var) # (2,)
print(type(var)) # <class 'tuple'>
var = (2)
print(var) # 2
print(type(var)) # <class 'int'>
var = (2,)
print(var) # (2,)
print(type(var)) # <class 'tuple'>
var = 2, 44
print(var) # (2, 44)
print(type(var)) # <class 'tuple'>
