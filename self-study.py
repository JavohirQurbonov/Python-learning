# class Talaba:
#     """"Talaba nomli klass yaratamiz"""
#     def __init__(self,ism,familiya,tyil):
#         self.name = ism
#         self.familiya = familiya
#         self.tyil = tyil
#         self.bosqich=1
#
#     def tanishtir(self):
#         print(f"Salom mening ismim {self.name} {self.familiya} \nMen {self.tyil}-yilda tug'ilganman ")
#
#     def get_name(self):
#         """"Talaba ismini qaytaradi"""
#         return self.name
#
#     def get_familiya(self):
#         """"Talaba familiyasini qaytaradi"""
#         return self.familiya
#     def get_tyil(self):
#         """"Talaba tug'ilga yilini qaytaradi"""
#         return self.tyil
#
#     def get_bosqich(self, bosqich):
#         """"Talaba bosqichi"""
#         self.bosqich = bosqich
#         return self.bosqich
#
# talaba1=Talaba("Javohir","Qurbonov",2001)
# from time import sleep
# from logging import info
from threading import settrace_all_threads

# print(talaba1.get_bosqich(4))


# Homework
# class User:
#     """"User information class"""
#
#     def __init__(self, login, name, lname, age, number, email):
#         self.login = login
#         self.name = name.strip().capitalize()
#         self.lname = lname.strip().capitalize()
#         self.age = age
#         self.number = number
#         self.email = email
#
#     def get_info(self):
#         return f"Foydalanuvchi logini=>{self.login}\nIsmi=>{self.name}\nFamiliyasi=>{self.lname}\nYoshi=>{self.age}\nTelefon nomeri=>{self.number}\nEmail=>{self.email}\nTug'ilgan yil=>{2025-self.age}"
#
# user1 = User("javohir6998", "javohir", "qurbonov", 24, "904466998", "javohir6998@gmail.com")
# # print(user1.get_info())
#
# print(user1.number)


# lesson2

# class Talaba:
#     """Talaba nomli klass"""
#
#     def __init__(self, name, surname, birth_date):
#         self.name = name.strip().capitalize()
#         self.surname = surname.strip().capitalize()
#         self.birth_date = birth_date
#         self.bosqich = 1
#
#     def get_info(self):
#         return f'{self.name}, {self.surname}, {self.birth_date} , {self.bosqich}-bosqich talabasi'
#
#     def update_bosqich(self):
#         self.bosqich += 1


# talaba1.update_bosqich()
# print(talaba1.get_info())

# class Fan:
#     """Fan nomli klass"""
#
#     def __init__(self, fan_nomi):
#         self.fan_nomi = fan_nomi.strip().capitalize()
#         self.talabalar_soni = 0
#         self.talabalar = []
#
#     def add_student(self, student_name):
#         self.talabalar.append(student_name)
#         self.talabalar_soni += 1
#
#     def get_students(self):
#         return list(talaba.get_info() for talaba in self.talabalar)
#
#
# matematika = Fan("Oliy Matematika")
# talaba1 = Talaba('javohir', 'qurbonov', 2001)
# talaba2 = Talaba('bahodir', 'qurbonov', 1995)
# talaba3 = Talaba('dilrabo', 'qurbonova', 1993)
#
# matematika.add_student(talaba1)
# matematika.add_student(talaba2)
# matematika.add_student(talaba3)

# print(matematika.talabalar_soni)
# print(matematika.talabalar)

# print(talaba1.name)
# print(matematika.get_students())

# print(dir(Talaba))

# def see_methods(klass):
#     return [method for method in dir(klass) if method.startswith('__') is False]
#
# print(see_methods(Talaba))

# print(see_methods(talaba2))

