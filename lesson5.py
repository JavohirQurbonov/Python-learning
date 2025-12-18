# phone={
#     'brand':'apple',
#     'model':'iphone16',
#     'price':1300,
#     'health':90,
#     'xitoy':False,
#     'brand':'samsung'
# }


# print(phone)

car={
    'brand':'chevrolet',
    'model':'lacetti',
    'price':4500
}
# new=list(car.keys())
# old=list(car.values())
# items=list(car.items())
# print(new)
# print(old)
# print(items)
# print(car['brand'])

# del car['brand']
# del car

# new=car.pop('price')
# boshqa=car.popitem()
# print(car)
# print(new)
# print(boshqa)
# print(car.get('models','qiymat yoq'))
# print(car['price'])
# car['color']='black'
# car['model']='gm'
# car.update({'model':'onix'})
# data=car['price']
# print(car)
# print(data)

# son=int(input("Nechta mahsulot kiritasiz=>"))
# products=[]
# for i in range(son):
#     product=input("Mahsulot nomini kiriting=>")
#     if product in products:
#         print(f"{product} borku aytingiz!")
#     else:
#         products.append(product)

# karzinka={
#     "non":4200,
#     "cola":11300,
#     "choy":11000,
#     "banan":22000,
#     "gosht":130000
# }
# qiymat=0
# for mahsulot in products:
#     if mahsulot in karzinka:
#         answer=f"{mahsulot}-narxi =>{karzinka[mahsulot]}"
#         qiymat+=karzinka[mahsulot]
#     else:
#         answer=f"Biza {mahsulot} qolmabdi!"
# print(qiymat)



# Homework

# # 1

# 2

# product=('olma',5000,3)
# total_price=product[1]*product[2]
# print(f"Olgan mahsulotingizni umumiy narxi=>{total_price}")

# 3

# employee=("Dilshod",5_000_000,500_000)
# salary=employee[1]+employee[2]
# print(f"Ishchining umumiy maoshi=>{salary}")


# # 2 List (Ro'yxatlar) bo'yicha masalalar:

# 1

# query=int(input("Nechta son kiritasiz=>"))
# numbers=[]
# for i in range(query):
#     ask=float(input(f"{i+1}-chi sonni kiriting:"))
#     numbers.append(ask)
# print(f"Kiritilgan sonlar=>{numbers}\nEng katta son=>{max(numbers)}\nEng kichik son=>{min(numbers)}")

# 2

# query=int(input("Nechta son kiritasiz=>"))
# numbers=[]
# for i in range(query):
#     ask=float(input(f"{i+1}-chi sonni kiriting:"))
#     numbers.append(ask)

# multi_numbers=[]
# for n in numbers:
#     multi_numbers.append(n*2)
# print(f"Kiritilgan sonlar=>{numbers}\n2 ga ko'paytirilgan shakli=>{multi_numbers}")

# 3

# query=int(input("Nechta son kiritasiz=>"))
# numbers=[]
# for i in range(query):
#     ask=float(input(f"{i+1}-chi sonni kiriting:"))
#     numbers.append(ask)

# numbers=set(numbers)
# new_list=list(numbers)
# print(new_list)

# 4

# query=int(input("Nechta so'z kiritasiz=>"))
# words=[]
# for i in range(query):
#     ask=input(f"{i+1}-chi so'zni kiriting:")
#     words.append(ask.casefold())
# print(f"Kiritilgan so'zlar=>{words}\nTartiblangan ko'rinish=>{sorted(words)}")

# 5

# query=int(input("Nechta son kiritasiz=>"))
# numbers=[]
# for i in range(query):
#     ask=float(input(f"{i+1}-chi sonni kiriting:"))
#     numbers.append(ask)

# juft_sonlar=[]
# for n in numbers:
#     if n%2==0:
#         juft_sonlar.append(n)
# print(juft_sonlar)

# 6

# numbers=[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
# max_numbers=[]
# for i in numbers:
#     max_numbers.append(max(i))
# print(max_numbers)


# # 3 Dictionary (Lug‘atlar) bo‘yicha masalalar:

# 1

# name=input("Ismingizni kiriting=>")
# age=int(input("Yoshingizni kiriting=>"))
# data={}
# data[name.capitalize()]=age
# print(data)

# 2

# pupils={
#     "Sanjar":[3,5,4,4,3],
#     "Bahodir":[5,5,4,5,4],
#     "Elbek":[5,4,4,5,4],
#     "Ahror":[4,3,4,5,4]
# }
# for k,v in pupils.items():
#     print(f"O'quvchining ismi=>{k} <=======> O'rtacha bahosi=>{sum(v)/len(v)}")

# 3

