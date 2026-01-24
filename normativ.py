# # 1--------------------print-----------------------
from calendar import month

# print("\"O'zbekiston Vatan\"im meni!!!")

# # 2

# import math
# tezlik=float(input("Tezlikni kiriting(km/h):"))
# masofa=float(input("Masofani kiriting(km):"))
# vaqt=masofa/tezlik
# soat=int(vaqt)
# minut=(vaqt-soat)*60
# print(f"Mashina {tezlik} tezlikda {masofa} masofani {soat} soat {math.ceil(minut)} minutda bosib o'tadi")

# # 3

# # topshiriq-1: 'print()' funksiyasidan foydalanib satrni chiqardik.
# # topshiriq-2: Tezlik va masofani qabul qilib, mashina qancha vaqtda bosib o'tishini aniqladik.
# # topshiriq-3: Dasturlarga izoh yozdik.
# # topshiriq-4: Bu topshiriqda xatoliklarni to'g'irladik.
# # topshiriq-5: a va b qiymat qabul qilib qiymatini almashtirib chiqardik.
# # topshiriq-6: Berilgan ma'lumotlarni matn ko'rinishida chiqardik va upper(),lower(),title() va capitalize() metodlaridan foydalandik.
# # topshiriq-7: Bu topshiriqda arifmetik operatorlardan foydalandik.

# # 4

# print("Notes from Day 1")
# print("The print statement is used to output strings")
# print("Strings are strings of characters")
# print("String Concatenation is done with the + sign")
# print("New lines can be created with a \ and the letter n")

# # 5

# a=float(input("A qiymatni kiriting:"))
# b=float(input("B qiymatni kiriting:"))
# a1=a
# a=b
# b1=a1
# print(f"A ga {a1} qiymat kiritilganda natija=>{a}")
# print(f"B ga {b} qiymat kiritilganda natija=>{b1}")

# # 6

# kocha="Bog'bon"
# mahalla="Sog'bon"
# tuman="Bodomzor" 
# viloyat="Samarqand"
# print(f"\"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloayti\"")


# manzil=f"\"{kocha.title()} ko'chasi, {mahalla.upper()} mahallasi, {tuman.lower()} tumani, {viloyat.capitalize()} viloayti\""
# print(manzil)

# # 7

# a=int(input("1-chi sonni kiriting:"))
# b=int(input("2-chi sonni kiriting:"))

# print(f"{a}+{b}={a+b}")
# print(f"{a}-{b}={a-b}")
# print(f"{a}*{b}={a*b}")
# print(f"{a}/{b}={a/b}")
# print(f"{a}//{b}={a//b}")
# print(f"{a}**{b}={a**b}")


# ------------------------------list-------------------------------

# # a

# ismlar=[]
# ismlar.append("Javohir")
# ismlar.append("Elbek")
# ismlar.append("Bahodir")
# print(ismlar)

# # # b

# ismlar=[]
# ismlar.append("Javohir")
# ismlar.append("Elbek")
# ismlar.append("Bahodir")
# print(ismlar)

# ismlar[0]="Ahror"
# ismlar[2]="Dilrabo"
# print(ismlar)

# # # c

# ismlar=["Onix","Gentra","Cobalt","Spark","Matiz","Malibu"]

# # # .pop() bu metodga list ichidagi elementning indeksini berish orqali sug'urib olinadi va sug'urib olingan elementni biror o'zgaruvchiga yuklab qo'ysa bo'ladi.Agar indeks kiritilmasa oxirgi elementni sug'urib oladi.

# x=ismlar.pop(2)
# print(ismlar,x)

# # # del orqali listagi elementni indeksi orqali o'chiriladi.Agar element indeksini kiritmasak listni butunlay o'chirib tashlaydi.

# del ismlar[0]
# print(ismlar)

# # # .remove() metodi orqali listdagi elementni nomi bilan o'chirsak bo'ladi.Albatta o'chirmoqchi bo'lgan elementimizni nomini to'g'ri va listdagi bilan bir xil holatda kiritishimmiz kerak. 

# ismlar.remove("Onix")
# print(ismlar)



# # # d

