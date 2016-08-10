from collections import namedtuple


# namedtuple is a function which returns a new subclass of tuple with named fields.
Color = namedtuple(typename='Color', field_names=['red', 'green', 'blue'])

color1 = Color(red=24, green=56, blue=126)
print(color1[0])
print(color1[1])
print(color1[2])
print(color1.red)
print(color1.green)
print(color1.blue)

color2 = Color(red=1, green=2, blue=3)
print(color2[0])
print(color2[1])
print(color2[2])
print(color2.red)
print(color2.green)
print(color2.blue)
