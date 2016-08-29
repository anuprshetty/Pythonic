# Context Manager:
# - Context manager allows us to properly manage resources so that we can specify what exactly we want to set up and tear down when working with certain objects.


# class based context manager
class OpenFile:

	def __init__(self, filename, mode):
		print("Inside __init__")
		self.filename = filename
		self.mode = mode

	# setup of context manager
	def __enter__(self):
		print("Inside __enter__")
		self.file = open(self.filename, self.mode)

		return self.file

	# teardown of context manager
	# Parameters:
	# - exc_type --> exception_type
	# - exc_val --> exception_value
	# - exc_tb --> exception_traceback
	# If an exception occurs, then we can use these parameters to access that exception info.
	def __exit__(self, exc_type, exc_val, exc_tb):
		print("Inside __exit__")
		self.file.close()


print("class based context manager:")
# Using custom context manager:
with OpenFile('class_based_context_manager_log.txt', 'w') as fd:
	fd.write('Testing class based custom context manager')

print(f"is file closed: {fd.closed}")  # True

print()
print("function based context manager: (Using decorator and generator)")

from contextlib import contextmanager


@contextmanager
def open_file(filename, mode):
	try:
		# setup of context manager
		fd = open(filename, mode)
		yield fd
	finally:
		# teardown of context manager
		fd.close()


with open_file('function_based_context_manager_log.txt', 'w') as fd:
	fd.write('Testing function based custom context manager')

print(f"is file closed: {fd.closed}")  # True
