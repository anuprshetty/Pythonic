# For primitive data types like int, float, string (Value based)
# == AND != --> Compares values
# is AND is not--> Compares objects OR memory location(id())
# NOTE: 
# - If two variables do not reference the same object, then they will have different ids.  OR
# - If two variables reference the same object, then they will have the same id. 

# Python internal memory management:
# If a set of variables have same value, then all the variables points to same memory location until the value of one of the variable changes to something else.
# Once a value of one of the variable changes, Python creates a seperate memory location to store the changed value and that variable now points to newly created memory location.
# Python does this to save some memory and avoid duplicate copies of the same value.
print("Strings")
name1 = "Anup"
name2 = "Anup"
name3 = "Anup"
# NOTE: String Interning: The process of keeping only one distinct copy of the string in memory. 
print(name1 == name2 == name3) # True
print(name1 is name2 is name3) # True
name2 = name1
print(name1 == name2) # True
print(name1 is name2) # True
name2 = "Ram"
print(name1 == name2) # False
print(name1 is name2) # False
# For non-primitive data types like list, tuple, set (Reference based)
# == --> Compares values
# is --> Compares objects OR memory location
print("Lists")
list1 = ["Anup", "Ram"]
list2 = ["Anup", "Ram"]
print(list1 == list2) # True
print(list1 is list2) # False
list2.append("Alice")
print(list1 == list2) # False
print(list1 is list2) # False
list2 = list1
print(list1 == list2) # True
print(list1 is list2) # True
list2.append("Bob")
print(list1 == list2) # True
print(list1 is list2) # True

# The "is" operator --> Unexpected results:
a = 3
b = 3
print(a is b) # True
# Why?
# Python Documetantion: The current implementation keeps an array of integer objects for all integers between -5 and 256, when you create an int in that range you actually just get back a reference to the existing object.
# NOTE: These memory optimizations completely depends on the Python interpreter we are using. Some interpreters optimize all the integer ranges not only the range between -5 and 256.
