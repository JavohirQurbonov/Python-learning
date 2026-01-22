# Homework

# 1

# def bank_transactions(money:list[int])->bool:
#     balance=0
#     for m in money:
#         balance+=m
#     return balance<0
# print(bank_transactions([-200, 300, 200, -100]))

# 2

# arr=[2,1,5,1,3,2]
# k=3
# def max_productivity(product_quantity:list[int],day:int) -> int:
#         start_sum=sum(product_quantity[:day])
#         maxx_sum=start_sum
#
#         for i in range(day,len(product_quantity)):
#                 start_sum+=product_quantity[i]
#                 start_sum-=product_quantity[i-day]
#                 maxx_sum=max(maxx_sum,start_sum)
#
#         return maxx_sum
#
# print(max_productivity(arr,k))

# 3

# def is_spam(email_text:str)->bool:
#     spam_words=['free','win','money']
#     text=email_text.lower().split()
#     for word in spam_words:
#         if word in text:
#             return True
#     return False
#
# print(is_spam('asus tuf gaming '))

# 4

# def has_products(products_list: list[int]) -> bool:
#     return any(product<=0 for product in products_list)
# print(has_products([1,2,7,0,5]))

# 5

# order=[(1,4),(2,3),(3,5)]
#
# def receive_ordes(orders:list[tuple]):
#     orders.sort(key=lambda x:x[1])
#     orders_count=0
#     last_end=-1
#     for start,end in orders:
#         if start>=last_end:
#             orders_count+=1
#             last_end=end
#     return orders_count
#
# print(receive_ordes(order))

# 6

# import string
# def is_strong_password(password:str)->bool:
#     if len(password)>=8:
#         for symbol in password:
#             if (symbol in string.ascii_uppercase or symbol in string.digits) and symbol in string.ascii_letters:
#                 return True
#     return False
# print(is_strong_password("Java6998"))

# import string
# def is_strong_password(password:str)->bool:
#     if len(password) < 8:
#         return False
#
#     has_upper = False
#     has_digit = False
#
#     for symbol in password:
#         if symbol in string.ascii_uppercase:
#             has_upper = True
#         if symbol in string.digits:
#             has_digit = True
#
#     return has_upper and has_digit
#
# # print(is_strong_password("Java6998"))
#
#
