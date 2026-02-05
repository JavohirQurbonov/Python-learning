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
# new=Phone("iphone",'white','batary','yomkst uxlagan','display qirilgan',vil='shanxay',tum='beshariq',mah='archa kocha')
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

class UserProfile:
    """UserProfile class"""
    def __init__(self, name:str, email:str):
        self.name = name
        self.email = email
        self.__password = ''




