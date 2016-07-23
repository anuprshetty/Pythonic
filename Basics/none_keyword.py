# None is a Python keyword used to define a null variable or null object.
# We typically use it to indicate that a variable has no value or no object assigned to it (yet).

# It is an object itself
print(isinstance(None, object)) # True

# Its also a data type of its own
print(type(None)) # <class 'NoneType'>

# None with == and is operators
var = None
if var == None:
    print("var == None") # printed
if var is None:
    print("var is None") # printed
    