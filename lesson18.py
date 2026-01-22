# def tashqi_funksiya(x):
#     def ichki_funksiya(y):
#         return x + y
#     return ichki_funksiya
#
# add_five=tashqi_funksiya(5)
# print(add_five(10))
from functools import wraps


# def matnni_qayta_ishlash(matn):
#     def tozalash():
#         return matn.strip().lower()
#
#     def uzunligi():
#         return len(matn)
#
#     def find_a():
#         data=tozalash()
#         return data.count('a')
#
#     return tozalash(), uzunligi(), find_a()
#
#
# print(matnni_qayta_ishlash(" Salom Dunyo! java"))

# def hisoblagic():
#     son=0
#
#     def qoshish():
#         nonlocal son
#         son+=1
#         if son==5:
#             son=0
#         return son
#
#     return qoshish
#
# hisob=hisoblagic()
# print(hisob())
# print(hisob())
# print(hisob())
# print(hisob())
# print(hisob())
# print(hisob())

# def salom_ber():
#     print("salom,dunyo")
#
# x=salom_ber
# x()

# def log(f):
#     print("Funksiya ishga tushmoqda")
#     f()
#     print("Funksiya tugadi!")
#
# def salom():
#     print("Salom,Temur")
#
# log(salom)

# def log_decorator(func):
#     def wrapper():
#         print("Ish boshlanmoqda")
#         func()
#         print("Ish tugadi")
#     return wrapper

# def kvadrat_decorator(func):
#     def wrapper(*args, **kwargs):
#         natija=func(*args, **kwargs)
#         return natija**2
#     return wrapper
#
# @kvadrat_decorator
# def raqam_ber():
#     return 5
#
# print(raqam_ber())


# def repeat(times):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             for _ in range(times):
#                 func(*args, **kwargs)
#         return wrapper
#     return decorator
#
# @repeat(5)
# def hello():
#     print("Salom")
# hello()
# #
# def my_decorator(func):
#     def wrapper(*args, **kwargs):
#         print("Oldin")
#         result = func(*args, **kwargs)
#         print("Keyin")
#         return result
#     return wrapper

#
# def my_decorator(func):
#     def wrapper(*args, **kwargs):
#         print("Hisoblanmoqda...")
#         return func(*args, **kwargs)
#     return wrapper
#
# @my_decorator
# def add(a, b):
#     return a + b
#
# print(add(3, 5))

#------------------Homework------------------

# 1

# def my_decorator(func):
#     count=0
#     def counter(*args):
#         nonlocal count
#         count+=1
#         func()
#         print(f"Funksiya {count}-marta chaqirildi")
#     return counter
# @my_decorator
# def my_func():
#      print("ASUS TUF GAMING")
# my_func()
# my_func()
# my_func()
# my_func()
# my_func()

# 2

# import time
# from functools import wraps
#
# def my_decorator(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result=func(*args, **kwargs)
#         end_time = time.time()
#         duration = end_time - start_time
#         print(f"{duration:.6f} soniya ketdi")
#         return result
#     return wrapper
# @my_decorator
# def my_func():
#      print("ASUS TUF GAMING")
# my_func()

# 3

# def my_decorator(func):
#     @wraps(func)
#     def wrapper(*args,**kwargs):
#         for symbol in args:
#             if symbol<=0:
#                 print("Xatolik:manfiy  son")
#
#         for symbol in kwargs.values():
#             if symbol<=0:
#                 print("Xatolik:manfiy  son")
#
#         return func(*args,**kwargs)
#     return wrapper
# @my_decorator
# def my_math(a,b):
#     return a+b
# my_math(5,-3)

# 4

# def check_admin(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         if args[0]=='admin':
#             print(f"Xush kelibsiz {str(args[0]).upper()}")
#         else:
#             print("Ruxsat yo'q")
#         return func(*args, **kwargs)
#     return wrapper
#
# @check_admin
# def receive(login):
#     return login
#
# receive('admin')

# 5

# def check_cache(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#
#
#
# @check_cache
# def add(a, b):
#     return a + b

# 6

# from functools import wraps
# def my_decorator(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         print(func.__name__)
#         print(args)
#         result = func(*args, **kwargs)
#         print(result)
#     return wrapper
#
# @my_decorator
# def add(x, y):
#     return x + y
# add(1, 2)

# 7
# from functools import wraps
#
# def limit_calls(limit):
#     def decorator(func):
#         count=0
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             nonlocal count
#             if  count<limit:
#                 count += 1
#                 return func(*args, **kwargs)
#             return "Limitdan oshib ketdi"
#         return wrapper
#     return decorator
#
# @limit_calls(3)
# def say_hello():
#     return "Hello Coder"
# print(say_hello())
# print(say_hello())
# print(say_hello())
# print(say_hello())
# print(say_hello())
# print(say_hello())


# # 8
# from functools import wraps
#
# def defender(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         try:
#             return func(*args, **kwargs)
#         except ZeroDivisionError:
#             print("Nolga bo‘lish mumkin emas")
#     return wrapper
#
#
# @defender
# def hisobla():
#     while True:
#         a=float(input("1-chi sonni kiriting:"))
#         b=float(input("2-chi sonni kiriting:"))
#         amal=input("Amalni kiriting:")
#         if amal=='*':
#             print(a*b)
#         elif amal=='+':
#             print(a+b)
#         elif amal=='-':
#             print(a-b)
#         elif amal=="/":
#             print(a/b)
#         ask=input("Yana hisoblaysizmi?(y/n)")
#         if ask=="n":
#             break
# hisobla()


