# class Parent:
#     def __init__(self,name,age):
#         self.name= name
#         self.__age=age
#
#     def get_age(self):
#         return self.__age
#
# class Child(Parent):
#     def display(self):
#         print(f"Ism:{self.name}")
#         #print(f"Yosh:{self.__age}")
#         print(f"Yosh:{self.get_age()}")
#
#
# child=Child("Ali",25)
# child.display()

# class User:
#     def __init__(self,name,password):
#         self.name=name
#         self.__password=password
#
#     def __encrypt_password(self):
#         return self.__password[::-1]
#
#     def get_encrypted_password(self):
#         return self.__encrypt_password()
#
# user=User("Ali","mysecret")
# # print(user.__encrypted_password())
#
# print(user.get_encrypted_password())

# class Product:
#     __slots__=('title','price')
#     def __init__(self,title,price):
#         self.title=title
#         self.price=price
#
# new=Product("olma",15000)
# # new.color='qizil'
# print(new.color)
#
# class Fruit(Product):
#     def __init__(self):
#         super().__