# cars=["Onix","Gentra","Cobalt","Spark","Matiz","Malibu"]

# other_cars=cars.copy()
# # other_cars=cars[:]

# print(cars)
# print(other_cars)


# # # e

# ismlar=["Javohir","Sohib","Ahror","Bahodir","Elbek","Akbar","Otabek","Eldor","Shahlo,","Lobar"]

# yaqinlar=ismlar.copy()
# yaqinlar.sort()

# print(ismlar)
# print(yaqinlar)

# # # .sort() metodi dastlabki listni elementlarini tartiblaydi
# # # sorted() funksiyasi yangi listga elementlarni tartib bilan joylashtiradi va list,tuple,set larda ham ishlaydi
# print(sorted(yaqinlar))

# # # f

# numbers=list(range(1,101))

# # 1 dan 100 gacha sonlar
# print(numbers)

# # 100 dan 1 gacha sonlar
# print(numbers[::-1])

# boshi=numbers[0:10]
# oxiri=numbers[-10:]
# ortasi=numbers[int(len(numbers)/2-6):int(len(numbers)/2+5)]

# new_list=[]
# new_list.append(boshi)
# new_list.append(ortasi)
# new_list.append(oxiri)
# # print(new_list)

# new_list_numbers=[]
# for i in new_list:
#     for j in i:
#         new_list_numbers.append(j)
# print(new_list_numbers)


# # 1.2-tuple
# # a

# sonlar=tuple(range(1,11))
# print(sonlar)

# # b

# print(sonlar[3:7])

# # c

# numbers=list(sonlar).copy()
# numbers[5]=12
# numbers[8]=23
# print(sonlar)
# print(numbers)


# --------------------------------IF----------------------------------

# # 1.1IF

# # a

# temperature=float(input("Haroratni kiriting:"))
# if temperature<0:
#     print("Sovuq kun, issiqroq kiying!")
# elif temperature>0 and temperature<20:
#     print("Ob-havo yaxshi, lekin sal sovuq.")
# elif temperature>=20:
#     print("Juda yaxshi ob-havo, zavqlaning!")

# # b

# age=int(input("Futbolchini yoshini kiriting:"))
# goal=int(input("Gollar sonini kiriting:"))

# if age<18 and goal>=1:
#     print("Yosh iste’dod!")
# elif age<18 and goal==0:
#     print("Mashq qilish kerak.")

# if (age>=18 and age<35) and goal>=3:
#     print("Yulduz futbolchi!")
# elif (age>=18 and age<35) and goal==0:
#     print("Oddiy futbolchi.")

# if age>=35 and goal>=1:
#     print("Mag‘lubiyatsiz veteran!")
# elif age>=35 and goal==0:
#     print("Tajribali murabbiy.")



# -----------------------------For----------------------------

# a

# sonlar=[1,2,7,10,8]
# maxx=sonlar[0]
# for i in sonlar:
#     if maxx<i:
#         maxx=i
# print(maxx)

# # b

# sonlar=[1,2,7,10,8]
# yigindi=0
# for son in sonlar:
#     yigindi+=son
# print(yigindi)

# # c

# for i in list(range(1,10)):
#     print(" ")
#     for j in list(range(1,11)):
#         print(f"{i}*{j}={i*j}")


# ------------------------------------dict------------------------------------

# a

# talaba_baholari={
#     "Javohir":{'Math':5,"English":4,"Physics":4},
#     "Bahodir":{'Math':4,"English":5,"Physics":3},
#     "Dilrabo":{'Math':3,"English":5,"Physics":4},
#     "Sohib":{'Math':4,"English":3,"Physics":4},
# }
# print(talaba_baholari)

# # b

# talaba_baholari["Ahror"]={'Math':4,"English":3,"Physics":3}
# talaba_baholari.update({"Ahror":{'Math':4,"English":3,"Physics":3}})
# print(talaba_baholari)

# # c

# # del operatori lug'atni kaliti bilan o'chiradi va qiymat qaytarmaydi.Agar to'g'ri kalit kiritilmasa xatolik beradi.

# del talaba_baholari["Sohib"]
# print(talaba_baholari)

