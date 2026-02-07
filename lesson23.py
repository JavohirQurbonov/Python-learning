# class Person:
#     def __init__(self,name,age):
#         print('init')
#         self.name=name
#         self.age=age
#     def __setattr__(self, name, value):
#             print('__setattr__',name,value)
#             # if value=='ali':
#             #     print(f"{value} ismli userga ruxsat yoq")
#             # else:
#             #     value=None
#             return super().__setattr__(name,value)
#
#     def __getattr__(self, name):
#         return
#
# obj=Person('ali',22)
# print(obj.__dict__)
# from itertools import count


# class Phone:
#     def __init__(self, model, color, *args):
#         self.model = model
#         self.color = color
#         self.parts = list(args)
#
#     def __getitem__(self, item):
#         print(item)
#         return self.parts[item]
#
#     frg
#
# new=Phone("iphone",'white','battery','yomkist uxlagan','display qirilgan')
# print(new[1][-3:])


# class Phone:
#     def __init__(self,model,color,*args,**kwargs):
#         self.model=model
#         self.color=color
#         self.parts=list(args)
#         self.adres=kwargs
#
#     def __getitem__(self, item):
#         if type(item)==int:
#             return self.parts[item]
#         else:
#             return self.adres[item]
#
#     def __setitem__(self, key, value):
#         if type(key)==int:
#             self.parts[key] = value
#         else:
#             self.adres[key] = value
#
#     def __repr__(self):
#         return self.adres
#
# new=Phone("iPhone",'white','batary','yomkst uxlagan','display qirilgan',vil='shanxay',tum='beshariq',mahalla='archa kocha')
# # data=new[1]
# # print(type(data))
# # print(new[1:5])
# # print(new.__dict__)
# print(new['mah'])
# new[2]='chotki'
# print(new.adres)
# print(new.parts)

# class Counter:
#     def __init__(self):
#         self.count = 0
#
#     def __call__(self):
#         self.count += 1
#         print(f"Chaqirilgan {self.count} marta")
#
# c=Counter()
# c()
# c()
# c()


#------------------------------Homework---------------------------------
# Class

# 1

# class SmartCounter:
#     """SmartCounter class"""
#     count=0
#     def __init__(self, number:float):
#         if not isinstance(number,(float,int)):
#             raise TypeError("Kiritilgan qiymat son bo'lishi kerak")
#         self.number = number
#         SmartCounter.count+=1
#
#     @classmethod
#     def total_objects(cls):
#         return SmartCounter.count
#
#     @staticmethod
#     def is_positive(n):
#         if not isinstance(n,(int,float)):
#             raise TypeError("Kiritilgan qiymat son bo'lishi kerak")
#         if n>0:
#             return True
#         else:
#             return False
#
#     def __str__(self):
#         return f"Number:{self.number}\nCount:{SmartCounter.total_objects()}"
#
#     def __repr__(self):
#         return f"Umumiy obyektlar:{SmartCounter.total_objects()}\nKiritilga son:{self.number}"
#
#
# c1=SmartCounter(10)
# c2=SmartCounter(7)
# print(SmartCounter.total_objects())
# print(SmartCounter.is_positive(-8))

# 2

# class Money:
#     """Money class"""
#     Money_currency={'USD','UZS','RUB'}
#     def __init__(self, amount:float, currency:str):
#         self._verify_amount(amount)
#         self._verify_currency(currency)
#
#         self.amount=amount
#         self.currency=currency.upper()
#
#     @staticmethod
#     def _verify_amount(amount):
#         if not isinstance(amount,(int,float)):
#             raise TypeError("Faqat son qiymat kiritish kerak")
#         if amount<0:
#             raise ValueError("Manfiy qiymat kiritish mumkin emas")
#
#     @staticmethod
#     def _verify_currency(currency):
#         if not isinstance(currency,str):
#             raise TypeError("So'z bilan kiriting birlikni")
#         if currency.upper() not in Money.Money_currency:
#             raise ValueError("Kiritilgan pul birligi mavjud emas")
#         if not currency.strip():
#             raise ValueError("Pul birligi kiritilgan bo'lishi kerak")
#
#     def __eq__(self, other):
#         if not isinstance(other,Money):
#             return NotImplemented
#         return self.currency==other.currency
#
#
#     def __add__(self, other):
#         if not isinstance(other,Money):
#             return NotImplemented
#         if self.currency!=other.currency:
#             raise ValueError("Pul birligi bir xil bo'lishi kerak")
#         else:
#             return self.amount+other.amount
#
#     def __sub__(self, other):
#         if not isinstance(other, Money):
#             return NotImplemented
#         if self.currency != other.currency:
#             raise ValueError("Pul birligi bir xil bo'lishi kerak")
#         else:
#             return abs(self.amount - other.amount)
#
#     def __mul__(self, other):
#         if not isinstance(other, Money):
#             return NotImplemented
#         if self.currency != other.currency:
#             raise ValueError("Pul birligi bir xil bo'lishi kerak")
#         else:
#             return self.amount * other.amount
#
#
# obj=Money(100,'usd')
# obj2=Money(200,'usd')
# print(obj-obj2)
#
#

