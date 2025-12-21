# def nurolloh_data(name,age,*hobbiy):
#     dicts={
#     "Ism":name.title(),
#     "Yosh":age,
#     "Hunar":hobbiy
#     }

#     qiymatlar=[]
#     for v in dicts.values():
#         if type(v)!=tuple:
#             qiymatlar.append(v)
#         else:
#             for i in v:
#                 qiymatlar.append(i)
#     return qiymatlar

# print(nurolloh_data("nurulloh",20,'nos','elektron sigara','pubg','cs go','gta5'))



# Homework

# 1

# kocha="bog'bon"
# mahalla="Sog'bon"
# tuman="BoDomzor"
# viloayat="samarqand"

# print(f"Ko'cha=>{kocha.title()}\nMahalla nomi=>{mahalla.upper()}\nTuman nomi=>{tuman.casefold()}\nViloyat nomi=>{viloayat.capitalize()}")

# 2

# age=int(input("Yoshingizni kiriting=>"))
# print(f"Siz {2025-age}-yilsiz!!!")

# 3

# ismlar=["sohib","elbek","ahror"]
# print(f"{ismlar[0].capitalize()} NKMK da ishlaydi.\n{ismlar[1].capitalize()} TDIDU da o'qiydi.\n{ismlar[2].capitalize()} Navoiy Azotda ishlaydi")

# 4

# taomlar=['manti','osh','qovurilgan tuxum','shashlik','somsa']
# nonushta=taomlar.copy()
# i=len(nonushta)-1
# while i>=0:
#     if nonushta[i]!="osh" and nonushta[i]!="qovurilgan tuxum":
#         del nonushta[i]
#     i-=1
# print(nonushta)

# 5

# toq_sonlar=list(range(11,100,2))
# kubik_sonlar=[]
# for n in toq_sonlar:
#     kubik_sonlar.append(n**3)
# print(f"{toq_sonlar}\n{kubik_sonlar}")

# 6

# cars=['toyota','mazda','hyundai','gm','kia']
# for car in cars:
#     if car=='gm':
#         print(car.upper())
#     else:
#         print(car.title())

# 7

# number=float(input("Sonni kiriting:"))
# if number>0:
#     print(f"{number} sonining kvadrati=>{number**2} ga teng.")
# else:
#     print("Musbat son kiriting!!!")

# 8

# age=int(input("Yoshingizni kiriting=>"))
# if age<=4 or age>=60:
#     print("Sizga chipta tekin!!!")
# elif age<=18:
#     print("Sizga chipta 10.000")
# else:
#     print("Chipta narxi 20.000")

# 9
# import random
# menyu={
#     'otam':'osh',
#     'onam':'manti',
#     'opam':'kabob',
#     'akam':'shashlik',
#     'men':'somsa'
# }

# meals=[]
# for v in menyu.values():
#     meals.append(v)

# tanlangan=random.sample(meals,3)
# for n in tanlangan:
#     print(n)

# 10

# menyu = {
#     "osh": 28000,
#     "manti": 15000,
#     "shashlik": 12000,
#     "somsa": 8000,
#     "norin": 25000,
#     "lag'mon": 22000,
#     "qovurilgan tuxum": 7000,
#     "sho'rva": 18000
# }
# while True:
#     buyurtma=[]
#     i=0
#     while i<3:
#         meal=input(f"{i+1}-chi taom nomini kiriting=>")
#         if not meal.isalpha():
#             print("Taom nomini kiriting!!!")
#             continue
#         buyurtma.append(meal)
#         i+=1
#     for b in buyurtma:
#         if b in menyu:
#             print(b,menyu[b])
#         else:
#             print(f"Kechirasiz bizda {b} yo'q")
#     ask=input("Yana buyurtma qilasizmi?(y/n)")
#     if ask=='n':
#         break

# 11

# a=float(input("1-chi sonni kiriting=>"))
# b=float(input("2-chi sonni kiriting=>"))
# if a>b:
#     print(f"{a}>{b} Katta son=>{a}")
# elif a<b:
#     print(f"{a}<{b} Katta son=>{b}")
# else:
#     print(f"{a}={b} Ikkita son teng!!!")

# 12

# from datetime import date
# def information(name,surname,birth,location,email=None,phone_number=None):
#     info={
#         'name':name.strip().title(),
#         'surname':surname.strip().title(),
#         'birth':birth,
#         'age':date.today().year-birth,
#         'location':location.strip().title(),
#         'email':email.strip() if email else None,
#         'number':phone_number.strip() if phone_number else None
#     }
#     return info

# mijozlar=[]

# while True:
#     name=input("Ismingizni kiriting:")
#     s_name=input("Familiyangizni kiriting:")
#     birth=int(input("Tug'ilgan yilingizni kiriting:"))
#     location=input("Manzilingizni kiriting:")
#     email=input("Emailingizni kiriting:") 
#     phone_number=input("Nomeringizni kiriting:") or None
#     mijozlar.append(information(name,s_name,birth,location,email,phone_number))

#     question=input("Yana ma'lumot kiritasizmi?(y/n)")
#     if question=='n':
#         break

# print(mijozlar)

# 13

# def maxx_son(a,b,c):
#     result=''
#     if b<a>c:
#         result=a
#     elif a<b>c:
#         result=b
#     elif a<c>b:
#         result=c
#     elif a==b and a>c:
#         result=a  
#     elif a==c and a>b:
#         result=c
#     elif c==b and c>a:
#         result=b
#     elif a==b==c:
#         result=a
    
#     return result

# while True:
#     a=float(input("a sonni kiriting:")) 
#     b=float(input("b sonni kiriting:"))
#     c=float(input("c sonni kiriting:"))  
#     print(maxx_son(a,b,c))

#     ask=input("Yana tekshirib ko'rasizmi?(y/n)")
#     if ask=='n':
#         break

# 14

# def ball(names):
#     baholar={}
#     i=len(names)
#     count=0
#     while count<i:
#         baho=float(input(f"{names[count].strip().title()} ni bahosini kiriting:")) 
#         baholar[names[count].title()]=baho
#         count+=1
#     return baholar

# names=['javohir','elmurod','ahror','bahodir','elbek','akbar']
# print(ball(names))

# 15
# from datetime import date
# def hisobla(age):
#     return date.today().year-age

# name=input("Ismingizni kiriting:")
# age=int(input("Yoshingizni kiriting:"))
# print(f"{name.title()} siz {hisobla(age)}-yilsiz!!!")