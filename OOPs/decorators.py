# Decorator:
# A function that takes a function as an argument and extends it's behaviour without explicitly modifying it.
# That's why we call it as decorator. It's sort of like decorating another function by extending it's behaviour. But it doesn't explicitly modify the function. It just adds extra flavour or functionality to the function.

# Typical syntax of a decorator function:
def decorator_function(arg_function):
	def wrapper_function():
		# Code to extend the functionality 
		arg_function()
		# Code to extend the functionality
	return wrapper_function

# @property decorator:
# Advantages of @property decorator in comparison with property() class.
# - Syntax is cleaner and more compact.
# - Easier to read and understand.
# - Avoids calling property() directly.
# - We will reuse the name of the property. So we avoid adding new names like name of the getter and name of the setter to our list of valid names in the class. (i.e., get_<attribute>, set_<attribute>).

class Dog:
    def __init__(self, age):
        self._age = age

    # age property
    # Getter
    @property
    def age(self):
        return self._age

    # Setter
    @age.setter
    def age(self, age):
        if isinstance(age, int) and 0 < age <= 30:
            self._age = age
        else:
            print("Invalid age")

    # Deleter
    @age.deleter
    def age(self):
        del self._age


dog = Dog(10)
print(dog.age)
dog.age = 5
print(dog.age)
dog.age = 35
print(dog.age)
del dog.age
# print(dog.age) # AttributeError: 'Dog' object has no attribute '_age'