# data={
#     'name':'Javohir',
#     'lname':'Qurbonov',
#     'age':24,
#     'year':2001,
#     'location':'Navai'
# }
# print(data)
# for i in data.keys():
#     if 'age'==i:
#         data['age']+=1
# print(data)

# 4

# data={
#     'javohir':24,
#     'elbek':22,
#     'sohib':26,
#     'bobur':20
# }
# print(sorted(data.keys()))

# 5

# employees={
#     'javohir':1000,
#     'elbek':400,
#     'sohib':300,
#     'bobur':500,
#     'ahror':600
# }
# new=[]
# for k,v in employees.items():
#     if v>=500:
#         new.append(k.capitalize())

# print(new)

# 6

# data={
#     'name':'javohir',
#     'lname':'qurbonov',
#     'age':24,
#     'salary':500,
#     'year':2001
# }

# for k,v in data.items():
#     if isinstance(v,(int,float)):
#         data[k]+=data[k]
# print(data)


# # 4

# 1

# xonalar = {
#     101: "band",  
#     102: "bo'sh",  
#     103: "band",  
#     104: "bo'sh",  
#     105: "band"
# }

# rooms=[]
# for k,v in xonalar.items():
#     if v=='bo\'sh':
#         rooms.append(k)
# if len(rooms)==0:
#     print("Kechirasiz bizda bo'sh xonalar yo'q")
# else:
#     print(f"Assalomu alaykum!\nBizda {rooms} xonalar bo'sh!!!")

# 2

# dokon = {
#     "olma": 12_000,
#     "banan": 18_000,
#     "shaftoli": 22_000,
#     "uzum": 15_000
# }

# query=int(input("Mahsulot qo'shish (1),o'zgartirish (2),o'chirish (3) (Ko'rsatilgan raqamlardan birini tanglang)=>"))
# if query==1 or query==2:
#     name=input("Mahsulot nomini kiriting=>")
#     price=int(input("Mahsulot narxini kiriting=>"))
#     dokon[name]=price
#     print(dokon)
# elif query==3:
#     name=input("Mahsulot nomini kiriting=>")
#     if name in dokon.keys():
#         del dokon[name]
#         print(dokon)
#     else:
#         print(f"Kechirasiz do'konda {name} qolmagan!!!")
#         print(f"Do'konda mavjud mahsulotlar=>{list(dokon.keys())}")


# 3

# ballar = {
#     "Ali": 85,
#     "Bobur": 90,
#     "Sarvar": 78,
#     "Zarina": 92
# }

# query=int(input("Ishtirokchiga ball qo'shish (1),eng yuqori ball (2),Ishtirokchini chiqarish (3) (Ko'rsatilgan raqamlardan birini tanglang)=>"))
# if query==1:
#     name=input("Ishtirokchi ismini kiriting=>")
#     ball=int(input("Qo'shimcha ballni kiriting=>"))
#     ballar[name.capitalize()]+=ball
#     print(ballar)
# elif query==2:
#     max_key=max(ballar,key=ballar.get)
#     max_value=ballar[max_key]
#     print(max_key,max_value)
# elif query==3:
#     name=input("Ishtirokchini ismini kiriting=>")
#     if name.capitalize() in ballar.keys():
#         del ballar[name.capitalize()]
#         print(ballar)
#     else:
#         print(f"Kechirasiz {name}-ismli ishtirokchi yo'q!!!")
#         print(f"Guruhda bor ishtirokchilar=>{list(ballar.keys())}")

# 4

# kutubxona = {
#     "Python Dasturlash",
#     "Sun’iy Intellekt Asoslari",
#     "Ma’lumotlar Bazasini Boshqarish",
#     "Algoritmlar va Ma’lumotlar Tuzilmalari"
# }
# book=input("Kitob nomini kiriting=>")
# for k in list(kutubxona):
#     if book==k.casefold():
#         answer=(set(kutubxona))
#     else:
#         answer=kutubxona.add(book.title())
# print(kutubxona)

# 5

# joylar=[1,2,3,4,5,6,7,8,9,10]
# band_joylar=[]

# count=len(joylar)
# while count>0:
#     # print(f"Bo'sh joylar=>{joylar}")
#     print(f"Band joylar=>{band_joylar}")
#     query=int(input(f"Joy raqamini kiriting {joylar}=>"))
#     band_joylar.append(joylar.pop(query-1))
#     ask=input("Yana joy band qilasizmi?(ha/yoq)")
#     if ask.casefold()=='yoq':
#        break
#     count-=1
# if len(joylar)==0:
#     print("Bo'sh joq qolmadi")

phone_dict={
    "brand":"apple",
    "price":1200,
    "chp":['ekran qirilgan','yumks yegan',"rangi tanimas daraja"],
    'change':('batraya','ekran','kamera qum')
}
print(phone_dict['chp'][1][8:])