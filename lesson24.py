# class Animal:
#
#     def __init__(self,name,color):
#         print("haa")
#         self.name=name
#         self.color=color
#
#     def speak(self):
#         return "Nomalum"
#
# class Cat(Animal):
#     def __init__(self,name,moylovi):
#         super().__init__(name)
#         self.moylovi=moylovi
#
#     def speak(self):
#         return "Miyav miyav"
#
#
# class Dog(Animal):
#     def __init__(self,name,dumi):
#         super().__init__(name)
#         self.dumi=dumi
#
#     def speak(self):
#         return "vov vov "
# new=Animal('simba')
# print(new.speak())
# cat=Cat('koshka')
# dog=Dog('rafinya')
# print(cat.speak())
# print(dog.speak())
# from os import name
# from logging import info
# from time import sleep


# class Animal:
#     pass
#
# class Dog(Animal):
#     pass
#
# dog=Dog()
# print(isinstance(dog,Dog))
# print(isinstance(dog,Animal))
# print(issubclass(Dog,Animal))
# print(issubclass(Animal,Dog ))

# -------------------------------------Homework----------------------------------------

# 1

# class Vehicle:
#     """Vehicle class"""
#     def __init__(self, name:str, speed:float):
#         self.name = name
#         self.speed = speed
#
#     @staticmethod
#     def factory():
#         return f"UzAuto Motors"
#
# class Car(Vehicle):
#     """Car class"""
#     def __init__(self, name, speed):
#         super().__init__(name,speed)
#
#     @staticmethod
#     def honk():
#         return f"Bip-bip!"
#
# class Bicycle(Vehicle):
#     """Bicycle class"""
#     def __init__(self, name, speed):
#         super().__init__(name,speed)
#
#     @staticmethod
#     def pedal():
#         return f"Tezroq aylantir"
#
# class Truck(Vehicle):
#     """Truck class"""
#     def __init__(self, name, speed):
#         super().__init__(name,speed)
#
#     def load_cargo(self):
#         return f"15 tonna yuk qabul qilamiz"
#
# car=Truck("Cobalt",180)
# print(car.load_cargo())
# print(Car.honk())
# print(Car.factory())
#
# print(Bicycle.pedal())
# # print(Truck.load_cargo())

# 2

# class Animal:
#     """Animal class"""
#     def __init__(self, name):
#         self.name = name
#
#     def make_sound(self):
#         return "Animal sound"
#
# class Lion(Animal):
#     """Lion class"""
#     def make_sound(self):
#         return f"Roar!"
#
#
# class Eagle(Animal):
#     """Eagle class"""
#     def make_sound(self):
#         return f"Screech"
#
#
# class Shark(Animal):
#     """Shark class"""
#     def __init__(self,name):
#         super().__init__(name)
#
#
#     def make_sound(self):
#         return f"Splash"
#
# animmal=Animal("bear")
# print(animmal.make_sound())
#
# shark=Shark("Simba")
# print(shark.make_sound())
#
#

# 3

# from abc import ABC,abstractmethod
# class Employee(ABC):
#     """Employee class"""
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     @abstractmethod
#     def get_salary(self,parametr):
#         pass
#
#
# class Manager(Employee):
#     """Manager class(inheritence class)"""
#     order_price=100
#     def __init__(self, name, age,experience):
#         super().__init__(name,age)
#         self.experience = experience
#
#     def get_salary(self,order_count):
#         return Manager.order_price*order_count
#
# class Developer(Employee):
#     """Developer class(inheritence class)"""
#     hours_worked = 45
#
#     def __init__(self, name, age, experience):
#         super().__init__(name, age)
#         self.experience = experience
#
#     def get_salary(self, hours):
#         return Developer.hours_worked * hours
#
# class Designer(Employee):
#     """Designer class(inheritence class)"""
#     hours_worked = 25
#
#     def __init__(self, name, age, experience):
#         super().__init__(name, age)
#         self.experience = experience
#
#     def get_salary(self, hours):
#         return Designer.hours_worked * hours
#
# obj=Designer("Java",24,5)
# print(obj.get_salary(8))

# 4
# from datetime import date
# class Product:
#     """Product class"""
#     def __init__(self, name:str, price:float):
#         self.name = name.title()
#         self.price = price
#
# class Electronics(Product):
#     """Electronics class (inheritence class)"""
#     def __init__(self,name,price):
#         super().__init__(name,price)
#
#     def apply_discounts(self,sale_procent):
#         return self.price*(100-sale_procent)/100
#
# class Clothing(Product):
#     """Clothing class (inheritence class)"""
#     def __init__(self,name,price):
#         super().__init__(name,price)
#
# class Foods(Product):
#     """Foods class (inheritence class)"""
#     def __init__(self,name,price):
#         super().__init__(name,price)
#
#     def check_expiry(self,expiration_date ,*args,**kwargs):
#         if not isinstance(expiration_date,(int,float)):
#             raise TypeError("Son qiymat kiriting")
#         if expiration_date<0:
#             raise ValueError("Manfiy qiymat kiritib bo'lmaydi!")
#         else:
#             today=date.today()
#             diff=today-date(*args,**kwargs)
#             dayss=diff.days
#             if dayss<expiration_date*30:
#                 return f"Yaroqli"
#             else:
#                 return f"Yaroqsiz"
#
#
#
#
# # obj=Foods("Non",3000)
# # print(obj.check_expiry(2,2026,1,9))
#
# obj1=Electronics("Laptop",11_000_000)
# print(obj1.apply_discounts(20))

# 5

