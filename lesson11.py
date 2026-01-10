# Exam

# 1

# login=input("Loginingizni kiriting:")
# password=int(input("Parolingizni kiriting:"))
# if login=='admin' and password==1234:
#     print("Xush kelibsiz!!!")
# else:
#     print("Login yoki parol noto'g'ri!")

# 2

# ball=float(input("Balingizni kiriting:"))
# if ball>=90 and ball<=100:
#     print(f"Sizning balingiz {ball} va bahoingiz 'A'")
# elif ball>=75 and ball<=89:
#     print(f"Sizning balingiz {ball} va bahoingiz 'B'")
# elif ball>=60 and ball<=74:
#     print(f"Sizning balingiz {ball} va bahoingiz 'C'")
# else:
#     print(f"Sizning balingiz {ball} va bahoingiz 'F'")  

# 3

# charge=int(input("Telefoningizni zaryad foizini kiriting(0-100):"))
# result=''
# if charge<20:
#     result=True
# else:
#     result=False

# if result==True:
#     print("Telefoningizni zaryadga ulang!!!")
# else:
#     print("Shart emas zaryadga ulash!!!")

# 4


# ask=int(input("Nechta mahsulot narxini kiritmoqchisiz?"))
# prices=[]
# i=0
# while i<ask:
#     price=int(input(f"{i+1}-chi mahsulot narxini kiriting:"))
#     prices.append(price)
#     i+=1
# print(f"Siz kiritgan mahsulot narxlari=>{prices}\nUmumiy summa=>{sum(prices)}\nEng qimmat mahsulot=>{max(prices)}")

# 5

# cities = ("Toshkent", "Samarqand", "Buxoro", "Xorazm","Navoiy","Andijon","namangan",'farg\'ona',"surxondaryo","qashqadaryo","jizzax","sirdaryo")
# asks=int(input("Shahar raqamini kiriting[1-12]:"))
# ask=asks-1
# result=''
# if ask==0:
#     result=cities[ask]
# elif ask==1:
#     result=cities[ask]
# elif ask==2:
#     result=cities[ask]
# elif ask==3:
#     result=cities[ask]
# elif ask==4:
#     result=cities[ask]
# elif ask==5:
#     result=cities[ask]
# elif ask==6:
#     result=cities[ask]
# elif ask==7:
#     result=cities[ask]
# elif ask==8:
#     result=cities[ask]
# elif ask==9:
#     result=cities[ask]
# elif ask==10:
#     result=cities[ask]
# elif ask==11:
#     result=cities[ask]
# else:
#     result="Oraliqdagi qiymatni kiriting!!!"

# print(result.title())


# 6

# ask=int(input("Nechta ism kiritmoqchisiz?"))
# names=set()
# i=0
# while i<ask:
#     name=input(f"{i+1}-chi ismni kiriting=>")
#     names.add(name.capitalize())
#     i+=1
# print(names)

# 7

# products={
#     'non':4000,
#     'cola':15000,
#     'sut':10000,
#     'un':8000,
#     'sok':14950,
#     'patir':5000
# }
# while True:
#     ask=input("Mahsulot nomini kiriting=>")
#     if ask.isalpha():
#         if ask.casefold() in products:
#             print(f"{ask.capitalize()}ni narxi =>{products[ask.casefold()]}")
#         else:
#             print(f"Kechirasiz bizda {ask.title()} yo'q !!!")
#     else:
#         print("Faqat so'z bilan yozing!!!")
    
#     question=input("Yana mahsulot narxini so'raysizmi?(y/n)")
#     if question=='n':
#         break


# 8


# secret=7
# while True:
#     number=int(input("O'ylagan soningizni kiriting=>"))
#     if number==secret:
#         print("Tabriklayman siz topdingiz!!!")
#         break
#     else:
#         print("Boshqa son kiriting!!!")

# 9


# def hisobla(son):
#     kvadrat=son**2
#     kubi=son**3
#     print(f"Siz kiritgan son=>{number} va bu sonning kvadrati=>{kvadrat},kubi=>{kubi} ga teng")

# number=int(input("Sonni kiriting:"))
# hisobla(number)

# 10

# mahsulotlar={
#     'non':4000,
#     'cola':15000,
#     'sut':10000,
#     'un':8000,
#     'sok':14950,
#     'patir':5000,
#     'pamidor':15000,
#     'bodring':18000
# }
# products={}
# while True:
#     product_name=input("Mahsulot nomini kiriting:")
#     quantity_product=int(input(f"{product_name.title()} miqdorini kiriting=>"))
#     products[product_name]=quantity_product
#     print(f"Siz kiritgan mahsulotlar=>{products}")
#     question=input("Yana mahsulot qo'shasizmi?(y/n)")
#     if question=='n':
#         break
    
# # print(products)

# mavjud_mahsulot={}
# yoq_mahsulotlar={}
# summa=0
# for product,quantity in products.items():
#     if product.casefold() in mahsulotlar:
#         mavjud_mahsulot[product]=(quantity*mahsulotlar[product])
#         summa+=(quantity*mahsulotlar[product])
#     elif product.casefold() not in mahsulotlar:
#         yoq_mahsulotlar[product]=quantity
#         print(f"Kechirasiz bizda {yoq_mahsulotlar} bu mahsulotlar yo'q")

# if summa>=100_000:
#     print(f"Sizga 10% chegirma bilan bo'lgan umumiy summa=>{summa*0.9}")
#     print(f"Siz olgan mahsulotlar va ularning miqdori=>{products}")
#     print(f"Siz sotib olgan mahsulotlar va ularning olgan miqdoringiz bilan bo'lgan narxlari=>{mavjud_mahsulot}\nUmumiy summa=>{summa} bo'ldi va chegirma bilan {summa*0.9} to'laysiz")
   
# else:
#     print(f"Siz olgan mahsulotlar va ularning miqdori=>{products}")
#     print(f"Siz sotib olgan mahsulotlar va ularning olgan miqdoringiz bilan bo'lgan narxlari=>{mavjud_mahsulot}\nUmumiy summa=>{summa} bo'ldi")
    
# if len(yoq_mahsulotlar)>0:
#     print(f"Kechirasiz bizda {list(yoq_mahsulotlar.keys())} bu mahsulotlar yo'q")

# 11

# def ballar(*ball):
#     baho=list(ball)
#     otgan_ball=[]
#     for b in baho:
#         if b>=60:
#             otgan_ball.append(b)
#     return otgan_ball
# print(ballar(45, 78, 90, 55, 60))

# 12

# def ish_kunlari(*qiymat):
#     grafik=list(qiymat)
#     borgan=0
#     bormagan=0
#     for k in qiymat:
#         if k==True:
#             borgan+=1
#         else:
#             bormagan+=1
#     return f"Borgan kunlar soni=>{borgan}\nBormagan kunlar soni=>{bormagan}"

# print(ish_kunlari(True, False, True, True, False, True))
