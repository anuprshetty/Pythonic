class Car:
    """This is a Car class"""
    color = "red"
    num = "123"
    def __init__(self, model_name, year):
        self.model_name = model_name
        self.year = year
    
    def display(self):
        """This is a display method"""
        print("{} - {}, {}, {}".format(self.model_name, self.year, self.color, self.num))


car = Car("Benz", 2015)
car.display()
print(Car.__doc__)
print(Car.display.__doc__)

# delete a property of the object
del car.year
# AttributeError: 'Car' object has no attribute 'year'
# print(car.year)
# delete the object itself.
del car
# NameError: name 'car' is not defined
# print(car)