# # .pop metodi orqali o'chirilgan qiymatni biror o'zgaruvchiga ta'minlab qo'ysa bo'ladi.Agar to'g'ri kalit kiritilmasa xatolik beradi.

# talaba_baholari.pop("Sohib")
# print(talaba_baholari)

# # d

# for k,v in talaba_baholari.items():
#     print(k)
#     for i,j in v.items():
#         print(i,j,end=" | ")
#     print(" ")
#     print(" ")

# # e

# talaba_baholari["Dilrabo"]['Math']=4
# print(talaba_baholari)

# # f

# ortacha_baho={}
# for k,v in talaba_baholari.items():
#     summ_baho=0
#     count=0
#     for i,j in v.items():
#         summ_baho+=j
#         count+=1
#     ortacha=summ_baho/count
#     ortacha_baho[k]=round(ortacha,1)
# print(ortacha_baho)

# # f.1
# ortacha_baho={}
# for k,v in talaba_baholari.items():
#     ball=[]
#     for f,b in v.items():
#         ball.append((b))
#     ortacha_baho[k]=round(sum(ball)/len(ball),1)
# print(ortacha_baho)

# # g

# ortacha_baho={}
# for k,v in talaba_baholari.items():
#     ball=[]
#     for f,b in v.items():
#         ball.append((b))
#     ortacha_baho[k]=round(sum(ball)/len(ball),1)

# for k,v in ortacha_baho.items():
#     if v<4:
#         print(f"{k} yiqildingiz")
#     else:
#         print(f"{k} tabriklayman o'tdingiz!!!")


# --------------------------------Set--------------------------------

# a

# bosh_toplam=set()
# print(type(bosh_toplam))

# # b

# bosh_toplam=set()
# bosh_toplam.update([4,35,12,78,31,23,10,8,45,89])
# print(bosh_toplam)

# # c

# bosh_toplam=set()
# bosh_toplam.update([4,35,12,78,31,23,10,8,45,89])
# # .remove metodi bilan element o'chirilganda element topilmasa xatolik beradi
# bosh_toplam.remove(12)
# print(bosh_toplam)

# # .discard() metodi bilan element o'chirilganda topilmasa xatolik bermaydi.
# bosh_toplam.discard(89)
# print(bosh_toplam)

# # d

# toplam_1 = {1, 2, 3, 4, 5}
# toplam_2 = {4, 5, 6, 7, 8}
#
# print(toplam_1.union(toplam_2))
#
# print(toplam_1.intersection(toplam_2))
#
# print(toplam_1.difference(toplam_2))
#
# print(toplam_1.symmetric_difference(toplam_2))
#
# print(toplam_1==toplam_2)



