class Node:

	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right

	def dfs_preorder_recursive(self):
		print(f" {self.value} ", end="")
		if self.left:
			self.left.dfs_preorder_recursive()
		if self.right:
			self.right.dfs_preorder_recursive()

	def dfs_preorder_iterative(self):
		stack = [self]
		while stack:
			node = stack.pop()
			if node is None:
				continue
			print(f" {node.value} ", end="")
			if node.right:
				stack.append(node.right)
			if node.left:
				stack.append(node.left)

	def dfs_inorder_recursive(self):
		if self.left:
			self.left.dfs_inorder_recursive()
		print(f" {self.value} ", end="")
		if self.right:
			self.right.dfs_inorder_recursive()

	def dfs_inorder_iterative(self):
		stack = []
		node = self
		while True:
			while node:
				if node.right is not None:
					stack.append(node.right)
				stack.append(node)
				node = node.left

			node = stack.pop()
			print(f" {node.value} ", end="")
			if node.right is not None:
				node = stack.pop()
			else:
				node = None

			if node is None and not stack:
				break

	def dfs_postorder_recursive(self):
		if self.left:
			self.left.dfs_postorder_recursive()
		if self.right:
			self.right.dfs_postorder_recursive()
		print(f" {self.value} ", end="")

	def dfs_postorder_iterative(self):
		stack = []
		node = self
		while True:
			while node:
				if node.right is not None:
					stack.append(node.right)
				stack.append(node)
				node = node.left

			node = stack.pop()
			try:
				_ = stack[-1]
			except IndexError:
				print(f" {node.value} ", end="")
				node = None
			else:
				if node.right is not None and node.right is stack[-1]:
					stack.pop()
					stack.append(node)
					node = node.right
				else:
					print(f" {node.value} ", end="")
					node = None

			if node is None and not stack:
				break

	def bfs_levelorder_iterative(self):
		queue = [self]
		while queue:
			node = queue.pop(0)
			print(f" {node.value} ", end="")
			if node.left:
				queue.append(node.left)
			if node.right:
				queue.append(node.right)


# Binary Tree:
#             a
#            / \
#           b   c
#          / \   \
#         d   e   f

root = Node('a', Node('b', Node('d'), Node('e')), Node('c', None, Node('f')))
print("DFS: Using Stack")
print("Traversal with recursion:")
print("Pre-order Traversal:")
root.dfs_preorder_recursive()
print()
print("In-order Traversal:")
root.dfs_inorder_recursive()
print()
print("Post-order Traversal:")
root.dfs_postorder_recursive()
print()
print()
print("Traversal with iteration:")
print("Pre-order Traversal:")
root.dfs_preorder_iterative()
print()
print("In-order Traversal:")
root.dfs_inorder_iterative()
print()
print("Post-order Traversal:")
root.dfs_postorder_iterative()
print()
print()
print("BFS: Using Queue")
print("Level-order Traversal:")
root.bfs_levelorder_iterative()
print()
