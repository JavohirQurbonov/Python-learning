# ----------------------------Day-1----------------------------
# 1
# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def study(self):
#         return f"{self.name} is studying"
#
#     def get_age(self):
#         return f"{self.name} is {self.age} years old"
#
# obj=Student("James", 24)
# print(obj.study())
# print(obj.get_age())
# from calendar import prcal
# from os import name
# from time import sleep


# 2
# class Product:
#     """Product Class"""
#     def __init__(self,name:str,price:int):
#         self.name = name
#         self.price = price
#
#     def info(self)->str:
#         return f"{self.name} - {self.price}$"
#
# obj=Product("ASUS TUF FAMING F15",700)
# print(obj.info())

# 3

# class Car:
#     """Car class"""
#     def __init__(self, brand:str, year:int):
#         self.brand = brand
#         self.year = year
#     def is_new(self)->bool:
#         if not isinstance(self.year,int):
#             raise TypeError('Year must be an integer')
#         if self.year>=2022:
#             return True
#         else:
#             return False
#
# car=Car('Ford',2002)
# print(car.is_new())
# car1=Car('Mustang',2025)
# print(car1.is_new())

# ----------------------Day-2----------------------

# # 1
# class Counter:
#     """Counter class"""
#     count=0
#     def __init__(self):
#         Counter.count+=1
#
#     @classmethod
#     def get_count(cls):
#         return Counter.count
#
# c1=Counter()
# c2=Counter()
# print(c2.get_count())

# 2

# class Student:
#     """Student Class"""
#     school_name="Ustudy"
#     def __init__(self,name:str,age:int):
#         if not isinstance(name,str) and not isinstance(age,int):
#             raise TypeError("Student Class has to be of type str or int")
#         self.name=name
#         self.age=age
#     def get_info(self):
#         return f"{self.name} {self.age} {Student.school_name} da o'qiydi"
#
#     @classmethod
#     def change_school(cls,s_name:str):
#         Student.school_name=s_name
#
# st=Student("Javohir",24)
# print(st.get_info())
# Student.change_school("PDP")
# st1=Student("Bahodir",30)
# print(st.get_info())
# print(st1.get_info())

# 3

# class Product:
#     """Product class"""
#     tax_percent=5
#     def __init__(self,name:str,price:float):
#         if not  isinstance(name,str) and not isinstance(price,float):
#             raise TypeError("Product Name and Price must be of type str")
#         self.name=name.capitalize()
#         self.price=price
#
#     def final_price(self):
#         return self.price+(self.tax_percent*self.price)/100
#
#     @classmethod
#     def update_tax(cls,new_tax):
#         cls.tax_percent=new_tax
#
# obj1=Product("Milk",40000)
# print(obj1.final_price())

# ----------------------------Day-3----------------------------------

# 1
# class Student:
#     """Student Class"""
#     def __init__(self, name, age:int):
#         if not isinstance(name, str) or not isinstance(age, int):
#             raise TypeError("Student Name and Age must be of type str")
#         self.name=name.title()
#         self.age=age
#
#     def __str__(self):
#         return f"{self.name}, {self.age} yosh"
#
#     # def __repr__(self):
#     #     return f"{self.__class__.__name__}({self.name}, {self.age})"
#
# obj=Student('ali', 18)
# print(obj)

# 2

# class Product:
#     """Product class"""
#     def __init__(self, name:str, price:float):
#         if not isinstance(name, str) or not isinstance(price, (int,float)):
#             raise TypeError("Product name must be of type str and price must be of type float or int ")
#         self.name = name.title()
#         self.price = price
#
#     def __str__(self):
#         return f"{self.name}-{self.price}"
#
#     def __repr__(self):
#         return f"{self.name}-{self.price}"
#
#     def __eq__(self, other):
#         return self.price == other.price
#
#     def __lt__(self, other):
#         return self.price < other.price
#
#     def __gt__(self, other):
#         return self.price > other.price
#
# fruit1=Product("Apple", 10000)
# fruit2=Product("Orange", 15000)
# print(fruit1)
# print(fruit2)
# print(fruit1==fruit2)
# print(fruit1>fruit2)
# print(fruit1<fruit2)

# 3

