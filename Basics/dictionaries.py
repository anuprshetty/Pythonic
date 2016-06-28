# Associative arrays, also called maps or dictionaries, are an abstract data type that can hold data in (key, value) pairs.
# Dictionary element --> (key, value)
# Keys should be unique
# Keys can be any Hashable types such as string, int.
# In addition to dictionary elements, dictionary data structure maintain an additional index table.
# Index table contains 2 things:
# 1. Keys which are sorted (Indeces) --> We can apply binary search on these keys (O(logn)). Efficient searching.
# 2. Memory addresses for the corresponding dictionary elements.
friends_ages = {"Anup": 24, "Ram": 35}
print(friends_ages)
print(friends_ages["Anup"])
# Add an element
friends_ages["Bob"] = 22
# Update an element
friends_ages["Ram"] = 30
print(friends_ages)

for key in friends_ages:
    print(f"{key} : {friends_ages[key]}")

# Dictionary object has view objects.
# Dictionary methods items(), keys() and values() return view objects.
print(friends_ages.items()) # dict_items([('Anup', 24), ('Ram', 30), ('Bob', 22)])
print(friends_ages.keys()) # dict_keys(['Anup', 'Ram', 'Bob'])
print(friends_ages.values()) # dict_values([24, 30, 22])

for (key, value) in friends_ages.items():
    print(f"{key} : {value}")

# NOTE: You can't directly edit views. Instead, you can still edit the dictionary, and the views reflect your changes immediately.

if "Anup" in friends_ages: # Check whether Anup key present in the dictionary or not.
    print(f"Anup --> {friends_ages['Anup']}")

if "Anup" in friends_ages.keys(): # Check whether Anup key present in the dictionary or not.
    print(f"Anup --> {friends_ages['Anup']}")
