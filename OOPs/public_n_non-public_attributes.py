# Public and Non-Public attributes help us to follow the principle of encapsulation.
# In Python an attribute can be public or non-public.

# 1. Public attribute: An attribute that can be accessed and modified directly without access restrictions.
class Car:
    def __init__(self, brand, model, year):
        self.__brand = brand # Non-Public attribute by name mangling approach.
        self._model = model # Non-Public attribute by naming convention approach.
        self.year = year # Public attribute

car = Car("Honda", "City", 2015)
print(car.year)
# Problem with public attribute: we can directly access and modify it without any validation.
car.year = 4693
print(car.year)

# 2. Non-Public attribute: An attribute that shouldn't be accessed or modified outside of class.
# NOTE: 
# * We don't use the term "private" here, since no attribute is really private in Python.
# * Technically you can access them outside the class. But you shouldn't according to the Python naming conventions. 
# * In Python, we don't have any access modifiers(private, protected, public) like any other object oriented programming languages. 
# * Everything is public in Python. So we rely on naming convention to tell other developers that a member of a class like an attribute or a method is intended to be non-public. 

# Two ways of defining non-public attributes:
# a. By naming convention --> _<attribute> [We add a leading underscore to the attribute name.]
# print(car.model) # AttributeError: 'Car' object has no attribute 'model'
print(car._model) # City # Technically you can access them outside the class. But you shouldn't according to the Python naming conventions.

# b. By name mangling (A process/mechanism called "name mangling" is triggerred to modify the name of the attribute which makes it more difficult to access.) --> __<attribute> (Only used for special cases) [We add 2 leading underscores to the attribute name.]
# What happens behind the scenes?
# __<attribute> --> name mangling --> _<class>__<attribute>
# Ex: __engine_serial_num --> name mangling --> _Car__engine_serial_num
# print(car.brand) # AttributeError: 'Car' object has no attribute 'brand'
# print(car._brand) # AttributeError: 'Car' object has no attribute '_brand'
# print(car.__brand) # AttributeError: 'Car' object has no attribute '__brand'
print(car._Car__brand) # Honda # Technically you can access them outside the class. But you shouldn't according to the Python naming conventions.

# NOTE:
# __<attribute> --> name mangling is triggerred.
# __<attribute>_ --> name mangling is triggerred.
# __<attribute>__ --> name mangling is NOT triggerred. This is reserved for "Magic Methods or Dunder - Double Under (Underscores)"
# You should only use name mangling for special cases, we usually rely on 1 leading underscore to define a non-public attribute.

# Non-Public Methods and Name Mangling:
# - To make a method "non-public", you should add a leading underscore.
def _display_data():
    pass

# - If you add two underscores, the process of name mangling will occur, just like with non-public attributes.
def __display_data():
    pass