# print(talaba2.__dict__)
#
# class Avto:
#     """Avto nomli klass yaratamiz"""
#
#     def __init__(self, model, rang, karobka, narx, yil):
#         self.model = model
#         self.rang = rang
#         self.karobka = karobka
#         self.narx = narx
#         self.yil = yil
#         self.kilometr = 0
#
#     def get_model(self):
#         return f"Mashina modeli=>{self.model}"
#
#     def get_rang(self):
#         return f"Mashina ranggi => {self.rang}"
#
#     def get_karobka(self):
#         return f"Mashina karobka => {self.karobka}"
#
#     def get_narx(self):
#         return f"Mashina narx => {self.narx}"
#
#     def get_yil(self):
#         return f"Mashina yil => {self.yil}"
#
#     def get_kilometr(self):
#         return f"Mashina kilometr => {self.kilometr}"
#
#     def get_info(self):
#         return f"Mashina modeli =>{self.model} ,ranggi =>{self.rang}, karobka turi=> {self.karobka}, narxi=>{self.narx} , year =>{self.yil} , distance=>{self.kilometr}"
#
#     def set_rang(self, rang):
#         self.rang = rang
#         return self.rang
#
#     def update_km(self, kilometr):
#         self.kilometr = kilometr
#         return self.kilometr
#
#
# class Avtosalon:
#     """Avtosalon class"""
#
#     def __init__(self, salon_nomi, manzili, tel_number):
#         self.salon_nomi = salon_nomi
#         self.manzili = manzili
#         self.avtomobillar = []
#         self.tel_number = tel_number
#
#     def add_car(self, new_car):
#         self.avtomobillar.append(new_car)
#         return self.avtomobillar
#
#     def get_info_car(self):
#         return list(car.get_info() for car in self.avtomobillar)
#
# avto1 = Avto('sedan', 'oq', 'avtomat', 12_000, 2025)
# avto2 = Avto('hechbek', 'qora', 'mexanika', 11_000, 2022)
# update_distance=avto2.update_km(48225)
# # print(avto1.get_info())
#
# salon1 = Avtosalon("Java", 'Olmazor', 904466998)
# salon1.add_car(avto1)
# salon1.add_car(avto2)
# # print(salon1.get_info_car())
#
# # print(Avtosalon.__dict__)
# print(dir(int))


# -------------------------------------Vorislik-polimorfizm------------------------------------------
#
# class Shaxs:
#     """Shaxs haqida ma'lumot"""
#     odamlar_soni=0
#     __universitet="Tatu"
#     def __init__(self, ism, familiya, passport, tyil):
#         self.ism = ism.strip().capitalize()
#         self.familiya = familiya.strip().capitalize()
#         self.passport = passport.strip().upper()
#         self.tyil = tyil
#         Shaxs.odamlar_soni += 1
#
#     def get_info(self):
#         # info=f"Ism =>{self.ism}\nFamiliya =>{self.familiya}\nPassport =>{self.passport}\nTYIL =>{self.tyil}"
#         info = f"Ism=>{self.ism}\nFamiliya=>{self.familiya}\n"
#         info += f"Passport=>{self.passport}\nTYIL=>{self.tyil}"
#         return info
#
#     def get_age(self):
#         return f"Siz {2026 - self.tyil}-yoshdasiz"
#
#     @classmethod
#     def change_universitet(cls, ism):
#         Shaxs.__universitet = ism.strip().capitalize()
#         return f"Unniversitetni yangilangan nomi=>{Shaxs.__universitet}"
#
#
# inson=Shaxs("javohir","qurbonov","ab8603868", 2001)
# print(Shaxs.change_universitet('inha'))
# print(Shaxs.odamlar_soni)
# # print(inson.get_age())
#
# class Talaba(Shaxs):
#     """Talaba haqida ma'lumot"""
#
#     def __init__(self, ism, familiya, passport, tyil, kurs):
#         """Talabaning xususiyatlari"""
#         super().__init__(ism, familiya, passport, tyil)
#         self.kurs = kurs
#         self.fanlar = []
#
#     def fanga_yozil(self, fan):
#         if isinstance(fan, Fan):
#             self.fanlar.append(fan)
#         else:
#             print("Fan klassidagi obyektlarni yuboring!!!")
#
#     def get_fanlar(self):
#         return [fan.fan_nomi for fan in self.fanlar]
#
#     def remove_fan(self, fan):
#         if fan in self.fanlar:
#             self.fanlar.remove(fan)
#         else:
#             print("Siz bu fanga yozilmagansiz!!!")
#
#     def get_info(self):
#         info = super().get_info()
#         return f"{info} ,\nKurs =>{self.kurs} ,\n{[fan.fan_nomi for fan in self.fanlar]}"
#
#
# class Professor(Shaxs):
#     """Professor haqida ma'lumot"""
#     def __init__(self, ism, familiya, passport, tyil, ilmiy_darajasi):
#         super().__init__(ism, familiya, passport, tyil)
#         self.ilmiy_darajasi = ilmiy_darajasi.strip().capitalize()
#         self.tajriba_yili=10
#
#     def get_info(self):
#         info1=super().get_info()
#         return f"{info1},\nIlmiy darajasi=>{self.ilmiy_darajasi},\nTajribasi=>{self.tajriba_yili}"
#
# prof=Professor('muhriddin','muhiddinov','ac45678945',1990, 'dotsent')
# # print(prof.get_info())
#
# class Shogird(Professor):
#     """Shogird haqida ma'lumot"""
#     def __init__(self, ism, familiya, passport, tyil, ilmiy_darajasi, oqish_joyi):
#         super().__init__(ism, familiya, passport, tyil, ilmiy_darajasi)
#         self.oqish_joyi = oqish_joyi
#
#     def get_info_shogird(self):
#         info2=super().get_info()
#         return f"{info2} ,\nO'qish joyi=>{self.oqish_joyi} ,\n"
#
#     def ban_user(self):
#         print("Foydalanuvchi bloklandi!!!")
#
# shogird = Shogird("bahodir", "qurbonov", "ab1245678", 1995, 'magistr','tatu')
# # print(shogird.ban_user())
#
#
#
#
# class Fan:
#     """Fan haqida ma'lumot"""
#
#     def __init__(self, fan_nomi, chiqarilgan_yili, betlar_soni):
#         self.fan_nomi = fan_nomi.strip().capitalize()
#         self.chiqarilgan_yili = chiqarilgan_yili
#         self.betlar_soni = betlar_soni
#
#
# fan1 = Fan("matematika", 2015, 221)
# fan2 = Fan("english", 2019, 180)
# fan3 = Fan("fizika", 2021, 215)
#
# talaba1 = Talaba("bahodir", "qurbonov", "ab1245678", 1995, 4)
# talaba1.fanga_yozil(fan1)
# talaba1.fanga_yozil(fan2)
# # print(talaba1.get_fanlar())
# talaba1.remove_fan(fan2)
# # print(talaba1.get_info())
#

