# For primitive data types like int, float, string (Value based)
# == --> Compares value
# is --> Compares both memory location and value
# Python internal memory management:
# If a set of variables have same value, then all the variables points to same memory location until the value of one of the variable changes to something else.
# Once a value of one of the variable changes, Python creates a seperate memory location to store the changed value and that variable now points to newly created memory location.
# Python does this to save some memory and avoid duplicate copies of the same value.
print("Strings")
name1 = "Anup"
name2 = "Anup"
print(name1 == name2) # True
print(name1 is name2) # True
name2 = name1
print(name1 == name2) # True
print(name1 is name2) # True
name2 = "Ram"
print(name1 == name2) # False
print(name1 is name2) # False
# For non-primitive data types like list, tuple, set (Reference based)
# == --> Compares values
# is --> Compares both memory location and values
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