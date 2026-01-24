# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# person=Person("Ali",18)
#
# # print(hasattr(person,"name"))
# # print(hasattr(person,"salary"))
# #
# # print(getattr(person,"name"))
# # print(getattr(person,"email","Not available"))
#
# # setattr(person,"age",25)
# # print(person.age)
# #
# # setattr(person,"name",'John')
# # print(person.name)
#
# delattr(person,"name")
# print(hasattr(person,"name"))
from abc import ABC
# class Employee:
#     MIN=18
#     MAX=40
#     STANDARD=500
#
#     @classmethod
#     def check_age(cls,x):
#         return cls.MIN<x<cls.MAX
#
#
#     def __init__(self,name,age,exp):
#         self.exp = exp
#         self.name = name
#         self.age=0
#         if not self.check_age(age):
#             print(f"Sizni {age} yoshingiz tushmadi")
#         else:
#             self.age=age
#
#         print(f"Sizga tajribangiz {self.exp} yil bo'lgani uchun {self.calculate_exp(self.exp)} $")
#
#
#     def get(self):
#         return f"hodimi ismi {self.name} yoshi {self.age} tajribasi {self.exp}"
#
#     @staticmethod
#     def calculate_exp(exp):
#         if exp>4:
#             data=Employee.STANDARD*1.5
#             return data
#         elif exp<4:
#             data=Employee.STANDARD*0.8
#             return data
#
#
#
#
#
# obj=Employee("ali",26,3)
# obj2=Employee("vali",36,20)
# print(obj.get())
# print(obj2.get())

# class Game_Zone:
#     computer_count=20
#     HOUR=9000
#     @classmethod
#     def check_count(cls,x):
#         return cls.computer_count>=x and x%2==0
#
#     def __init__(self, user_count, playing_time):
#         self.user_count = 0
#         self.playing_time = 0
#         if not self.check_count(user_count):
#             return f"Foydalanuvchilar soni ko'p"
#         else:
#             self.user_count=user_count
#
#     @staticmethod
#     def calculate(user_count,playing_time):
#         data=user_count*playing_time*9000
#         return data
# obj=Game_Zone(5,20)
# print(obj.calculate(5,20))











# Homework

# 1
# from datetime import datetime
#
# class Person:
#     """Person class"""
#     def __init__(self,name,age):
#         self.name = name.capitalize()
#         self.age = age
#
#     def get_info(self):
#         return f"Name:{self.name}\nAge:{self.age}"
#
#     @classmethod
#     def from_birth_year(cls,name, birth_year):
#         year=datetime.today().year
#         diff=year-birth_year
#         return cls(name,diff)
#
# obj1=Person.from_birth_year("elbek",2002)
# print(obj1.get_info())
#
# obj2=Person("javohir",25)
# print(obj2.get_info())

# 2

# class Student:
#     """Student class"""
#     def __init__(self,full_name, grade):
#         self.full_name = full_name.title()
#         self.grade = grade
#
#     def __repr__(self):
#         return f"{self.full_name}-{self.grade}-bosqichda o'qiydi"
#     def get_info(self):
#         return f"{self.full_name}-{self.grade}-bosqichda o'qiydi"
#
#     @staticmethod
#     def validate_grade(grade):
#         if int(grade)>=1 and int(grade)<=11:
#             return True
#         else:
#             return False
#
#     @classmethod
#     def create_if_valid(cls, full_name, grade):
#         if cls.validate_grade(grade):
#             return cls(full_name, grade)
#         else:
#             return "Invalid grade"
#
#
# obj=Student("Javohir Qurbonov","8")
# print(obj.get_info())
# print(obj.create_if_valid("Bahodir Qurbonov","10"))

# 3
from datetime import datetime

class Car:
    """Car class"""
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def get_info(self):
        return f"{self.brand} {self.model} {self.year}"

    @staticmethod
    def is_old(year):
        current_year=datetime.now().year
        return (current_year-int(year))>10

    @classmethod
    def from_string(cls, car_string):
        brand, model, year = car_string.split(",")
        return cls(brand, model, year)

car1=Car.from_string("Toyota,Camry,2020")
print(car1.get_info())
print(Car.is_old(car1.year))

