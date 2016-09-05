# Function as decorator
def decorator_function(original_function):
	def wrapper_function(*args, **kwargs):
		print(f"Wrapper function displayed this before {original_function.__name__} function")
		return original_function(*args, **kwargs)

	return wrapper_function

# Example 1:

# This ...
# def display():
# 	print('display function ran')
#
#
# display = decorator_function(display)
# display()

# ... is same as this!


@decorator_function
def display():
	print('display function ran')


display()

# Example 2:


@decorator_function
def display_info(name, age):
	print(f"display_info function ran with arguments ({name}, {age})")


display_info("Anup", "24")

# Class as decorator


class DecoratorClass:

	def __init__(self, original_function):
		self.original_function = original_function

	def __call__(self, *args, **kwargs):
		print(f"__call__ function displayed this before {self.original_function.__name__} function")
		return self.original_function(*args, **kwargs)


# Example 1:

# This ...
# def display():
# 	print('display function ran')
#
#
# display = DecoratorClass(display)
# display()

# ... is same as this!


@DecoratorClass
def display():
	print('display function ran')


display()

# Example 2:


@DecoratorClass
def display_info(name, age):
	print(f"display_info function ran with arguments ({name}, {age})")


display_info("Anup", "24")
