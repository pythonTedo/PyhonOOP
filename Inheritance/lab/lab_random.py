# from random import choice
#
# class RandomList(list):
#
#     def get_random_element(self):
#
#         element_to_get = choice(self)
#         self.remove(element_to_get)
#         return element_to_get
#
# ll = RandomList([1,2,3,4,5,6,7])
############################################################################################################################
# class Animal:
#     def eat(self):
#         return "eating"
#
# class Dog(Animal):
#      def bark(self):
#          return "bark"
#
# class Pesho(Dog):
#     def smile(self):
#         return "smile"
#
#
# d = Dog()
# p = Pesho()
#
# print(d.bark())
# print(d.eat())
# print(p.bark())
# print(p.eat())
############################################################################################################################
# class Clock:
#     def __init__(self, hours, minutes, seconds):
#         self.hours = hours
#         self.minutes = minutes
#         self.seconds = seconds
#
#     @property
#     def time(self):
#         return f"{self.hours}:{self.minutes}:{self.seconds}"
#
#     def __repr__(self):
#         return self.time
#
#     def show_time(self):
#         print(self.time)
#
# class Calendar:
#     def __init__(self, year, month, day):
#         self.year = year
#         self.month = month
#         self.day = day
#
#
#     @property
#     def date(self):
#         return f"{self.year}/{self.month}/{self.day}"
#
#     def __repr__(self):
#         return self.date
#
#     def show_date(self):
#         print(self)
#
# class ClockCalendar(Clock, Calendar):
#     def __init__(self, year, month, date, hours, minutes, seconds):
#         Calendar.__init__(self, year, month, date)
#         Clock.__init__(self, hours, minutes, seconds)
#
#         #super().__init__(hours, minutes, seconds) ## vzima samo ot purviq class
#
#     def show_date_time(self):
#         return f"{self.date} {self.time}"
#
# # Clock(15, 45, 50).show_time()
# # Calendar(2020, 12, 14).show_date()
#
# print(ClockCalendar(2020, 12, 14, 0o1, 0o1, 0o1).show_date_time())
############################################################################################################################
# class Person:
#     def sleep(self):
#         return "sleeping"
#
# class Employee:
#     def get_fired(self):
#         return "fired"
#
# class Teacher(Person, Employee):
#     def teach(self):
#         return "teaching"
#
# c = Teacher()
# print(c.get_fired())






