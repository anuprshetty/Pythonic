# Packing and Unpacking using (Tuple not List)(*) AND (Dictionary or Mapping)(**).

x, y = 2, 3 # tuple
print(x, y)
t = (4, 5, 6)
a, b, c = t
print(t, a, b, c)

student_age = {"Anup": 24, "Ram": 20, "Bob": 30}
print(student_age.items())
for name, age in student_age.items(): # Unpacking
    print(name, age)

person = ("Alice", 23, "Doctor", "Bengaluru")
name, _, profession, _ = person # Ignore values by _

print(name, profession)

head, *tail = [1, 2, 3, 4, 5, 6]
print(head, tail) # 1 [2, 3, 4, 5, 6]
*head, tail = [1, 2, 3, 4, 5, 6]
head, *mid, tail = [1, 2, 3, 4, 5, 6]
first, second, *rest = [1, 2, 3, 4, 5, 6]

# head, *tail = [] # ValueError: not enough values to unpack (expected at least 1, got 0)

# Enumerate() Function:
names = ["Anup", "Ram", "Bob", "Alice"]
print(enumerate(names)) # <enumerate object at 0x00000209CE7B9740>
print(list(enumerate(names))) # [(0, 'Anup'), (1, 'Ram'), (2, 'Bob'), (3, 'Alice')]
print(list(enumerate(names, start=-2))) # [(-2, 'Anup'), (-1, 'Ram'), (0, 'Bob'), (1, 'Alice')]

for index, name in enumerate(names):
    print(index, name)


# Packing and Unpacking Arguments
# Packing
def multiply(*args):
    product = 1
    for num in args:
        product *= num
    
    return product

print(multiply(1, 2, 3))

# Unpacking
def add(x, y):
    return x + y

nums = [3, 5]
print(add(*nums)) # Arguments

nums = {"x": 3, "y": 5}
print(add(**nums)) # Keyword Arguments

# Packing and Unpacking with Named Arguments

def add(*args):
    sum = 0
    for num in args:
        sum += num
    
    return sum

def multiply(*args):
    product = 1
    for num in args:
        product *= num
    
    return product

def apply(*args, operator):
    if operator == "*":
        return multiply(*args)
    elif operator == "+":
        return add(*args)
    else:
        return "Invalid operator"

# Mandatory Named Argument
print(apply(4, 5, 6, 7, operator="*"))
print(apply(4, 5, 6, 7, operator="+"))
print(apply(4, 5, 6, 7, operator="%"))


# Packing and Unpacking Keyword Arguments
def named1(**kwargs):
    print(kwargs)

def named2(name, age):
    print(name, age)

named1(name="Bob", age=25) # {'name': 'Bob', 'age': 25}
details = {"name": "Alice", "age": 26}
named2(**details) # Alice 26


# Packing and Unpacking with both args and kwargs
# *args and **kwargs normally used to accept unlimited number of arguments to a function.
def both(*args, **kwargs):
    print(args) # (2, 3, 4, 5)
    print(kwargs) # {'name': 'Anup', 'age': '24', 'role': 'Developer'}

# Positional arguments -> *args
# Keyword/Named arguments -> **kwargs
both(2, 3, 4, 5, name="Anup", age="24", role="Developer")
both() # () {}

# Usage:
def request(method, url, data=None, json=None, **kwargs):
    pass

def post(url, data=None, json=None, **kwargs):
    request('post', url, data=None, json=None, **kwargs)

def get(url, data=None, json=None, **kwargs):
    request('get', url, data=None, json=None, **kwargs)
