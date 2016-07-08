# Inheritance means a printer is a device.

# Default Inheritance: The 'object' class is the parent class of all the classes in Python by default. 

class Device:
    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True

    def __str__(self):
        # self.name!r calls __repr__() method of self.name object.
        # self.name!s calls __str__() method of self.name object.
        return f"Device {self.name!r} ({self.connected_by})"

    def disconnect(self):
        self.connected = False
        print(f"{self.name} is disconnceted.")

device = Device("printer", "USB")
print(device.name.__str__()) # printer
print(device.name.__repr__()) # 'printer'
print(device) # Calls __str__(). If not calls __repr__().
device.disconnect()


class Printer(Device):
    # The Python super() method lets you access methods from a parent class from within a child class. 
    # This helps reduce repetition in your code. 
    # super() does not accept any arguments.
    def __init__(self, name, connected_by, capacity):
        super().__init__(name, connected_by)
        self.capacity = capacity
        self.remaining_pages = capacity

    def __str__(self):
        return f"{super().__str__()} ({self.remaining_pages} pages remaining)"

    def print(self, pages):
        if not self.connected:
            print("Your printer is not conncted!")
            return
        elif pages <= self.remaining_pages:
            print(f"Printing {pages} pages.")
            self.remaining_pages -= pages
        else:
            print(f"Only {self.remaining_pages} pages available in the printer.")


printer = Printer("Laser printer", "USB", 150)
print(printer)
printer.print(20)
printer.print(200)
print(printer)
printer.disconnect()
printer.print(30)
