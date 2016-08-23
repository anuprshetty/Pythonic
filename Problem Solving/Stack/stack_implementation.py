class Stack:

	def __init__(self, capacity=None):
		self._stack = []
		if capacity is not None and capacity < 0:
			self._capacity = 0
		else:
			self._capacity = capacity

	def push(self, ele):
		if self.capacity() is not None:
			if self.size() < self.capacity():
				self._stack.append(ele)
			else:
				print("Error: Stack is full")
		else:
			self._stack.append(ele)

	def pop(self):
		try:
			ele = self._stack.pop()
		except IndexError:
			return "Error: Stack is empty"
		return ele

	def peek(self):
		try:
			ele = self._stack[-1]
		except IndexError:
			return "Error: Stack is empty"
		return ele

	def capacity(self):
		return self._capacity

	def size(self):
		return len(self._stack)

	def top(self):
		return len(self._stack) - 1

	def is_empty(self):
		return len(self._stack) == 0

	def is_full(self):
		if self.capacity() is None:
			return False
		else:
			return self.size() == self.capacity()

	def display(self):
		print(self._stack)


print("Stack Implementation:")
stack = Stack(capacity=2)
print(stack.capacity())
print(stack.size())
print(stack.top())
stack.push(1)
stack.push(2)
stack.push(3)
stack.display()
print(stack.peek())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.is_empty())
stack.display()

print("Stack in Python:")
stack = []  # capacity is infinite
print(len(stack))  # size
print(len(stack)-1)  # top
stack.append(1)  # push
stack.append(2)
stack.append(3)
print(stack)
print(stack[-1])  # peek without exception handling
print(stack.pop())  # pop without exception handling
print(stack.pop())
print(stack.pop())
print(len(stack) == 0)  # is_empty
print(stack)

# Time complexity for push, pop, peek --> O(1)
# Space complexity for stack --> O(n)
