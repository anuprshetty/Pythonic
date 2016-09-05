class Student:

	def __init__(self, id, name, marks, laptop):
		self.id = id
		self.name = name
		self.marks = marks
		self.laptop = laptop

	def show(self):
		print(f"{self.id} {self.name} {self.marks}")
		self.laptop.show()

	class Laptop:

		def __init__(self, brand, hdd):
			self.brand = brand
			self.hdd = hdd

		def show(self):
			print(f"{self.brand} {self.hdd}")


laptop = Student.Laptop("HP", "1TB")
student = Student("1", "Anup", "86", laptop)
student.show()
