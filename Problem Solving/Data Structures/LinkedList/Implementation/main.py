# LinkedList:
# - A linear collection of data elements where each element(node) points to the next one.
# - Head: The first node of the linkedlist.
# - Tail: The last node of the linkedlist.

# 2 types of LinkedList:
# - 1. Singly LinkedList
# - 2. Doubly LinkedList

# Advantages of LinkedList:
# - The elements(nodes) can be easily inserted and removed just by updating the pointers.
# - They are dynamic, so their length can increase or decrease as needed.

# # Disadvantages of LinkedList:
# - They take more memory than arrays because they need to store references to other nodes.
# - Nodes must be read linearly in the order that they are stored in the data structure.

from linked_list import LinkedList


my_linked_list = LinkedList()

my_linked_list.insert_node("Python")
my_linked_list.insert_node("World")
my_linked_list.insert_node("Hi")
my_linked_list.insert_node("Hello")
my_linked_list.insert_node("Code")

my_linked_list.show()
print(f"nodes_count_iterative: {my_linked_list.nodes_count_iterative()}")
print(f"nodes_count_recursive_wrapper: {my_linked_list.nodes_count_recursive_wrapper()}")

values = ['Python', 'Golang']
for value in values:
	print(f"is_exists {value}: {my_linked_list.is_exists(value)}")

values = ['Code', 'Golang', 'Hi', 'World']
my_linked_list.show()
for value in values:
	print(f"delete_node {value} : {my_linked_list.delete_node(value)}")
my_linked_list.show()

my_linked_list.show_reversed_recursive_wrapper()
