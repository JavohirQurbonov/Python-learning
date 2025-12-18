# phone_dict={
#     "brand":"apple",
#     "price":1200,
#     "chp":['ekran qirilgan','yumks yegan',"rangi tanimas daraja"],
#     'change':('batraya','ekran','kamera qum')
# }
# print(phone_dict['chp'][1][8:])

# shajara={
#     'bobo':{
#         'name':'ali',
#         'age':80,
#         'adres':'chorsu',
#         'farzan':['vali','sobir',{
#             'rus':'chp'
#         }]
#     }
# }


# print(shajara['bobo']['farzan'][-1]['rus'])

# keys=["a","b","c"]
# new_dict=dict.fromkeys(keys,3)
# print(new_dict)

# my_dict={"a":1,"b":2}
# value=my_dict.setdefault("a",3)
# print(my_dict)

# students = {
#     "student1": {
#         "name": "Ali",
#         "age": 20,
#         "subjects": ["Mathematics", "Physics", "Chemistry"]
#     },
#     "student2": {
#         "name": "Laylo",
#         "age": 22,
#         "subjects": ["Biology", "History", "Geography"]
#     },
#     "student3": {
#         "name": "Bekzod",
#         "age": 19,
#         "subjects": ["Computer Science", "Mathematics"]
#     }
# }

# students={
#     "ahror":5,
#     "sohib":4,
#     "begzod":3,
#     "elbek":5
# }
# students["bexrux"]=5,
# students["javohir"]=4,
# students["siddiq"]=3

# students["begzod"]=5

# del students['siddiq']

# print(students)

# name=input("Ismingizni kiriting:")
# age=int(input("Yoshingizni kiriting:"))
# if name:
#     fam=input(f"{name} familiyangizni kiriting:")
#     print(f"{name} {fam} {2025-age} yilsiz")
# else:
#     print("nega yozmading")

# age=int(input("Yoshingiz"))
# if age<13:
#     print("Sizga 14000")
# elif age<18:
#     print("Sizga 18000")
# else:
#     print("Sizga 22 ming")



# Homework

# 1

# query=float(input("Son kiriting=>"))
# if query>0:
#     print(f"{query} <---> Musbat son")
# elif query==0:
#     print(f"{query} <---> raqami musbat ham emas,manfiy ham emas")
# else:
#     print(f"{query} <---> Manfiy son")

# 2

# query=float(input("Ballni kiriting [0-100]=>"))
# if query>0 and query<=100:
#     if query>=90:
#         print(f"{query} ---> A")
#     elif 80<query<90:
#         print(f"{query} ---> B")
#     elif 70<query<80:
#         print(f"{query} ---> C")
#     elif 60<query<70:
#         print(f"{query} ---> D")
#     else:
#         print(f"{query} ---> F")
# else:
#     print("0-100 oralig'ida ball kiriting!!!")

# 3

# query=int(input("Nechta son kiritmoqchisiz=>"))
# numbers=[]
# for i in range(query):
#     ask=float(input(f"{i+1}-chi sonni kiriting=>"))
#     numbers.append(ask)
# print(max(numbers))


# 3.2

# a=float(input("3 ta sonning 1-chisini kiriting=>"))
# b=float(input("3 ta sonning 2-chisini kiriting=>"))
# c=float(input("3 ta sonning 3-chisini kiriting=>"))
# if a>b and a>c:
#     print(f"Max son=>{a}")
# elif b>a and b>c:
#     print(f"Max son=>{b}")
# elif c>a and c>b:
#     print(f"Max son=>{c}")
# elif a==b and b==c:
#     print("Hamma sonlar teng")
# elif a==b and a>c:
#     print(f"Max son {a}")
# elif a==c and a>b:
#     print(f"Max son {a}")
# elif b==c and b>a:
#     print(f"Max son {b}")

# 4

# year=int(input("Yilni kiriting=>"))
# if year%4==0 and year%100!=0 or year%400==0:
#     print(f"{year} <=> Kabisa yili")
# else:
#     print(f"{year} <=> Kabisa yili emas")

# 5

# password=int(input("Parolni kiriting:"))
# if password==12345:
#     print("Xush kelibsiz!!!")
# else:
#     print("Parol noto'g'ri")

# 6

# number=int(input("Sonni kiriting=>"))
# if number%3==0 and number%5==0:
#     print(f"{number}-soni 3 ga va 5 ga bo'linadi")
# elif number%3==0 and number%5!=0:
#     print(f"{number}-soni 3 bo'linadi")
# elif number%3!=0 and number%5==0:
#     print(f"{number}-soni 5 bo'linadi")
# else:
#     print(f"{number}-soni 3 ga ham,5 ga ham bo'linmaydi")


# # 2



