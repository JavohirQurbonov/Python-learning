# def aralash(name,age):
#     if name=='ali':
#         name+='jon'
#     return name
#
# data=aralash('ali',24)
# print(data)

# def get_product(*args,**kwargs):
#     return args,kwargs
#
# son=get_product(2,3,4,4,54,5,olma='qizil',nok='sariq',banan='hindi')
# # print(son)
# new=[]
# for i in son:
#     for j in i:
#         new.append(j)
# print(tuple(new))

# def counting_salary(name,part,**kwargs):
#     standard=30
#     jami=sum(list(kwargs.values()))
#     data=f"{name.title()} haftalik {jami*standard} $ "
#     soliq=jami*standard-jami*standard*0.1
#     paynet=jami*standard-jami*standard*0.01
#     return soliq+paynet
#
# data=counting_salary("nurulloh",'barber',monday=8,th=8,w=8,thr=8,fr=8,st=8)
# print(data)

# def funk(a,b=10,*args,c=20,**kwargs):
#     print(f"a:{a},b:{b},args:{args},c:{c},kwargs:{kwargs}")
#
# funk(1,2,3,4,c=30,d=40,e=50)

# Self-study

# 1

# number=float(input("Sonni kiriting=>"))
# calculate=lambda x:x*10
# print(calculate(number))

# 2

# a=float(input("a sonni kiriting=>"))
# b=float(input("b sonni kiriting=>"))
# hisobla=lambda  a,b:a+b
# print(hisobla(a,b))

# 3

# import random as r
# numbers=r.sample(range(0,1000),10)
# numbers=list(numbers)
# # funksiya=list(map(lambda x:x**2,numbers))
# # print(funksiya)
#
# funksiya=list(filter(lambda x:x%2!=0 ,numbers))
# print(numbers)
# print(funksiya)

# Homework

# 1

# def multiply_numbers(*args):
#     multiply=1
#     for number in list(args):
#         if len(args)>0:
#             multiply*=number
#         else:
#             multiply=1
#     return multiply
# print(multiply_numbers(10,12,15))

# 2

# def calculate_average(**kwargs):
#     average=sum(kwargs.values())/len(kwargs)
#     return average
# print(calculate_average(ali=85, vali=90, hasan=80))

# 3
#
# def count_types(*args):
#     dicts={}
#     for t in list(args):
#         if type(t) == int:
#             dicts['int']=t
#         elif type(t) == float:
#             dicts['float']=t
#         elif type(t) == str:
#             dicts['str']=t
#         elif type(t) == list:
#             dicts['list']=t
#         elif type(t) == tuple:
#             dicts['tuple']=t
#         elif type(t) == set:
#             dicts['set']=t
#     return dicts
#
# print(count_types(1,'hello',[1,2,3],{2,3}))


# 4

# def emloyee_data(name,age,**kwargs):
#     data={}
#     data['name'] = name.capitalize()
#     data['age'] = age
#     data.update(kwargs)
#     return data
# print(emloyee_data('javohir',24,maosh=800_000))

# 5

# def find_min_max(*args):
#     if len(args)>0:
#          minn=min(args)
#          maxx=max(args)
#          print(f"Min osn=>{minn}  va Max son=>{maxx}")
#     else:
#         print(None)
#
# find_min_max()

# 6

# def calculate_total(**kwargs):
#     products={ }
#     products.update(kwargs)
#     return f"Umumiy summa=>{sum(products.values())},Mahsulotlar=>p{products}"
#
# print(calculate_total(olma=10000,uzum=20000,non=15000))

# 7

