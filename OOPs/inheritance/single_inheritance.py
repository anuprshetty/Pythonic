# Inheritance means a printer is a device.

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
    
    def __init__(self, name, connected_by, capacity):
        super().__init__(name, connected_by)
        self.capacity = capacity
        self.remaining_pages = capacity

    def __str__(self):
        # Calling superclass method from subclass method.
        return f"{super().__str__()} ({self.remaining_pages} pages remaining)"

    def print(self, pages):
        if not self.connected:
            print("Failed to print pages. Your printer is not conncted!")
            return
        elif pages <= self.remaining_pages:
            print(f"Printing {pages} pages.")
            self.remaining_pages -= pages
        else:
            print(f"Failed to print {pages} pages. Only {self.remaining_pages} pages available in the printer.")


printer = Printer("Laser printer", "USB", 150)
print(printer)
printer.print(20)
printer.print(200)
print(printer)
printer.disconnect()
printer.print(30)
print()

# Check if a Class is a Subclass of another Class
print(issubclass(Printer, Device))  # True
print(issubclass(Printer, object))  # True
print(issubclass(Device, object))  # True