#------------------------Normativ 2-modul--------------------------------
# 15-16
# # 1
#
# products = {
#     'adrenaline': {'narxi': 200, 'soni': 20},
#     'coca-cola': {'narxi': 10000, 'soni': 30},
#     'morojniy': {'narxi': 20000, 'soni': 10},
#     'non' : {'narxi':5000,'soni':200}
# }
#
#
#
# def add_product(product_name,product_price,product_quantity):
#
#     name = product_name.strip().lower()
#     price = int(product_price)
#     quantity = int(product_quantity)
#     if price > 0 and quantity > 0:
#         if name not in products.keys():
#             products[name] = {'narxi': price, 'soni': quantity}
#             products_list()
#             print("Mahsulot qo'shildi!!!")
#         else:
#             products[name]['soni'] += quantity
#             products_list()
#     else:
#         print("Ma'lumot kiritishda xatolik.Qaytadan urinib ko'ring!!!")
#         products_list()
#
#
# def get_out_product(product_name,product_quantity):
#
#     if product_name not in products.keys():
#         print(f"Bizda {product_name}-mahsuloti mavjud emas!!!")
#     elif product_quantity<products[product_name]['soni']:
#         products[product_name]['soni'] -= product_quantity
#         print(f"{product_name}-mahsulotidan {products[product_name]['soni']}-ta qoldi")
#     else:
#         print(f"Afsuski {product_name}-mahsulotidan {products[product_name]['soni']}-ta mavjud!!!")
#         try:
#             while True:
#                 question=input("Mahsulotni borini olasizmi?(y/n)")
#                 if question=='y':
#                     products[product_name]['soni'] -= products[product_name]['soni']
#                     if products[product_name]['soni'] == 0:
#                         products.pop(product_name,None)
#                     products_list()
#                     break
#         except ValueError:
#             print("Tog'ri bo'limni tanlang!")
#
#
# def products_list():
#     print(f"{'Mahsulot nomi':<15} | {'Narxi':<12} | {'Miqdori':<12} | {'Umumiy summa':<14}")
#     print("-" * 65)
#     for k, v in products.items():
#         print(f"{k.title():<15} | {v['narxi']:<12} | {v['soni']:<12} | {v['narxi'] * v['soni']:<14}")
#
#
# def input_data():
#     while True:
#         back_to_menu=False
#         try:
#             command=int(input("1.Mahsulot qo'shish\n2.Mahsulot olib chiqish\n3.Mahsulotlar ro'yxati\n0.Chiqish\nBo'limni tanlang:"))
#             if command not in [0,1,2,3]:
#                 print("\nTog'ri bo'limni tanlang!\n")
#                 continue
#             if command==0:
#                 print("Dastur tugadi!!!")
#                 break
#             if command==1:
#                 while True:
#                     print("\n---MAHSULOT QO'SHISH BO'LIMI---\n")
#                     product_name = input("Mahsulot nomini kiriting('exit'-chiqish):")
#                     if product_name=='exit':
#                         back_to_menu=True
#                         break
#                     try:
#                         product_price=int(input("Mahsulot narxini kiriting('exit'-chiqish):"))
#                         if product_price=='exit':
#                             back_to_menu = True
#                             break
#                         product_quantity=int(input("Mahsulot miqdorini kiriting('exit'-chiqish):"))
#                         if product_quantity=='exit':
#                             back_to_menu = True
#                             break
#                         add_product(product_name, product_price, product_quantity)
#                     except ValueError:
#                         print("Ma'lumot kiritishda xatolik!")
#                         ask=input("Yana mahsulot kiritasizmi?(y/n)")
#                         if ask=='n':
#                             break
#                 if back_to_menu:
#                     continue
#
#             if command == 2:
#                 while True:
#                     print("\n---MAHSULOT OLIB CHIQISH BO'LIMI---\n")
#                     product_name = input("Mahsulot nomini kiriting('exit'-chiqish):")
#                     if product_name == 'exit':
#                         back_to_menu = True
#                         break
#                     try:
#                         product_quantity = int(input("Mahsulot miqdorini kiriting('exit'-chiqish):"))
#                         if product_quantity == 'exit':
#                             back_to_menu = True
#                             break
#                         get_out_product(product_name, product_quantity)
#                     except ValueError:
#                         print("Ma'lumot kiritishda xatolik!")
#                         ask = input("Yana mahsulot olib chiqasizmi?(y/n)")
#                         if ask == 'n':
#                             break
#                 if back_to_menu:
#                     continue
#
#             if command == 3:
#                 while True:
#                     print("\n---MAHSULOTLAR RO'YXATI BO'LIMI---\n")
#                     products_list()
#                     question=input("Menyuga qaytasizmi?(y/n)")
#                     if question == 'y':
#                         back_to_menu = True
#                         break
#
#                 if back_to_menu:
#                     continue
#
#             return command
#         except ValueError:
#             print("Tog'ri bo'limni tanlang!")
#             question=input("Menyuga qaytasizmi?(y/n)")
#             if question=='n':
#                 break
#
# input_data()
#

# # 2
# 17-18
# class User:
#     """Foydalanuvchi haqida ma'lumot beruvchi klass"""
#     def __init__(self, firstname, lastname, username, email, phone=None, bio=None):
#         self.firstname = firstname.title()
#         self.lastname = lastname.title()
#         self.username = username
#         self.email = email
#         self.phone = phone
#         self.bio = bio
#
#     def get_full_name(self):
#         return f"{self.firstname} {self.lastname}"
#
#     def get_info(self):
#         return f"Ism:{self.firstname}\nFamiliya:{self.lastname}\nUsername:{self.username}\nEmail:{self.email}\nPhone:{self.phone}\n"
#
#     def update_email(self,new_email):
#         self.email=new_email
#         return self.email
#
#     def update_phone(self,new_phone):
#         self.phone=new_phone
#         return self.phone
#
# obj1=User("javohir",'qurbonov','java_coder','javohir5592272@gmail.com','904466998')
# obj2=User('sohib','rahmatov','sohib7474','sohib@gmail.com')
# print(obj1.get_info())
#
# obj2.update_phone(934557585)
# print(obj2.get_info())
#
# obj1.update_phone(333231003)
# print(obj1.get_info())


