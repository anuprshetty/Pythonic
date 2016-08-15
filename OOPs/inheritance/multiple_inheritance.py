# Method Resolution Order (MRO):
# - MRO is a concept used in inheritance.
# - It is the order in which a method is searched for in a classes hierarchy and is especially useful in Python because Python supports multiple inheritance.

# NOTE: Python follows C3 super-class linearization Algorithm for MRO. Please refer below C3 super-class linearization Algorithm.


class Programmer:

	code = 1
	id = "Programmer"
	skill = "Coding"

	def __init__(self, programmer_score):
		self.programmer_score = programmer_score

	def display(self):
		print(f"I am a {self.id} with score {self.programmer_score}")

	def who_am_i(self):
		print(f"I am an {self.id}")

	def get_skill(self):
		print(f"My skill is {self.skill}")


class Athlete:

	code = 2
	id = "Athlete"

	def __init__(self, athlete_score):
		self.athlete_score = athlete_score

	def display(self):
		print(f"I am an {self.id} with score {self.athlete_score}")

	def who_am_i(self):
		print(f"I am an {self.id}")


# NOTE: Athlete is the immediate superclass of Student class.
class Student(Athlete, Programmer):

	code = 3

	def __init__(self, student_score, athlete_score, programmer_score):
		Athlete.__init__(self, athlete_score)  # Same as --> super().__init__(athlete_score)
		Programmer.__init__(self, programmer_score)

		self.student_score = student_score

		print("Inside of __init__() method:")
		self.display()
		Athlete.display(self)  # Same as --> super().display()
		Programmer.display(self)

	def display(self):
		print(f"I am a Student with score {self.student_score}")


student = Student(30, 20, 10)

print()
# print(f"MRO: {Student.__mro__}")  # Type is tuple
print(f"MRO: {Student.mro()}")  # Type is list
# MRO: [<class '__main__.Student'>, <class '__main__.Athlete'>, <class '__main__.Programmer'>, <class 'object'>]
print()

print("Outside of class:")
student.display()
student.who_am_i()
student.get_skill()
# student.unknown_method()  # AttributeError: 'Student' object has no attribute 'unknown_method'


print("\nMRO In Action:")

# Short History on MRO in Python:
# - Old style class in Python: By default, class that WON'T INHERIT from Python root ‘object’ class.
# - New style class in Python: By default, class that INHERITS from Python root ‘object’ class.
# - Old style class inheritance follows DLR (Depth-first Left to Right) algorithm for MRO.
# - New style class inheritance follows C3 super-class linearization algorithm for MRO.
# - Till Python 2.2, only Old style classes were there. (follows DLR (Depth-first Left to Right) algorithm)
# - People found some inconsistencies with DLR (Depth-first Left to Right) algorithm which is used for Old style class inheritance.
# - So they came up with C3 super-class linearization algorithm which is used for New style class inheritance.
# - In Python 2.2, New style classes were introduced. (follows C3 super-class linearization algorithm)
# - But Python 2.2 is still compatible with Old style classes (follows DLR (Depth-first Left to Right) algorithm).
# - But Python 3, it only supports New style classes (follows C3 super-class linearization algorithm). It won't support Old style classes.

# C3 super-class linearization Algorithm:
# - C3 superclass linearization is an algorithm used primarily to obtain the order in which methods should be inherited in the presence of multiple inheritance.
# - In other words, the output of C3 superclass linearization is a deterministic Method Resolution Order (MRO).

# NOTE: Basically, the idea behind C3 is that if you write down all of the ordering rules imposed by inheritance relationships in a complex class hierarchy, the algorithm will determine a monotonic ordering of the classes that satisfies all of them. If such an ordering can not be determined, the algorithm will fail.

# - C3 superclass linearization is called C3 because it "is consistent with three properties":
# 1. a consistent extended precedence graph,
# 2. preservation of local precedence order, and
# 3. fitting a monotonicity criterion.

# For detailed explanation of internal working of MRO in Python and C3 superclass linearization algorithm,
# - https://www.python.org/download/releases/2.3/mro/

# Example demonstrating working of C3 superclass linearization algorithm for MRO in Python:


class A:
	# def method(self):
	# 	print(f"Inside class: A")
	pass


class B:
	# def method(self):
	# 	print(f"Inside class: B")
	pass


class C(A, B):
	# def method(self):
	# 	print(f"Inside class: C")
	pass


class D(B):
	def method(self):
		print(f"Inside class: D")
	# pass


class E(C, D):
	# def method(self):
	# 	print(f"Inside class: E")
	pass


print(f"MRO: {E.mro()}")
# MRO: [<class '__main__.E'>, <class '__main__.C'>, <class '__main__.A'>, <class '__main__.D'>, <class '__main__.B'>, <class 'object'>]
e = E()
e.method()  # Inside class: D


# Example demonstrating EXCEPTION with C3 superclass linearization algorithm for MRO in Python:


class X:
	pass


class Y(X):
	pass


# class Z(X, Y):  # TypeError: Cannot create a consistent method resolution order (MRO) for bases X, Y
# 	pass
