class Car:
    """This is a Car class"""
    # Class attributes
    count = 0
    def __init__(self, model_name, year):
        Car.count = Car.count + 1
        # Instance attributes
        self.model_name = model_name
        self.year = year
    
    def display(self):
        """This is a display method"""
        print("{} - {}, {}, {}".format(self.model_name, self.year, self.count, Car.count))


car = Car("Benz", 2015)
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
