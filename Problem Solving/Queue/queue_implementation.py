class Queue:

	def __init__(self, capacity=None):
		self._queue = []
		if capacity is not None and capacity < 0:
			self._capacity = 0
		else:
			self._capacity = capacity

	@property
	def capacity(self):
		return self._capacity

	@property
	def size(self):
		return len(self._queue)

	def is_empty(self):
		return len(self._queue) == 0

	def is_full(self):
		if self.capacity is None:
			return False
		else:
			return self.size == self.capacity

	@property
	def back(self):
		return len(self._queue) - 1

	@property
	def front(self):
		if self.is_empty():
			return -1
		else:
			return 0

	def display(self):
		print(self._queue)

	def enqueue(self, ele):
		if not self.is_full():
			self._queue.append(ele)
		else:
			print("Error: Queue is full")

	def dequeue(self):
		if not self.is_empty():
			return self._queue.pop(0)
		else:
			return "Error: Queue is empty"

	def peek(self):
		if not self.is_empty():
			return self._queue[0]
		else:
			return "Error: Queue is empty"


print("Queue Implementation:")
queue = Queue(capacity=2)
print(queue.capacity)
print(queue.size)
print(queue.front)
print(queue.back)
print(queue.is_empty())
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.display()
print(queue.is_full())
print(queue.peek())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
queue.display()

print("Queue in Python:")
queue = []
print(len(queue))  # size
print(len(queue) == 0)  # is_empty
if len(queue) == 0:  # front
	print(-1)
else:
	print(0)
print(len(queue)-1)  # back
queue.append(1)  # enqueue
queue.append(2)
queue.append(3)
print(queue)  # display
print(queue[0])  # peek without exception handling
print(queue.pop(0))  # dequeue
print(queue.pop(0))
print(queue.pop(0))
print(queue)  # display

# Time complexity for enqueue, dequeue, peek --> O(1)
# Space complexity for queue --> O(n)
