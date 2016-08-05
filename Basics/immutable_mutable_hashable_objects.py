# In Python, everything is an object.
# 2 types of objects:
# 1. Immutable built-in objects: int, float, bool, string, tuple
# 2. Mutable built-in objects: list, set and dictionary.
# NOTE: Immutable objects can't be changed whereas mutable objects can. 

# id(obj) Function:
# - Return the “identity” of an object. 
# - This is an integer which is guaranteed to be unique and constant for this object during its lifetime. 
# NOTE: Two objects with non-overlapping lifetimes may have the same id() value.
# NOTE: CPython implementation detail: This is the address of the object in memory.

# Immutable Objects:
int_val = 100
print(type(int_val))
print(id(int_val))
int_val = 200 # Once the value changes, the old memory location is deleted by Python. And new memory location is created to store new value.
print(type(int_val))
print(id(int_val)) # Every time you change an immutable object, a new object is created with different ID.

str_val1 = "Anup"
print(type(str_val1)) # <class 'str'>
print(id(str_val1)) # 2363930470448
# str_val1[2] = "o" # TypeError: 'str' object does not support item assignment
str_val2 = str_val1
print(id(str_val2)) # 2363930470448
str_val1 = "Arun"
print(id(str_val1)) # 2363938851504
print(id(str_val2)) # 2363930470448


# Mutable Objects:
my_list = [1, 2, 4, 6]
print(type(my_list))
print(id(my_list)) # 1674851754880
my_list[2] = 8
print(id(my_list)) # 1674851754880


# Hashable Objects:
# An object is hashable if it has a hash value which never changes during it's lifetime.
# Every immutable object has __hash__() which gives hash value for that immutable object.
print("Hashable Objects: ")
print(int_val.__hash__()) # 200
print(str_val1.__hash__()) # -3543439955247231470
print(str_val2.__hash__()) # 4622815410798504814
# Mutable objects don't have hash.
# print(my_list.__hash__()) # TypeError: 'NoneType' object is not callable

# IMPORTANT:
# Tuples are Immutable objects.
# But Tuples are Hashable if and only if individual tuple elements are hashable.

# tuple elements are immutable
tuple1 = (1, 3, 5)
print(tuple1.__hash__()) # 5437428145492376519
# tuple elements are mutable
tuple2 = (3, [5, 6], 8)
# print(tuple2.__hash__()) # TypeError: unhashable type: 'list'

# NOTE: We can modify mutable objects inside the immutable object.
print(tuple2) # (3, [5, 6], 8)
tuple2[1].append(77)
tuple2[1][0] = 10
print(tuple2) # (3, [10, 6, 77], 8)

# Dictionary is sorted based on Keys. So faster searching (Binary search O(logn)).
# Dictionary is hash table. Time complexity for search --> O(1).
# Immutable objects are hashable.
# Always Hashable objects are used as dictionary keys.
my_dict = {
    1 : "int",
    3.5: "float",
    False: "bool",
    "string": "a string",
    (3, 5, 6): "a tuple",
    # a mutable object (List) is inside an immutable object (Tuple).
    # So it's not hashable. Thereby it can't be a dictionary key.
    # (3, [5, 9], 6): "a tuple containing a list" # TypeError: unhashable type: 'list'
}
print(type(my_dict)) # <class 'dict'>
print(my_dict)