# class Box:
#     """Box Class"""
#     def __init__(self, items:list):
#         self.items = items
#
#     def __len__(self):
#         return len(self.items)
#
#     def __call__(self, *args, **kwargs):
#         return f"Boxda {len(self.items)} ta element bor"
#
#     def __str__(self):
#         return str(self.items)
#
# box1=Box([1,2,3,'java','baxa'])
# print(box1)
# print(box1())

# ---------------------------------------------Day-4-------------------------------------

# 1

# class BankAccount:
#     """Bank account class"""
#     def __init__(self, balance):
#         self.__balance = balance
#
#     @property
#     def balance(self):
#         return self.__balance
#
#     def deposit(self, amount):
#         if not isinstance(amount, (int,float)):
#             raise TypeError("Balance must be an integer/float")
#         if amount < 0:
#             raise ValueError("Balance cannot be negative")
#         self.__balance += amount
#
#     def withdraw(self, amount):
#         if not isinstance(amount, (int,float)):
#             raise TypeError("Balance must be an integer/float")
#         if amount < 0:
#             raise ValueError("Balance cannot be negative")
#         if amount > self.__balance:
#             raise ValueError("Balance cannot be greater than current balance")
#         self.__balance -= amount
#
#     def __repr__(self):
#         return f"Balance: {self.__balance}"
#
# acc=BankAccount(10000)
# acc.deposit(100)
# print(acc.balance)
# acc.withdraw(10000000)
# print(acc.balance)

# 2

# class Product:
#     """Product class"""
#     def __init__(self, name:str, price):
#         self.name = name.title()
#         self.__price = price
#
#     def __repr__(self):
#         return f"Name: {self.name}, Price: {self.__price}"
#
#     @property
#     def price(self):
#         return self.__price
#
#     @price.setter
#     def price(self, new_price):
#         if not isinstance(new_price, (int,float)):
#             raise TypeError('Price must be a numeric value')
#         if new_price>0:
#             self.__price = new_price
#         else:
#             raise ValueError('Price must be positive')
#
# obj=Product("apple",15000)
# obj.price=20000
# print(obj)

# 3

# class User:
#     """User class"""
#     def __init__(self,user:str,password:str):
#         self.user = user
#         self.__password = password
#
#     def __len__(self):
#         return len(self.__password)
#
#     def __repr__(self):
#         return f"{self.user} {self.__password}"
#
#     def check_password(self):
#         if len(self.__password)<8:
#             return  False
#
#         has_upper=False
#         has_digit=False
#
#         for s in self.__password:
#             if s.isupper():
#                 has_upper=True
#             if s.isdigit():
#                 has_digit=True
#
#         return has_digit and has_upper
#
# obj=User("java","Java6998")
# print(obj.check_password())
#
#


#----------------------------------------Day-5-----------------------------------------

# class Animal:
#     """Animal class"""
#     def __init__(self, name:str):
#         self.name = name
#
#
#     def sound(self):
#         print("Animal sound")
#
# class Dog(Animal):
#     def sound(self):
#         return f"{self.name.title()}-Dog barks"
#
# obj=Dog("simba")
# print(obj.sound())

# 2

# class Employee:
#     """Employee class"""
#     def __init__(self, name:str, salary:float):
#         self.name = name.title()
#         self.salary = salary
#
#     def get_info(self):
#         info=f"Name:{self.name}\nSalary:{self.salary}"
#         return info
#
# class Developer(Employee):
#     """Developer class"""
#     def __init__(self, name:str, salary:float,language:str):
#         super().__init__(name, salary)
#         self.language=language
#
#     def get_info(self):
#         info=f"Name:{self.name}\nSalary:{self.salary}\n"
#         info+=f"Language:{self.language}"
#         return info
#
# obj=Employee('javohir',500)
# obj2=Developer('javohir',600,'python')
# print(obj.get_info())
# print(obj2.get_info())

# 3

