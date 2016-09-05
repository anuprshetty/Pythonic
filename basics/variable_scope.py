# LEGB rule - Local, Enclosing, Global, Built-in

print("Before function:")
b = 'global b'
x = 'global x'
print(f"x: {x}")


def variable_scope(z):
	print("Inside function:")
	# print(f"a: {a}")  # NameError: name 'a' is not defined
	print(f"b: {b}")  # b: global b
	# print(f"c: {c}")  # UnboundLocalError: local variable 'c' referenced before assignment
	c = 'local c'
	print(f"z: {z}")
	y = 'local y'
	# x = 'local x'  # SyntaxError: name 'x' is assigned to before global declaration
	print(f"y: {y}")
	# print(f"x: {x}")  # SyntaxError: name 'x' is used prior to global declaration
	# NOTE: Names listed in a global statement must not be used in the same code block textually preceding that global statement.
	global x
	print(f"x: {x}")
	x = 'local x'
	print(f"y: {y}")
	print(f"x: {x}")


variable_scope('local z')
print("After function:")
# print(f"y: {y}") # NameError: name 'y' is not defined
print(f"x: {x}")


def no_global_var_declaration_1():
	global no_global_var
	# print(f"no_global_var: {no_global_var}")  # NameError: name 'no_global_var' is not defined
	# no_global_var += 1  # NameError: name 'no_global_var' is not defined
	no_global_var = 1


def no_global_var_declaration_2():
	global no_global_var
	no_global_var += 10


no_global_var_declaration_1()
no_global_var_declaration_2()
print(f"no_global_var: {no_global_var}")  # no_global_var: 11

print("Built-in scope:")
m = min([2, 4, 1, 6])  # Here min() function is in Built in scope.
print(f"m: {m}")
import builtins
print("Variables in built-in scope:")
print(dir(builtins))

print("Enclosing scope:")
p = 'global p'
q = 'global q'
r = 'global r'

i = 'global i'
j = 'global j'


def outer():
	p = 'outer p'
	q = 'outer q'

	i = 'outer i'

	def inner():
		p = 'inner p'

		nonlocal i  # Please see the NOTE below.
		i = 'inner i'

		global j
		j = 'inner j'

		print("inner scope:")
		print(f"p: {p}")
		print(f"q: {q}")
		print(f"r: {r}")

		print(f"i: {i}")
		print(f"j: {j}")

	print("outer scope - before inner scope:")
	print(f"i: {i}")
	print(f"j: {j}")

	inner()

	print("outer scope - before after scope:")
	print(f"p: {p}")
	print(f"q: {q}")
	print(f"r: {r}")

	print(f"i: {i}")
	print(f"j: {j}")


outer()

print("global scope:")
print(f"p: {p}")
print(f"q: {q}")
print(f"r: {r}")

print(f"i: {i}")
print(f"j: {j}")

# NOTE: Enclosing scope - nonlocal keyword:
# - The nonlocal statement causes the listed identifiers to refer to previously bound variables in the nearest enclosing scope excluding globals. This is important because the default behavior for binding is to search the local namespace first. The statement allows encapsulated code to rebind variables outside of the local scope besides the global (module) scope.
# - Names listed in a nonlocal statement, unlike those listed in a global statement, must refer to pre-existing bindings in an enclosing scope (the scope in which a new binding should be created cannot be determined unambiguously).
# - Names listed in a nonlocal statement must not collide with pre-existing bindings in the local scope.
