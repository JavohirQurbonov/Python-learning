# def my_function(a,b,/,*,c,d):
#     print(a+b+c+d)
#
# my_function(5,6,c=7,d=8)

# def calculate(a):
#     S=a*a
#     P=4*a
#     return f"Yuzasi =>{S},Perimetri=>{P}"
# print(calculate(5))

# def sana(satr):
#     return satr.lower().count('a')
# print(sana('Assalomu alaykum'))

# def hisobla(mahsulot_narxi,chegirma):
#     if chegirma>20:
#         print("Chegirma foizi xato")
#     else:
#         print(f"Chegirmadagi narxi=>{mahsulot_narxi-(mahsulot_narxi*chegirma)/100}")
#
# hisobla(250000,18)

# def oylik(**kwargs):
#     new_data={}
#     for key, value in kwargs.items():
#         new_data[key]=value*8*22
#     return new_data
#
# print(oylik(Ali=15000,Vali=20000,olim=18000))

# def new_price(data):
#     new_prices=[]
#     for d in data:
#         d=d+200
#         new_prices.append(d)
#     return new_prices
# print(new_price([3000,2000,4500]))


# sonlar=[1,2,3,4,5]
# kvadrat=list(map(lambda x:x**3,sonlar))
# print(kvadrat)


# sonlar=[1,2,3,4,5,6]
# answer=list(filter(lambda x:x%2==0,sonlar))
# print(answer)
#
# answer=list(map(lambda x:x**2,answer))
# print(answer)

# from functools import reduce
# sonlar=[1,2,3,4,5]
# bolinma=reduce(lambda x,y: x/y,sonlar)
# print(bolinma)


# mevalar = ["olma", "banan", "uzum"]
# narxlar = [5000, 7000, 10000]
# boglangan=dict(zip(mevalar, narxlar))
# print(boglangan)






