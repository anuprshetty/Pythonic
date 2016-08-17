# Duck Typing:
# - If there is a bird which is walking like a duck, quacking like a duck and swimming like a duck, then that bird is a duck.
# - It simply means, it doesn't matter if that bird is duck or not. What matters is the behavior of that bird, if it is matching with duck, then that's a duck.


class PyCharm:

	def execute(self):
		print("Compiling ...")
		print("Running ...")


class VSCode:

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
# -- Here ide object acts like interface.
# -- PyCharm and VSCode classes act like implementation.
