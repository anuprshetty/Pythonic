numbers = [1, 4, 6]
doubled = [x * 2 for x in numbers]
print(numbers)
print(doubled)

friends = ["Anup", "Ram", "Sham", "Bob", "Alice"]
close_friends = [f for f in friends if f.endswith("am")]
print(friends)
print(close_friends)

list1 = [2, 4, 5]
list2 = [x for x in list1]
print(list1)
print(list2)
print(list1 == list2) # True
# The resultant list in list comprehension always points to newly created memory location even though it has same values of the source list. 
# The resultant list never points to source list memory location.
print(list1 is list2) # False

# NOTE: Displaying the memory address of the object using id() function.
print("list1: ", id(list1), "list2: ", id(list2))