# class User:
#     """Foydalanuvchi haqida ma'lumot beruvchi klass"""
#
#     def __init__(self, firstname, lastname, username, email, phone=None, bio=None):
#         self.firstname = firstname.title()
#         self.lastname = lastname.title()
#         self.username = username
#         self.email = email
#         self.phone = phone
#         self.bio = bio
#
#     def get_full_name(self):
#         return f"{self.firstname} {self.lastname}"
#
#     def get_info(self):
#         return (
#             f"Ism: {self.firstname}\n"
#             f"Familiya: {self.lastname}\n"
#             f"Username: {self.username}\n"
#             f"Email: {self.email}\n"
#             f"Phone: {self.phone}\n"
#             f"Bio: {self.bio}\n"
#         )
#
#     def update_email(self, new_email):
#         self.email = new_email
#
#     def update_phone(self, new_phone):
#         self.phone = new_phone
#
#
# obj1 = User("javohir", "qurbonov", "java_coder", "javohir@gmail.com", "904466998", "Python backend developer")
# obj2 = User("sohib", "rahmatov", "sohib7474", "sohib@gmail.com")
#
# print(obj1.get_info())
#
# obj2.update_phone("934557585")
# obj2.update_email("new_sohib@gmail.com")
#
# print(obj2.get_info())

# 13-14

# month_names=['yanvar','fevral','mart','aprel','may','iyun','iyul','avgust','sentyabr','oktyabr','noyabr','dekabr']
# unpaid_month=[]
# month_number=1
# paid_month=0
# unpaid=0
# while month_number<=12:
#     status=input(f"{month_names[month_number-1].title()}-oyi uchun ijarani to'ladingizmi?(y/n)(chiqish-'exit')")
#     if status=='exit':
#         break
#     if status.lower() in ['y','n']:
#         if status=="y":
#             paid_month+=1
#         else:
#             unpaid_month.append(month_names[month_number-1].title())
#             unpaid+=1
#         month_number+=1
#     else:
#         print("Iltimos 'y' or 'n' ikkisidan birini kiriting!")
#         continue
# print(f"Siz {paid_month}-oy uchun to'ladingiz!"
#       f"{unpaid_month}-oylar uchun ijarani to'lamadingiz!")

# extra

# month_names = [
#     'yanvar','fevral','mart','aprel','may','iyun','iyul','avgust','sentyabr','oktyabr','noyabr','dekabr']
#
# unpaid_months = []
# month_number = 1
# paid_months = 0
#
# while month_number <= 12:
#     try:
#         status = input(f"{month_names[month_number-1].title()} oyi uchun ijarani to'ladingizmi? (y/n)(chiqish-'exit'): ")
#
#         if status.lower() == 'exit':
#             break
#
#         if status.lower() not in ['y', 'n']:
#             raise ValueError("Noto‘g‘ri qiymat")
#
#         if status.lower() == 'y':
#             paid_months += 1
#         else:
#             unpaid_months.append(month_names[month_number-1].title())
#
#         month_number += 1
#
#     except ValueError:
#         print("Iltimos faqat 'y' yoki 'n' kiriting!")
#
# print(f"Siz {paid_months} oy ijarani to‘ladingiz.")
# print(f"To‘lanmagan oylar: {unpaid_months}")


#15-16

