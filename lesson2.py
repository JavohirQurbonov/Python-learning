# fruits=['olma','behi','uzum','shaftoli']
# print(fruits[1:3:2])
# fruits.append('banan')
# fruits.insert(3,'limon')
# new_f=['o\'rik','tarvuz']
# fruits.extend(new_f)
# print(fruits)






# user=input("Ismingizni kiriting:")
# address=input("Manzilingizni kiriting:")
# age=int(input("Yoshingizni kiriting:"))
# data=[]
# data.append(user.capitalize())
# data.append(address.capitalize())
# data.append(age)
# print(data)

# odatlarim=['uxlash','pubg','chekish','noschi','kitob uqish','insta']
# new_hobbies=['python']
# new_u=odatlarim.pop(0)
# new_u2=odatlarim.pop(1)
# new_u3=odatlarim.pop(-2)
# new_hobbies.append(new_u)
# new_hobbies.append(new_u2)
# new_hobbies.append(new_u3)
# print(new_hobbies)
# print(odatlarim)

# son=int(input("nechta mahsulot kerak"))
# mahsulotlar=[]
# for i in range(son):
#     product=input(f"{i+1}-mahsulot nomi:")
#     mahsulotlar.append(product)
# print(mahsulotlar)



# Homework

# 1

# numbers=[1,2,3]
# numbers.append(4)
# print(numbers)

# 2

# numbers=[5,10,15,20]
# numbers.remove(15)
# print(numbers)

# 3

# numbers=[8,9,10]
# numbers[1]=99
# print(numbers)

# 4

# numbers=[1,2,3,4]
# numbers.clear()
# print(numbers)

# 5

# question=int(input("Nechta son qo'shmoqchisiz=>"))
# numbers=[3,6,9]
# for i in range(question):
#     ask=int(input(f"{i+1}-sonni kiriting=>"))
#     numbers.append(ask)
# print(numbers)

# 6

# numbers=[7,14,21,28,35]
# del numbers[3]
# print(numbers)

# 7

# numbers=[2,4,6]
# numbers.insert(1,3)
# print(numbers)

# 8

# numbers=[1,2,3,4,5]
# numbers[2:4]=7,8
# print(numbers)

# 9

# numbers=[11,22,33]
# new_list=[]
# for i in range(len(numbers)):
#     new_list.append(numbers[i])
# print(new_list)

# 10

# numbers=[4,5,6]
# del numbers[-1]
# print(numbers)

# numbers=[4,5,6]
# numbers.pop(-1)
# print(numbers)

# 11

# numbers=[1,2,3,4,5]
# print(len(numbers))

# 12

# list_1=[2,4,6]
# list_2=[8,10,12]
# list_1.extend(list_2)
# print(list_1)

# 13

# ask=int(input("Sonni kiriting=>"))
# numbers=[5,10,15]
# if ask in numbers:
#     print(True)
# else:
#     print(False)

# 14

# numbers=[7,7,7,3,3]
# print(numbers.count(7))

# 15

# numbers=[10,20,30]
# new_numbers=numbers.copy()
# print(new_numbers)

# numbers=[10,20,30]
# new_list=[]
# for i in range(len(numbers)):
#     new_list.append(numbers[i])
# print(new_list)



# text='jjbbjh bbhjbbjh'
# print(text.splitlines())

matn = "Hello Python World acsasc"
print(matn.swapcase())