# 3
#
# class UserProfile:
#     """UserProfile class"""
#     def __init__(self, name:str, email:str):
#         self.name = name
#         self.email = email
#         self.__password = ''
#
#     def __getattr__(self, item):
#         return f"'{item}' bunday atribut mavjud emas"
#
#     def __getattribute__(self, item):
#         print(f"Log:{item}")
#         if item=='password':
#             raise AttributeError("'password' atributiga tashqaridan kirish mumkin emas")
#         return object.__getattribute__(self,item)
#
# u = UserProfile("Ali", "ali@gmail.com")
#
# print(u.name)
# print(u.age)
# try:
#     print(u.password)
# except AttributeError as e:
#     print(e)
# print(u._UserProfile__password)

# 4

# class CustomList:
#     """CustomList class"""
#     def __init__(self,data:list):
#         self.__data = data
#
#     def __getitem__(self, item):
#         try:
#             return self.__data[item]
#         except IndexError:
#             raise IndexError("Custom error")
#     def __setitem__(self, key, value):
#         try:
#             self.__data[key]=value
#         except IndexError:
#             raise IndexError('Indeksda xatolik')
#     def __len__(self):
#         return len(self.__data)
#
# cl = CustomList([10, 20, 30])
#
# print(cl[1])
# cl[1] = 99
# print(cl[1])
# print(len(cl))

# 5
#
# class InventoryItem:
#     total_items = 0
#     total_quantity = 0
#
#     def __init__(self, name: str, price: float, quantity: int):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#
#         InventoryItem.total_items += 1
#         InventoryItem.total_quantity += quantity
#
#     @staticmethod
#     def is_valid_price(price):
#         return isinstance(price, (int, float)) and price >= 0
#
#     @classmethod
#     def get_statistics(cls):
#         return {
#             "total_items": cls.total_items,
#             "total_quantity": cls.total_quantity
#         }
#
#     def __setattr__(self, key, value):
#         if key == "price" and not InventoryItem.is_valid_price(value):
#             raise ValueError("Price manfiy bo‘lishi mumkin emas")
#         object.__setattr__(self, key, value)
#
#     def __getattr__(self, item):
#         return f"{item} mavjud emas!"
#
#     def __getitem__(self, key):
#         if key in ("price", "quantity"):
#             return getattr(self, key)
#         raise KeyError("Bunday key yo‘q")
#
#     def __setitem__(self, key, value):
#         if key == "quantity":
#             self.quantity = value
#         elif key == "price":
#             self.price = value
#         else:
#             raise KeyError("Bunday key yo‘q")
#
#     def __add__(self, other):
#         if self.name != other.name:
#             raise ValueError("Faqat bir xil nomdagi itemlar qo‘shiladi")
#         return InventoryItem(
#             self.name,
#             self.price,
#             self.quantity + other.quantity
#         )
#
#     def __eq__(self, other):
#         return self.name == other.name and self.price == other.price
#
#     def __str__(self):
#         return f"Name:{self.name} | Price: {self.price} | Quantity: {self.quantity}"
#
#     def __repr__(self):
#         return f"InventoryItem(name='{self.name}', price={self.price}, quantity={self.quantity})"
#
# i1 = InventoryItem("Laptop", 1000, 5)
# i2 = InventoryItem("Laptop", 1000, 3)
#
# print(i1 + i2)
# print(i1["price"])
# i1["quantity"] = 10
#
#

# ---------------------------Extra---------------------------

# 1

