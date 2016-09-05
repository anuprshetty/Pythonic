# Operator Overloading:
# - Overloading is an example of compile-time polymorphism.

a = 5
b = 3

print("Addition:")
print(a + b)  # Operator Overloading
print("Behind the scenes:")
print(int.__add__(a, b))

a = '5'
b = '3'

print("Concatenation:")
print(a + b)  # Operator Overloading
print("Behind the scenes:")
print(str.__add__(a, b))


print("Operator Overloading:")
# - Whenever we perform any operation with objects using an operator in Python, the corresponding magic method will be called behind the scenes on those objects.
# - The type of operands will change on the same operator. Based on the type of operands, the operation of the operator will change. That is called operator overloading.


class Student:

	def __init__(self, m1, m2):
		self.m1 = m1
		self.m2 = m2

	def __add__(self, other):  # Overloading + operator.
		m1 = self.m1 + other.m1
		m2 = self.m2 + other.m2

		return Student(m1, m2)

	def __str__(self):
		return f"{self.m1} {self.m2}"


s1 = Student(35, 50)
s2 = Student(40, 27)
print(s1)
print(s2)

# Operator Overloading
s3 = s1 + s2  # s3 = Student.__add__(s1, s2)

print(s3)