# class BankAccount:
#     """BankAccount class (Father class)"""
#     def __init__(self,name,balance):
#         self.name = name
#         self.balance = balance
#
# class SavingAccount(BankAccount):
#     """SavingAccount class (inheritence class)"""
#     def __init__(self,  name, balance):
#         super().__init__(name, balance)
#
#     def withdraw(self,amount):
#         if not isinstance(amount,(float,int)):
#             raise TypeError("Miqdorni son bilan kiriting!")
#         if amount<0:
#             raise ValueError("Qiymat manfiy bo'lishi mumkin emas!")
#         if amount>self.balance:
#             return f"Balansda yetarli mablag' yo'q"
#         else:
#             self.balance-=amount
#             return f"Balansda {self.balance} pul qoldi"
#
#
#
# class CheckingAccount(BankAccount):
#     """CheckingAccount class (inheritence class)"""
#     def __init__(self, name, balance,pin_kod):
#         super().__init__(name, balance)
#         self.pin_kod = pin_kod
#
#     def check_balance(self,user_pin_kod):
#         if len(str(user_pin_kod))==4:
#             if not isinstance(user_pin_kod,int):
#                 raise TypeError("Pin kod butun son ko'rinishida bo'lsin!")
#             if user_pin_kod<0:
#                 raise  ValueError("Pin kod manfiy bo'lmaydi!")
#             if user_pin_kod==self.pin_kod:
#                 return f"Sizning balansingiz=>{self.balance}"
#             else:
#                 return  f"Pin kod xato kiritildi"
#
#         else:
#             return f"Pin kod 4 xonadan iborat bo'lishi kerak"
#
#
#
# obj1=SavingAccount("Javohir",4000)
# print(obj1.withdraw(5000))
#
# obj2=CheckingAccount("Bahodir",5000,7885)
# print(obj2.check_balance(7785))
#
#




# ----------Extra-------------
# 1

# class Person:
#     """Person class"""
#     def __init__(self, name:str, age:int):
#         self.name = name.title()
#         self.age = age
#
#     def get_info(self):
#         return f"Ism:{self.name}\nAge:{self.age}"
#
#     def __repr__(self):
#         return f"Ism:{self.name}\nAge:{self.age}"
#
# class Student(Person):
#     """Student class (inheritence class)"""
#     def __init__(self,name,age,course:int):
#         super().__init__(name,age)
#         self.course = course
#
#     def get_info(self):
#         return f"Ism:{self.name}\nAge:{self.age}\nCourse:{self.course}"
#
# obj1=Student("javohir",24,1)
# print(obj1.get_info())
#

# 2

# class Employee:
#     """Employee class"""
#     def __init__(self, name, salary):
#         self.name = name.title()
#         self.salary = salary
#
#     def get_salary(self):
#         return f"Salary:{self.salary}"
#
# class Manager(Employee):
#     """Manager class (inheritence class)"""
#     def __init__(self,name,salary,bonus):
#         super().__init__(name,salary)
#         self.bonus = bonus
#
#     def get_salary(self):
#         return f"{super().get_salary()}\nBonus:{self.bonus}"
#
# obj=Manager("javohir",500,200)
# print(obj.get_salary())
#
#
#

# 3

# class Vehicle:
#     """Vehicle class"""
#     def __init__(self, brand:str, speed:int):
#         self.brand = brand
#         self.speed = speed
#
# class Car(Vehicle):
#     """Car class (Inheritense class)"""
#     def __init__(self, brand:str, speed:int,color:str):
#         super().__init__(brand,speed)
#         self.color = color

# 4

# class User:
#     """User class"""
#     def __init__(self, login: str):
#         self.login = login
#
# class Admin(User):
#     """Admin class"""
#     def __init__(self, login: str, password: str):
#         super().__init__(login)
#         self.password = password
#
# class SuperAdmin(Admin):
#     """SuperAdmin class"""
#     def __init__(self, login: str, password: str, experience: float):
#         super().__init__(login, password)
#         self.experience = experience
#
# sa = SuperAdmin("javohir", "1234", 5)
# print(sa.login)
# print(sa.password)
# print(sa.experience)
#

# 5

# class Account:
#     """Account class"""
#     def __init__(self, balance: float):
#         self.balance = balance
#
#     def deposit(self, amount):
#         if not isinstance(amount, (int, float)):
#             raise TypeError("Miqdorni son ko'rinishida kiriting!")
#         if amount < 0:
#             raise ValueError("Manfiy qiymat kiritish mumkin emas")
#         self.balance += amount
#         return self.balance
#
#
# class SavingsAccount(Account):
#     """SavingsAccount class"""
#     def __init__(self, balance: float):
#         super().__init__(balance)
#
#     def add_interest(self, percent):
#         self.balance += (self.balance * percent) / 100
#         return self.balance
#
# obj = SavingsAccount(120_000)
# print(obj.add_interest(12))
# print(obj.deposit(5000))

# 6

# class Animal:
#     """Animal class"""
#     pass
#
# class Dog(Animal):
#     """Dog class"""
#     pass
#
# class Cat(Animal):
#     """Cat class"""
#     pass
#
# def check_animal(obj):
#     if isinstance(obj, Dog):
#         return "Bu Dog obyekt"
#     elif isinstance(obj, Cat):
#         return "Bu Cat obyekt"
#     elif isinstance(obj, Animal):
#         return "Bu Animal obyekt"
#     else:
#         return "Noma'lum tur"
#
#
# dog1 = Dog()
# cat1 = Cat()
# animal1 = Animal()
#
# print(check_animal(dog1))
# print(check_animal(cat1))
# print(check_animal(animal1))

# 7

# class Notification:
#     """Notification class"""
#     def send(self, message):
#         print(f"Notification: {message}")
#
# class EmailNotification(Notification):
#     """EmailNotification class"""
#     def send(self, message):
#         super().send(message)
#         print(f"Email yuborildi: {message}")
#
#
# note = EmailNotification()
# note.send("Salom, Javohir!")









