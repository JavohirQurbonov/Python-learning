# cars=['onix','gentra','nexia2','tico']
# for i in range(len(cars)):
#     if cars[i]=='tico':
#         print(cars[i].upper())
#     else:
#         print(cars[i])

# students=['durbek','javohir','javohir','azamat','eshdavlat','odiljon','samandar','nurilloh',[22,24,19,21,16,20,24,21]]
# students[-1].append(30)
# print(students)

# ages=[22,24,19,21,16,20,24,21]
# ages.sort()
# print(f"Studentlar soni:{len(ages)}\nEng yosh katta=>{max(ages)}\nEng kichik yosh=>{min(ages)}\nO'rtacha yosh=>{int(sum(ages)/len(ages))}\nTartiblash=>{ages}")

# yoshlar=[]
# keksalar=[]
# for a in ages:
#     if a>=20:
#         keksalar.append(a)
#     else:
#         yoshlar.append(a)

# print(f"Yoshlar=>{yoshlar} va soni=>{len(yoshlar)}\nKattalar=>{keksalar} va sonni {len(keksalar)}")

# students=['durbek','javohir','javohir','azamat','eshdavlat','odiljon','samandar','nurilloh',]
# a_li=[]
# a_siz=[]
# standart='a'
# for ism in students:
#     if standart in ism.lower():
#         a_li.append(ism)
#     else:
#         a_siz.append(ism)

# print(a_li)
# print(a_siz)
# if(len(a_li)>len(a_siz)):
#     print(a_li)
# elif (len(a_li)==len(a_siz)):
#     print(f"{a_li}\n{a_siz}")
# else:
#     print(a_siz)
# new_number=[]
# for s in students:
#     new_number.append(len(s))
# print(new_number)


# Homework

# 1

# query=int(input("Sonni kiriting=>"))
# if (query==0):
#     print("Nol soni juft ham emas,toq ham emas")
# elif (query%2==0):
#     print(f"{query}-soni juft son")
# else:
#     print(f"{query}-soni toq son")

# 2

# query=float(input("Haroratni kiriting=>"))
# if query<0:
#     print("Havo sovuq")
# elif query>=0 and query<=20:
#     print("Havo salqin!")
# elif query>20:
#     print("Havo issiq")

# 3

# a=float(input("Xonaning 1-chi tomonini kiriting=>"))
# b=float(input("Xonaning 2-chi tomonini kiriting=>"))
# result=a*b
# print(f"Xonaning tomonlari=>{a,b} va xonaning maydoni=>{result}kv.m")

# 4

# query=input("Ismni kiriting=>")
# x=len(query)
# if x<5:
#     print("Ismingiz juda qisqa!")
# elif x>=5 and x<8:
#     print("Ismingiz o'rtacha uzunlikda!")
# elif x>=8:
#     print("Ismingiz juda uzun!")

# 5

# query=int(input("Ballni kiriting=>"))
# if query>=90:
#     print(f"Balingiz=>{query} va ko'rsatgichingiz=>'A'")
# elif query>=80 and query<=89:
#     print(f"Balingiz=>{query} va ko'rsatgichingiz=>'B'")
# elif query>=70 and query<=79:
#     print(f"Balingiz=>{query} va ko'rsatgichingiz=>'C'")
# elif query>=60 and query<=69:
#     print(f"Balingiz=>{query} va ko'rsatgichingiz=>'D'")
# elif query<60:
#     print(f"Balingiz=>{query} va ko'rsatgichingiz=>'F'")


# 6

# query=int(input("Oy raqamini kiriting(1:12)=>"))
# if query==12 or query==1 or query==2:
#     print("Qish fasli")
# elif query==3 or query==4 or query==5:
#     print("Bahor fasli")
# elif query==6 or query==7 or query==8:
#     print("Yoz fasli")
# elif query==9 or query==10 or query==11:
#     print("Kuz fasli")