# from abc import ABC,abstractmethod
#
# class Computer(ABC):
#     """Computer class"""
#     total_computers=0
#
#     def __init__(self, brand, model, year, price):
#         self.brand=brand
#         self.model=model
#         self.year=year
#         self.price=price
#         Computer.total_computers+=1
#
#     @abstractmethod
#     def display_info(self):
#         pass
#
#     @classmethod
#     def get_total_computers(cls):
#         return f"Jami kompyuterlar:{cls.total_computers}"
#
# class Monoblock(Computer):
#     """Monoblock class"""
#     def __init__(self, brand, model, year, price,screen_size):
#         super().__init__(brand,model,year,price)
#         self.screen_size=screen_size
#
#     def display_info(self):
#         return f"Brand:{self.brand}\nModel:{self.model}\nYear:{self.year}\nPrice:{self.price}\nScreen:{self.screen_size}"
#
# class Notebook(Computer):
#     """Notebook class"""
#     def __init__(self, brand, model, year, price, battery_life):
#         super().__init__(brand,model,year,price)
#         self.battery_life=battery_life
#
#     def display_info(self):
#         return f"Brand:{self.brand}\nModel:{self.model}\nYear:{self.year}\nPrice:{self.price}\nBattery:{self.battery_life}"
#
#
# obj1=Monoblock('Apple','iMac',2022,1500,27)
# obj2=Notebook('Lenovo','Thinkpad',2024,900,8)
# print(obj1.display_info())
# print(obj2.display_info())
# print(Computer.get_total_computers())


# 17

from abc import ABC,abstractmethod
from itertools import product


class Computer(ABC):
    """Computer class"""
    total_computer=0
    def __init__(self, brand, model, year, price):
        self.brand=brand
        self.model=model
        self.year=year
        self._price=price
        Computer.total_computer+=1

    @abstractmethod
    def display_info(self):
        pass

    @classmethod
    def get_total_computers(cls):
        return f"Jami kompyuterlar:{cls.total_computer}"

    def get_price(self):
        return f"Narxi:{self._price}"

    def set_price(self,price):
        if price<0:
            raise ValueError("Narx manfiy bo'lishi mumkin emas!")
        else:
            self._price=price

    def __gt__(self, other):
        return self._price > other._price

    def __repr__(self):
        return f"Brand:{self.brand}\nModel:{self.model}\nYear:{self.year}\nPrice:{self._price}"

class Monoblock(Computer):
    """Monoblock class"""
    def __init__(self,brand,model,year,price, screen_size):
        super().__init__(brand,model,year,price)
        self.screen_size=screen_size

    def display_info(self):
        return f"Brand:{self.brand}\nModel:{self.model}\nYear:{self.year}\nPrice:{self._price}\nScreen:{self.screen_size}"

class Notebook(Computer):
    """Notebook class"""
    def __init__(self,brand,model,year,price, battery_life):
        super().__init__(brand,model,year,price)
        self.battery_life=battery_life

    def display_info(self):
        return f"Brand:{self.brand}\nModel:{self.model}\nYear:{self.year}\nPrice:{self._price}\nScreen:{self.battery_life}"


class Factory:
    """Factory class"""
    total_factories=0
    def __init__(self,name):
        self.name=name
        self.products=[]
        Factory.total_factories+=1

    def add_product(self,product):
        if isinstance(product,Computer):
            self.products.append(product)
        else:
            raise ValueError("Kompyuter klassidan emas!")
    def __repr__(self):
        return f"{self.name}({self.products})"
    def list_products(self):
        return f"Zavodda mavjud mahsulotlar:{self.products}"

    @classmethod
    def get_total_factories(cls):
        return f"Jami yaratilgan zavodlar soni:{cls.total_factories}"

obj1 = Monoblock('Apple', 'iMac', 2022, 1500, 27)
obj2 = Notebook('Lenovo', 'Thinkpad', 2024, 900, 8)
obj3 = Monoblock('Asus', 'TUF GAMING', 2023, 800, 15)
factory1=Factory("Lenovo")
factory1.add_product(obj2)
factory1.add_product(obj3)
factory2=Factory("Apple")
factory2.add_product(obj1)
print(factory1.list_products())
print(Factory.get_total_factories())
print(obj1<obj2)
print(factory1.list_products())
print(factory1)


# print(obj1.display_info())
# print(obj2.display_info())
# print(Computer.get_total_computers())



# print(obj2)







