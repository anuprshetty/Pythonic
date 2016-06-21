name = "Ram" # single quote
name = "Anup" # double quote

print(name)
print(name + name) # string join
print(name * 3) # print name 3 times

name2 = name

print(name2)

name2 = "Sham"

print(name2)
print(name)

# String formatting
# f-strings - allows embedding variables inside a string.
name = "Bob"
print(f"Hello, {name}")
name = "Alice"
print(f"Hello, {name}")
# template-strings - allows inserting variable values to a placeholder.
name = "Bob"
age = 32
print("Hello, {}! Your age is {}".format(name, age))
print("Hello, {1}! Your age is {0}".format(age, name))
age = 40
print("Hello, {}! Your age is {}".format(name, age))
