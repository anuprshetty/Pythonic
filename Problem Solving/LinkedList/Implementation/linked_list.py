from node import Node


class LinkedList:

	def __init__(self):
		self.head = None

	# Assumption: elements are inserted to linkedlist in ascending order.
	def insert_node(self, value):
		new_node = Node(value)

		# Insert a node at the beginning of the linkedlist.
		if self.head is None:
			self.head = new_node
		elif value <= self.head.value:
			new_node.next = self.head
			self.head = new_node
		# Insert a node at the middle or end of the linkedlist.
		else:
			prev = self.head
			runner = self.head.next
			while (runner is not None) and (value > runner.value):
				prev = runner
				runner = runner.next

			prev.next = new_node
			new_node.next = runner

	# Traversing in CS: To visit every element in the data structure and doing something with the data.
	def show(self):
		print("LinkedList: ", end="")
		if self.head is None:
			print()
			return

		runner = self.head
		while True:
			print(f"{runner.value}", end="")
			runner = runner.next
			if runner is not None:
				print(" -> ", end="")
			else:
				print()
				break

	def nodes_count_iterative(self):
		count = 0
		runner = self.head

		while runner is not None:
			count += 1
			runner = runner.next

		return count

	def nodes_count_recursive_wrapper(self):
		return self.nodes_count_recursive(self.head)

	def nodes_count_recursive(self, start_node):
		if start_node is None:
			return 0
		else:
			return 1 + self.nodes_count_recursive(start_node.next)

	def is_exists(self, search_value):
		runner = self.head

		while runner is not None:
			if runner.value == search_value:
				return True
			else:
				runner = runner.next

		return False

	def delete_node(self, value):
		# Delete the node at the beginning of the linkedlist.
		if self.head is None:
			pass
		elif self.head.value == value:
			self.head = self.head.next
		# Delete the node at the middle or end of the linkedlist.
		else:
			prev = self.head
			runner = self.head.next

			while (runner is not None) and (value > runner.value):
				prev = runner
				runner = runner.next

			if (runner is not None) and (value == runner.value):
				prev.next = runner.next

		return value

	def show_reversed_recursive_wrapper(self):
		print("LinkedList Reversed: ", end="")
		self.show_reversed_recursive(self.head)

	def show_reversed_recursive(self, start_node):
		if start_node is not None:
			self.show_reversed_recursive(start_node.next)
			if start_node.next is None:
				print(f"{start_node.value}", end="")
			else:
				print(f" -> {start_node.value}", end="")