# def count_numbers(numbers:list):
#     number={}
#     for n in numbers:
#         number[n]=numbers.count(n)
#     key,value=max(number.items(),key=lambda x:x[1])
#     return key,value
#
# print(count_numbers([1, 2, 2, 3, 3,4,4]))

# # 2
#
# def is_balanced(text:str):
#     stack=[]
#     symbols={
#         '(':')',
#         '[':']',
#         '{':'}'
#     }
#
#     for part in text:
#         if part in symbols:
#             stack.append(part)
#         elif part in symbols.values():
#             if not stack:
#                 return False
#             if symbols[stack.pop()]!=part:
#                 return False
#
#     return not stack
#
# print(is_balanced("{}"))

# 3
# To'liqmas


# def minn_diff(numbers:list):
#     pass
#
#
# print(minn_diff([5, 1, 9, 3]))

# 4
# To'liqmas

# def group_words(words:list):
#     same_letter_word=[]
#     for word in words:
#         # letter=[]
#         print(word)
#         for w in words:
#             if len(word)==len(w):
#                 same_letter_word.append(w)
#
#     return same_letter_word
#
#
#
#
# print(group_words(["eat", "tea", "tan", "ate", "nat"]))


# 5

#
# def longest_seqeunce(numbers:list):
#     x=''
#     for list_1 in numbers:
#         i=0
#         size=len(list_1)
#         test_list=[]
#         while i<size-1:
#             if list_1[i]<list_1[i+1]:
#                 test_list.append(list_1[i])
#             if list_1[-1]==list_1[i+1]:
#                 test_list.append(list_1[-1])
#             i+=1
#         # print(test_list)
#         if len(test_list)==size:
#             x=test_list.copy()
#
#     return x
# print(longest_seqeunce([[1,4,5],[3,5,7,9,12],[5,6,8,9,10,16,18]]))


# Extra
# def longest_sequence(numbers: list):
#     longest = []
#
#     for seq in numbers:
#         is_increasing = True
#         for i in range(len(seq) - 1):
#             if seq[i] >= seq[i + 1]:
#                 is_increasing = False
#                 break
#
#         if is_increasing and len(seq) > len(longest):
#             longest = seq
#
#     return longest
#
#
# print(longest_sequence([[1,4,5],[3,5,7,9,12],[5,6,8,9,10,16,18]]))


# 6

# def single_number(numbers:list):
#     single_numbers=[]
#     for num in numbers:
#         if numbers.count(num)==1:
#             single_numbers.append(num)
#
#     return single_numbers
#
# print(single_number([4, 1, 2, 1, 2]))

# 7

# def split_bill(payments:dict):
#     key,value = max(payments.items(),key=lambda x:x[1])
#     keys=[]
#     values=[]
#     for k,v in payments.items():
#         keys.append(k)
#         values.append(v)
#     one_person = sum(values) / len(payments)
#     lists={}
#     extra_pay={}
#     for i,j in payments.items():
#         if j>one_person:
#             lists[i]=j
#             extra_pay[i]=(j-one_person)
#
#     return f"Ko'p to'lov qilganlar:{lists}\nOrtiqcha to'langan summalar:{extra_pay}\nBitta odamga tushgan summa:{one_person}"
#
# print(split_bill(
# {
#     "Ali": 120,
#     "Vali": 80,
#     "Soli": 100,
#     "Java":110,
#     "Elbek":105
# }
# ))



# 8

# def max_num_from_text(text:str):
#     try:
#         number=[]
#         for part in  text.split():
#             if part.isdigit():
#                 number.append(int(part))
#
#         return max(number)
#     except ValueError:
#         return f"Matnda son qatnashmagan yoki ajratib yozilmagan!"
#
# print(max_num_from_text("Ali  12 ta olma va  105 ta banan oldi"))


# 9

# def rotate(numbers:list,k):
#     # n=len(numbers)
#     # k%=n
#     i=0
#     while i<k:
#         pop_n=numbers.pop()
#         numbers.insert(0,pop_n)
#         i+=1
#
#     return numbers
#
#
# print(rotate([1, 2, 3], 100))





# 10

# musbat
# juft
# 3 ga bo'linadigan

# def find_numbers(numbers:list):
#     correct_answer=[]
#     for num in numbers:
#         if num>0 and num%2==0 and num%3==0:
#             correct_answer.append(num)
#
#     return correct_answer,sum(correct_answer)
#
# print(find_numbers([3, 6, -2, 9, 4, 12]))