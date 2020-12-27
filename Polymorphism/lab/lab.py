from abc import ABC, abstractmethod
from math import pi
# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def return_name(self):
#         return f"{self.name} new guy"
#
# class Shape(ABC):
#
#     def __init__(self, id):
#         self.id = id
#
#     @abstractmethod
#     def parameter(self):
#         pass
#
#     @abstractmethod
#     def area(self):
#         pass
#
# class Circle(Shape):
#     def __init__(self, id, radius):
#         super().__init__(id)
#         self.radius = radius
#
#     def parameter(self):
#         return 2 * pi * self.radius
#
#     def area(self):
#         return pi * self.radius ** 2
#
# class Rectangle(Shape):
#     def __init__(self, id, height, width):
#         super().__init__(id)
#         self.height = height
#         self.width = width
#
#     def parameter(self):
#         return self.height * self.width
#
#     def area(self):
#         return (self.height + self.width)/2
#
# ###################### if we have different classes we want ABSTRACT CLASS FOR COMBINING MORE THAN 1
# def print_info(obj):
#     if isinstance(obj, Person):
#         obj.return_name()
#     elif isinstance(obj, Shape):  ## elif isinstanse(obj.Circle) or isinstanse(obj, Rectangle)
#         print(f"Area: {obj.area()}")
#         print(f"Parimeter: {obj.parameter()}")
#
#
# print_info(Circle(1, 3))
# print_info(Rectangle(2, 5, 3))
########################################################################################################################
#               DUCKTYPING

# class Circle:
#     def __init__(self, id, radius):
#         self.id = id
#         self.radius = radius
#
#     def parameter(self):
#         return 2 * pi * self.radius
#
#     def area(self):
#         return pi * self.radius ** 2
#
# class Rectangle:
#     def __init__(self, id, height, width):
#         self.id = id
#         self.height = height
#         self.width = width
#
#     def parameter(self):
#         return self.height * self.width
#
#     def area(self):
#         return (self.height + self.width)/2
#
#
# def print_shape_info(shape):
#     print(f"Area: {shape.area()}")
#     print(f"Parimeter: {shape.parameter()}")
#
# print_shape_info(Circle(1, 3))
# print_shape_info(Rectangle(2, 5, 3))
########################################################################################################################
# def execute(func, *args):
#     return func(*args)
#
# def say_hello(name, my_name):
#     print(f"Hello, {name}, I am {my_name}")
#
# def say_bye(name):
#     print(f"Goodbye {name}")
#
#
# execute(say_hello, "Tedo", "Pesho")
# execute(say_bye, 'Ionko')
########################################################################################################################
# class Guitar:
#     def play(self):
#         print("Playing on the guitar")
#
# class Piano:
#     def play(self):
#         print("Piano music")
#
# def play_instrument(obj):
#     return obj.play()
#
# guitar = Guitar()
# play_instrument(guitar)
#
# piano = Piano()
# play_instrument(piano)
########################################################################################################################
class ImageArea:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def get_area(self):
        return self.height * self.width

    def __eq__(self, other):
        return self.get_area() == other.get_area()

    def __gt__(self, other):
        return self.get_area() > other.get_area()

    def __ge__(self, other):
        return self.get_area() >= other.get_area()

ia1 = ImageArea(2, 3)
ia2 = ImageArea(4, 5)

print(ia1 > ia2)
print(ia1 < ia2)
print(ia1 == ia2)
print(ia1 >= ia2)
print(ia1 != ia2)