# ----------------------------------------INKAPSULYATSIYA-----------------------------------------------
#
# from uuid import uuid4
#
#
# class Avto:
#     """Avtomobil klassi"""
#
#     __num_avto = 0
#     def __init__(self, make, model, color, year, price, km):
#         self.make = make
#     def __init__(self, make, model, color, year, price, km=0):
#         """Avtomobil xususiyatlari"""
#         self.make = make
#         self.model = model
#         self.color = color
#         self.year = year
#         self.price = price
#         self.__km = km
#         self.__id = uuid4()
#         Avto.__num_avto += 1
#
#     def get_km(self):
#         return self.__km
#
#     def get_id(self):
#         return self.__id
#
#     def update_km(self, km):
#         """Mashina masofasini o'zgartitish"""
#         if km > self.__km:
#             self.__km += km
#         else:
#             print("Mashina masofasini kamaytirib bo'lmaydi!!!")
#
#     @classmethod
#     def get_avto_num(cls):
#         return cls.__num_avto
#
#     def get_info(self):
#         return {
#             "make": self.make,
#             "model": self.model,
#             "color": self.color,
#             "year": self.year,
#             "price": self.price,
#             "distance": self.__km,
#             "id": self.__id
#         }
#
# car=Avto('chevrolet','cobalt', 'white', 2020, 10_000, 48_000)
# car.update_km(50_000)
# # print(Avto.get_avto_num())
#


# --------------------------------------DUNDER METODLAR---------------------------------------

#
# class Avto:
#     """Avtomobil klassi"""
#
#     __num_avto = 0
#
#     def __init__(self, make, model, color, year, price):
#         """Avtomobil xususiyatlari"""
#         self.make = make
#         self.model = model
#         self.color = color
#         self.year = year
#         self.price = price
#         Avto.__num_avto += 1
#
#     def __repr__(self):
#         """Obyekt haqida ma'lumot"""
#         return f"Avto:\nMake=> {self.make} \nModel=> {self.model}\nColor=> {self.color}\nYear=> {self.year}\nPrice=> {self.price}"
#
#     def __str__(self):
#         return f"{self.make} {self.model} {self.color} {self.year} {self.price}"
#
#     def __eq__(self, other_avto):
#         return self.price == other_avto.price
#
#     def __lt__(self, other_avto):
#         return self.price < other_avto.price
#
#     def __gt__(self, other_avto):
#         return self.price > other_avto.price
#
#     def __le__(self, other_avto):
#         return self.price <= other_avto.price
#
#
# # car=Avto('chevrolet','cobalt', 'white', 2020, 12_000)
# # car2=Avto('chevrolet','lacetti', 'black', 2021, 15_000)
# # print(len(car))
#
# class AvtoSalon:
#     def __init__(self, name):
#         self.name = name
#         self.cars = []
#
#     def __repr__(self):
#         return f"AvtoSalon nomi=> {self.name}\nMashinalar=>{self.cars}"
#
#     def __len__(self):
#         return len(self.cars)
#
#     def __getitem__(self, index):
#         return self.cars[index]
#
#     def __setitem__(self, index, value):
#         if isinstance(value, Avto):
#             self.cars[index] = value
#
#     def add_avto(self, avto):
#         if isinstance(avto, Avto):
#             self.cars.append(avto)
#         else:
#             print("Avto obyektini kiriting!!!")
#
#
# car = Avto('chevrolet', 'cobalt', 'white', 2020, 12_000)
# car2 = Avto('chevrolet', 'lacetti', 'black', 2021, 15_000)
# salon = AvtoSalon("Javohir_Avto")
# for c in [car, car2]:
#     salon.add_avto(c)
# # print(len(salon))
#
# print(salon[0])

