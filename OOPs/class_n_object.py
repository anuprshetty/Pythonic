class Car:
    """This is a Car class"""
    # Class attributes
    count = 0

    # Constructor
    def __init__(self, model_name, year):
        Car.count = Car.count + 1
        # Instance attributes
        self.model_name = model_name
        self.year = year
    
    def display(self):
        """This is a display method"""
        print("{} - {}, {}, {}".format(self.model_name, self.year, self.count, Car.count))
    
    # String representation of an object for users
    def __str__(self):
        return "__str__: An object of Car class"
    
    # String representation of an object for developers while debugging.
    # __repr__() method is used in Python debugger.
    # __repr__() method is used to unambiguous representation of an object. So that you use that to recreate the object.
    def __repr__(self):
        return "__repr__: An object of Car class"


car = Car("Benz", 2015)
# __str__() function:
# Without __str__() function: <__main__.Car object at 0x000001AD09F27FD0>
# With __str__() function: An object of Car class
print(car) # Calls __str__() function.
print(car.__str__()) # Explicit calling
print(car.__repr__()) # Explicit calling
car.display()
print(Car.__doc__)
print(Car.display.__doc__)

car2 = Car("Audi", 2017)
Car.display(car2)
print(Car.__dict__)
print(car2.__dict__)

# delete a property of the object
del car.year
# AttributeError: 'Car' object has no attribute 'year'
# print(car.year)
# delete the object itself.
del car
# NameError: name 'car' is not defined
# print(car)
