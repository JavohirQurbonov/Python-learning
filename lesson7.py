# darslar=["english","tarix","matematika"]
# for x in darslar:
#     print(x)

# fruits=["apple","banana","cherry"]
# for x in fruits:
#     print(x)
#     if x=="banana":
#         break

# fruits=["apple","banana","cherry"]
# for x in fruits:
#     print(x)
#     if x=="banana":
#         continue

# adj=["red","big","tasty"]
# fruits=["apple","banana","cherry"]

# for x in adj:
#     for y in fruits:
#         print(x,y)

# i=1
# while i<6:
#     print(i)
#     i+=1

# i=1
# while i<6:
#     print(i)
#     if i==3:
#         break
#     i+=1

# import random

# son = random.randint(1, 100) # 41
# while True:
#     user_answer=int(input("1,100 taxmin qiling:(0):")) # 77
#     if user_answer==0:
#         break
#     if son>user_answer:
#         x=son-user_answer
#         print(f"{x} qo'shing")
#     elif son<user_answer:
#         y=user_answer-son
#         print(f"{y} ayiring")
#     else:
#         print(f"Topdingiz {son}        sizni javobiz {user_answer}")
#         break


# import random

# tomonlar=['left','center','right']
# human=0
# computer=0
# while computer<6 or human<6:
#     varatar=random.choice(tomonlar) # left
#     user_answer=input(f"Varataga teping {tomonlar}(stop):") # right
#     if user_answer=='stop':
#         break
#     if not user_answer in tomonlar:
#         print(f"Faqat {tomonlar}larga teping ")
#         continue
#     print(f"Varata {varatar} tomonga sakramoqda")
#     print(f"Siz zarbangaiz {user_answer} tomonga tepdingiz")
#     if user_answer==varatar:
#         print("Negoal")
#         computer+=1
#     else:
#         print("Gaoal")
#         human+=1
#     if computer==5:
#         print("Kompyuter yutdi!")
#         break
#     elif human==5:
#         print("Siz yutdingiz!")
#         break


# Homework

# 1

# i=1
# while i<=10:
#     if i%2==0:
#         print(i)
#     i+=1

# 2

# number=int(input("Sonni kiriting:"))
# if number>0:
#     i=1
#     j=0
#     numbers=[]
#     while i<=number:
#         numbers.append(i)
#         j+=i
#         i+=1
#     print(f"Sonlar=>{numbers} va ularning yig'indisi=>{j}")
# else:
#     print("Musbat son kiriting!!!")
    

# 3


# i=0
# numbers=[]
# while True:
#     number=int(input("Sonni kiriting:"))
#     if number==0:
#         break
#     numbers.append(number)
#     i+=1

# print(numbers)
# print(f"Kiritilgan sonlar soni=>{i}")


# 4

# number=int(input("Sonni kiriting:"))
# if number>0:
#     teskari_son=0
#     while number>0:
#         raqam=number%10
#         teskari_son=teskari_son*10+raqam
#         number//=10
#     print(teskari_son)
# else:
#     print("Musbat son kiriting!!!")

# 5


# attempt=0
# while attempt<3:
#     password=int(input("Parolni kiriting:"))
#     if password==12345:
#         print("Tizimga xush kelibsiz!!!")
#         break
#     else:
#         print("Parol noto'g'ri")
#     attempt+=1
#     if attempt==3:
#         print("Urinishlar tugadi!!!")

# 6

# i=0
# while i<=20:
#     if i%3==0:
#         print(i)
#     i+=1