# --------------------------------Fayllar bilan ishlash----------------------------------

# with open('pi.txt') as fayl:
#     pi = fayl.read()
#     pi= pi.rstrip()
#     pi= pi.replace('\n','')
#     pi= float(pi)
#     print(pi)


# file=open('pi.txt')
# pi=file.read()
# print(pi)
# file.close()

# with open('pi.txt') as file:
#      numbers=file.readlines()
# print(numbers)

# with open('pi.txt') as file:
#     numbers=[number.rstrip() for number in file]
#     print(numbers)

# with open('pi.txt','w') as file:
#     file.write("hello")
# print(file)

# file_name='new.txt'
# name='javohir'
# surname='qurbonov'
# age=24
# with open(file_name,'w') as file:
#     file.write(name.capitalize()+'\n')
#     file.write(surname.capitalize())
#     file.write(str(age)+'\n')
# print(file)

# with open('new.txt','a+') as file:
#     file.write('Navoiy viloyati')
# print(file)

# import pickle
#
# student1={'name':'elbek','surname':'razzokov','birt_date':'12.09.2001','kurs':1}
# with open("students","wb") as file:
#     pickle.dump(student1,file)

# with open('C:\\Users\\javoh\\Desktop\\data.txt') as file:
#     file=file.read()
# #     print(file)
#

# def izla(number):
#     result=''
#     with open('C:\\Users\\javoh\\Downloads\\pi_1000_digits.txt','r') as file:
#         pi=file.read()
#         pi=pi.strip()
#         pi=pi.replace('\n ',' ')
#         if str(number) in pi:
#             result='bor'
#         else:
#             result='yoq'
#     return result
# print(izla(12092001))


# def fill_information(name,surname,age):
#     file_name='information.txt'
#     with open(file_name,'a') as fayl:
#         fayl.write(name+'\n')
#         fayl.write(surname+'\n')
#         fayl.write(str(age)+'\n')
#     return file_name
#
# count=0
# while True:
#     name=input(f"{count+1}:Enter your name:")
#     surname=input(f"{name.capitalize()} enter your surname:")
#     age=int(input(f"{name.capitalize()} enter your age:"))
#     count+=1
#     data = fill_information(name, surname, age)
#     ask=input("Do you add any person?(y/n)")
#     if ask=="n":
#         break
#
# print(data)

# import json

# x = {'name': 'javohir',
#      'email': 'javohir5592272@gmail.com',
#      'phone':None}
# with open('data.json', 'w') as outfile:
#     json.dump(x, outfile)
# with open('data.json', 'r') as f:
#     file=json.load(f)
# print(type(file))

# data={'Model':'Malibu','Rang':'Qora','Yil':2020,'Narx':40_000}
# with open('data.json','w') as f:
#     json.dump(data,f)
#
# with open('data.json') as f:
#     data = json.load(f)
# print(data['Rang'])


# import datetime as dt
# bugun=dt.date.today()
# keyingi=dt.date(2026,2,5)
# while bugun<=keyingi:
#     bugun=bugun+dt.timedelta(days=1)
#     print(bugun)

# import datetime as dt
# today = dt.date.today()
# ramadan=dt.date(2026,2,17)
# hayit=dt.date(2026,3,17)
# while today<=ramadan:
#     today=today+dt.timedelta(days=1)
#     print(today)
# while today<=hayit:
#     today=today+dt.timedelta(days=1)
#     print(today)

# print(today)