# class Manager:
#     """Manager class"""
#     def __init__(self, name, experience):
#         Manager.check_info(name,experience)
#
#         self.name = name.title()
#         self.experience = experience
#
#     @classmethod
#     def check_info(cls,name,experience):
#         if not isinstance(name,str):
#             raise TypeError("Ism harfda kiritilishi kerak")
#         if not isinstance(experience,(float,int)):
#             raise TypeError("Tajriba raqamda kiritiladi!")
#
#     def team_info(self):
#         return f"Name:{self.name}\nExperience:{self.experience}"
#
# class Developer(Manager):
#     """Developer class"""
#     def __init__(self,name,experience,age,languages:list):
#         super().__init__(name,experience)
#         self.age = age
#         self.languages = languages
#
#     def team_info(self):
#         return f"Name{self.name}\nExperience:{self.experience}\nAge:{self.age}\nLanguages:{self.languages}"
#
# obj=Developer("Javohir",1,24,['python','typescript'])
# print(obj.team_info())
#

# ------------------------------Day-6----------------------------------

# 1

# from abc import ABC,abstractmethod
# from math import pi
#
# class Shape(ABC):
#     """Shape class"""
#     @abstractmethod
#     def area(self):
#         pass
#
# class Rectangle(Shape):
#     def __init__(self,width,height):
#         self.width = width
#         self.height = height
#
#     def area(self):
#         return f"Eni:{self.width}\nBo'yi:{self.height}\nYuzi:{self.width*self.height}"
#
# class Circle(Shape):
#     def __init__(self,radius):
#         self.radius = radius
#
#     def area(self):
#         return f"Radius:{self.radius}\nYuzi:{pi*pow(self.radius,2)}"
#
# obj=Circle(5)
# print(obj.area())

# 2

# from abc import ABC,abstractmethod
#
# class Vehicle(ABC):
#     """Vehicle class"""
#
#     @abstractmethod
#     def start_engine(self):
#         pass
#
# class Car(Vehicle):
#     """Car class"""
#
#     def start_engine(self):
#         return f"Car engine started"
#
# class Bike(Vehicle):
#     """Bike class"""
#
#     def start_engine(self):
#         return f"Bike engine started"
#
# obj=Car()
# obj1=Bike()
# print(obj.start_engine())
# print(obj1.start_engine())

# ------------------------------Day-7--------------------------

# 1

# from abc import ABC,abstractmethod
#
# class Account(ABC):
#     """Account class"""
#     def __init__(self,balance:float):
#         self.__balance = balance
#
#     @staticmethod
#     def verify_amount(amount):
#         if  not isinstance(amount,(float,int)):
#             raise TypeError("Qiymat son ko'rinishida bo'lishi kerak")
#         if amount<0:
#             raise ValueError("Miqdor manfiy bo'lishi mumkin emas")
#
#     def deposit(self,amount):
#         self.verify_amount(amount)
#         self.__balance+=amount
#
#     def withdraw(self,amount):
#         self.verify_amount(amount)
#         if amount>self.__balance:
#             raise ValueError("Hisobda mablag' yetarli emas!")
#         self.__balance-=amount
#
#     def get_balance(self)->float:
#         return self.__balance
#
#     @abstractmethod
#     def account_type(self)->str:
#         pass
#
# class SavingsAccount(Account):
#     """SavingsAccount class (inheritense class)"""
#     def __init__(self,balance,interest_rate):
#         super().__init__(balance)
#         self.interest_rate = interest_rate
#
#     def apply_interest(self):
#         procent=self.get_balance()*self.interest_rate/100
#         self.deposit(procent)
#
#     def account_type(self) ->str:
#         return f"Savings"
#
# class CheckingAccount(Account):
#     """Checking Account (inheritense class)"""
#     def __init__(self ,balance ,fee ):
#         super().__init__(balance)
#         self.fee = fee
#
#     def withdraw(self,amount):
#         total=amount+self.fee
#         super().withdraw(total)
#
#     def account_type(self) ->str:
#         return f"Checking"
#
#
#
# savings = SavingsAccount(1000, 5)
# checking = CheckingAccount(2000, 10)
#
# accounts = [savings, checking]
#
# def show_account_info(accounts: list):
#     """Bitta funksiya orqali barcha accountlarni ishlatish"""
#     for acc in accounts:
#         print(f"Account type: {acc.account_type()}, Balance: {acc.get_balance()}")
# savings.apply_interest()
# checking.withdraw(500)
#
# print("\nBalans yangilanganidan keyin:")
# show_account_info(accounts)

