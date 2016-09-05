# Abstract Class and Abstract Method:
# - By default, Python don't support abstract classes and abstract Methods.
# - We need to use 'abc' module to achieve abstract classes.
# - abc --> Abstract Base Class
# -- Abstract class will have at least one abstract method.
# -- A method without body (no implementation) is known as abstract method.
# -- We can't instantiate abstract class.
# -- All the classes which are inheriting abstract class should implement all the abstract methods declared in abstract class.

from abc import ABC, abstractmethod


class IDE(ABC):

	@abstractmethod
	def execute(self):
		pass


class PyCharm(IDE):

	def execute(self):
		print("Compiling ...")
		print("Running ...")


class VSCode(IDE):

	def execute(self):
		print("Spell checking ...")
		print("Convention checking ...")
		print("Compiling ...")
		print("Running ...")


class Laptop:

	def code(self, ide):  # Here ide object is a duck. Because all we care about is an object (i.e., ide) which has a method execute().
		ide.execute()


print("PyCharm:")
py_charm_ide = PyCharm()
laptop = Laptop()
laptop.code(py_charm_ide)

print()

print("VSCode:")
vs_code_ide = VSCode()
laptop = Laptop()
laptop.code(vs_code_ide)

# NOTE:
# - Here ide object is a duck. Because all we care about is an object (i.e., ide) which has a method execute().
# - We are not concerned about which class that object belongs to. We are only concerned about whether that object has a method execute() or not. That is called Duck Typing.
# - Duck Typing in Python analogous to interfaces in C# or Java.
# -- Here IDE class acts like interface or abstract base class.
# -- PyCharm and VSCode classes act like implementation.
