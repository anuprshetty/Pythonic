# Order of execution
def hello(): # 1. Create a Python variable hello which is a callable.
    print("Hello World!") # 3. Execute the function.

hello() # 2. Call the function.

# NOTE: 
# - In Python, objects are PASSED by reference and NOT PASSED by value. 
# - We pass a reference to the object, not a new copy, so the original object can be modified. 

def add(x, y): # Parameters
    # pass # Do Nothing
    result = x + y
    return result

result = add(3, 5) # Positional Arguments
print(result)

result = add(y=2, x=4) # Keyword or named Arguments
print(result)

result = add(6, y=7) # Positional Arguments first, Keyword Arguments next.
print(result)

# Default parameter values in function.
def subtract(x, y=3): # Required Parameters first, Optional/Default Parameters next.
    # pass # Do Nothing
    result = x - y
    return result

result = subtract(2)
print(result)


# NOTE: Avoid returning diffrent data types in a function, although it is possible. 
# Best Practice - Always return same data type in a function.
