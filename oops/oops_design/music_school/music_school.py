import os


class MusicSchool:

	_students = {}
	_students_file_path = os.path.join(os.path.dirname(__file__), "students_data.txt")
	_is_students_file_created = False

	def __init__(self, working_hours, revenue):
		self.working_hours = working_hours
		self.revenue = revenue

		if not MusicSchool._is_students_file_created:
			MusicSchool.create_students_file()

	@classmethod
	def get_student_info_string(cls, student_name):
		student_info = cls._students[student_name]
		student_age = student_info[0]
		student_classes = student_info[2]

		student_info_string = f"\"Student: {student_name} who is {student_age} years old and is taking {student_classes}\""

		return student_info_string

	@classmethod
	def print_student(cls, student_name):
		print(cls.get_student_info_string(student_name))

	@classmethod
	def print_students_data(cls):
		for student_name in cls._students:
			cls.print_student(student_name)

	@classmethod	
	def add_student(cls, student_name, student_data):
		cls._students[student_name] = student_data
		cls.store_student(student_name)

	@classmethod
	def create_students_file(cls):
		file_mode = "w"

		# fd --> file descriptor or file object.
		# File Object: An object exposing a file-oriented API (with methods such as read() or write()) to an underlying resource (Ex: a file).

		# 2 ways to work with a file:

		# 1. Normal way: Explicitly close the fd object or a file.
		# fd = open(cls._students_file_path, file_mode)
		# fd.write("")
		# fd.close()

		# 2. Using Context Managers:
		# Context Managers are Python constructs that will make your life much easier. By using them, you don't need to remember to close a file at the end of your program and you have access to the file in the particular part of the program that you choose.
		with open(cls._students_file_path, file_mode) as fd:
			fd.write("")

		cls._is_students_file_created = True
		print(f"students_data.txt file path: {cls._students_file_path}")

	@classmethod
	def store_student(cls, student_name):
		file_mode = "a"

		with open(cls._students_file_path, file_mode) as fd:
			fd.write(cls.get_student_info_string(student_name) + "\n")


headquarter_1 = MusicSchool(8, 15000)
MusicSchool.print_students_data()
MusicSchool.add_student("Gino", [15, "653-235-345", ["Piano", "Guitar"]])
MusicSchool.add_student("Talina", [28, "555-765-452", ["Cello"]])
MusicSchool.add_student("Eric", [12, "583-356-223", ["Singing"]])
MusicSchool.print_students_data()

print()

headquarter_2 = MusicSchool(8, 20000)
MusicSchool.add_student("Jack", [60, "562-234-234", ["Piano"]])
MusicSchool.print_students_data()
