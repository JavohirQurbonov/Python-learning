# class Person:
#     def __init__(self,name,age,id,card_number):
#         self.name=name
#         self._age=age  # chala himoya
#         self.__id=id
#         self.__card_number=card_number
#
#     def get_id(self):
#         return self.__id
#
#     def update(self,x):
#         self.__id=x
#
#     def get_card_number(self):
#         card=list(self.__card_number)
#         card[4:13].replace('*')
#         return f"{self.__card_number[0:4]}"
# from enum import verify, Enum


# class Employee:
#     HARF = "qwertyuiopasdfghjklzxcvbnm"
#     HARF_KATTA = HARF.upper()
#
#     def __init__(self, fio, age, weight, ps):
#         self.varify_fio(fio)
#         self.verify_age(age)
#         self.__fio = fio
#         self.__age = age
#         self.__weight = weight
#         self.__ps = ps
#
#     @classmethod
#     def varify_fio(cls, fio):
#         if type(fio) != str:
#             raise TypeError("Malumot str yozilsin")
#         fio_list = fio.split()
#         if len(fio_list) != 3:
#             raise ValueError("qiymatlar uch qismdan iborat bolsin")
#         standard = cls.HARF + cls.HARF_KATTA
#
#         for qism in fio_list:
#             for harf in qism:
#                 if harf not in standard:
#                     raise ValueError("Malumot str yozilsin")
#                 else:
#                     print("Qabul qilindi")
#
#
#     @classmethod
#     def verify_age(cls, age):
#         if type(age) != int:
#             raise TypeError("Malumot int yozilsin")
#         if age < 0:
#             raise ValueError("Yosh manfiy bo'lmasin")
#         if age>=18 and age<=125:
#             return True
#         else:
#             return False
#
#     @property
#     def age(self):
#         return self.__age
#     @age.setter
#     def age(self, age):
#         verify_age = self.verify_age(age)
#         if verify_age:
#             self.__age = age
#
#     def get_info(self):
#         return f"""
#         FIO:{self.__fio}
#         Age:{self.__age}
#         Weight:{self.__weight}
#         PS:{self.__ps}
# """
#
#
# new = Employee("ali valiyev nurulohivich", 20, 62, "AB 1234567")
# print(new.get_info())


# ------------------------Homework---------------------------
#
# 1
# class Car:
#     """Car class"""
#     def __init__(self):
#         self.__mileage = 0
#
#     def drive(self,distance):
#         if type(distance)!=int:
#             raise TypeError('Masofa son bo\'lishi kerak')
#         if distance<0:
#             raise ValueError('Masofa musbat bo\'lishi kerak')
#         self.__mileage+=distance
#
#     def get_mileage(self):
#         return self.__mileage
#
#     @staticmethod
#     def is_service_needed(distance):
#         if type(distance)!=int:
#             raise TypeError('Masofa son bo\'lishi kerak')
#         if distance<0:
#             raise ValueError('Masofa musbat bo\'lishi kerak')
#         if distance>10_000:
#             return True
#         else:
#             return False
# car = Car()
# car.drive(10100)
# car.drive(10200)
# print(car.get_mileage())
# print(Car.is_service_needed(car.get_mileage()))

# 2

# class Student:
#     """Student class"""
#     __students_count = 0
#     def __init__(self, name,age):
#         self.__name = name.title()
#         self.__age = age
#         Student.__students_count+=1
#
#     @classmethod
#     def get_students_count(cls):
#         return cls.__students_count
#
#     @staticmethod
#     def is_adult(age):
#         if not isinstance(age,int):
#             raise TypeError('Yosh son bo\'lishi kerak')
#         return age >= 18
#
# s1 = Student("Ali", 19)
# s2 = Student("Bobur", 17)
# s3 = Student("javohir", 24)
# print(Student.get_students_count())
# print(Student.is_adult(19))
# print(Student.is_adult(17))

# 3

# class Product:
#     """Product class"""
#     __foiz=0
#     def __init__(self,price):
#         self.__price = price

#     @classmethod
#     def set_discount(cls,foiz):
#         if not isinstance(foiz,int):
#             raise TypeError('Foiz son bo\'lishi kerak')
#         if foiz < 0 or foiz > 100:
#             raise ValueError('Chegirma 0-100 oraliqda bo\'lishi kerak')
#         cls.__foiz = foiz

#     @staticmethod
#     def calculate_tax(amount):
#         standart_tax=5
#         if not isinstance(amount,int):
#             raise TypeError('Miqdor son bo\'lishi kerak')
#         if amount<0:
#             raise ValueError('Musbat son bo\'lishi kerak')
#         return amount+(amount*standart_tax)/100


#     def get_price(self):
#         return self.__price*((100-Product.__foiz)/100)



# p1 = Product(1000)
# Product.set_discount(10)  
# print(p1.get_price())  
# print(Product.calculate_tax(900))  




