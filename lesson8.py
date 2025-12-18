# name='ali'
# new={}
# i=len(name)
# step=0
# while i>0:
#     new[name[step]]=name
#     step+=1
#     i-=1
# print(new)

# import random
# belgi=['+','-','*','//']
# togri=0
# xato=0
# urinish=0
# while True:
#     son1=random.randint(1,100)
#     son2=random.randint(1,100)
#     amal=random.choice(belgi)

#     if amal=='+':
#         javob=son1+son2
#     elif amal=='-':
#         javob=son1-son2
#     elif amal=='//':
#         javob=son1//son2
#     elif amal=='*':
#         javob=son1*son2
    
#     print(f"{son1}{amal}{son2}=?")
#     user_answer=input("Natijani kiriting:")
#     if user_answer=='stop':
#         break
#     if int(user_answer)==javob:
#         print(f"{son1}{amal}{son2}={javob} Javobingiz to'g'ri")
#         togri+=1
#     else:
#         print("Javobingiz noto'g'ri")
#         xato+=1

#     urinish+=1

#     if urinish==6:
#         break
# print(f"To'g'ri javoblar soni=>{togri}\nXato javoblar soni=>{xato}")

# def salom_ber(name):
#     print("Assalomu alaykum",name)

# salom_ber('ali')
# salom_ber('vali')
# salom_ber('jobir')

# Homework

# 1

# def juft_toq(son):
#     if son%2==0:
#         print(f"{son}-soni juft son")
#     else:
#         print(f"{son}-soni toq son")

# ask=int(input("Sonni kiriting:"))
# juft_toq(ask)

# 2

# def salom_ber(name):
#     print(f"Assalomu alaykum {name}")

# name=input("Ismingizni kiriting:")
# salom_ber(name.capitalize())

# 3

# def add(a,b):
#     result=a+b
#     print(f"{a}+{b}={result}")

# a=float(input("1-chi sonni kiriting:"))
# b=float(input("2-chi sonni kiriting:"))
# add(a,b)

# 4

# def kvadrat(son):
#     print(f"{son}-sonning kvadrati -->{son**2}")

# number=float(input("Sonni kiriting:"))
# kvadrat(number)

# 5

# def yoshni_aniqla(age):
#     if age>18:
#         print("Yoshingiz 18 dan katta")
#     else:
#         print("Yoshingiz 18 dan kichik")

# age=int(input("Yoshingizni kiriting:"))
# yoshni_aniqla(age)

# 6

# def sonlarni_kopaytir(x,y,z):
#     print(f"{x}*{y}*{z}={x*y*z}")

# a=float(input("1-chi sonni kiriting:"))
# b=float(input("2-chi sonni kiriting:"))
# c=float(input("3-chi sonni kiriting:"))

# sonlarni_kopaytir(a,b,c)

# 7

# def teskari(matn):
#     teskari=''
#     for harf in matn:
#         teskari=harf+teskari
#     print(f"{matn}-ning teskarisi -->{teskari}")

# text=input("Matnni kiriting=>")
# teskari(text)


# def teskari(matn):
#     print(matn[::-1])
# text=input("Matnni kiriting=>")
# teskari(text)

# 8

# def eng_katta(a,b,c):
#     if b<a>c:
#         print(f"{a},{b},{c} sonlaridan kattasi {a}")
#     elif a<b>c:
#         print(f"{a},{b},{c} sonlaridan kattasi {b}")
#     elif a<c>b:
#         print(f"{a},{b},{c} sonlaridan kattasi {c}")
#     elif a==b==c:
#         print(f"{a},{b},{c} sonlarining hammasi teng")
#     elif a==b>c:
#         print(f"{a},{b},{c} sonlaridan kattasi {b}")
#     elif a==c>b:
#         print(f"{a},{b},{c} sonlaridan kattasi {c}")
#     elif a<b==c:
#         print(f"{a},{b},{c} sonlaridan kattasi {b}")
#     elif a==b<c:
#         print(f"{a},{b},{c} sonlaridan kattasi {c}")
#     elif a==c<b:
#         print(f"{a},{b},{c} sonlaridan kattasi {b}")
#     elif a>b==c:
#         print(f"{a},{b},{c} sonlaridan kattasi {a}")

# a=float(input("1-chi sonni kiriting:"))
# b=float(input("2-chi sonni kiriting:"))
# c=float(input("3-chi sonni kiriting:"))
# eng_katta(a,b,c)


# def eng_katta(a,b,c):
#     print(max(a,b,c))

# a=float(input("1-chi sonni kiriting:"))
# b=float(input("2-chi sonni kiriting:"))
# c=float(input("3-chi sonni kiriting:"))
# eng_katta(a,b,c)

# 9

# def kopaytir(numbers):
#     i=1
#     for number in numbers:
#         i*=number
#     print(i)


# numbers=[]
# while True:
#     ask=input("Sonni kiriting(stop):")
#     if ask=='stop':
#         break
#     if not ask.isdigit():
#         print("Faqat son kiriting!!!")
#         continue
#     else:
#         numbers.append(float(ask))
# print(numbers)  
# kopaytir(numbers)

# 10

# def birlashtir(matn1,matn2):
#     result=matn1+' '+matn2
#     print(result)

# matn1=input("1-chi matnni kiriting:")
# matn2=input("2-chi matnni kiriting:")
# birlashtir(matn1,matn2)