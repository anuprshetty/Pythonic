nums = [1, 2, 3]

# help(obj) method: To get the help for an obj.
print(help(nums))

# dir(obj) method: To get the list of attributes and methods of an obj.
print(dir(nums))

# pass keyword in Python:
# - A null statement, a statement that will do nothing
# - The pass statement is used as a placeholder for future code.
# - When the pass statement is executed, nothing happens, but you avoid getting an error when empty code is not allowed.
# - Empty code is not allowed in loops, function definitions, class definitions, or in if statements.

print("\npass_keyword_demo:")


def pass_keyword_demo():

	print("This will be printed")
	pass
	print("This will ALSO be printed")


pass_keyword_demo()
