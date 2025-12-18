# Homework

# 1

# def max_price(price):
#     return max(price)

# print(max_price([12_000,45_000,23_000]))

# 2

# def min_price(price):
#     return min(price)

# print(min_price([12_000,45_000,23_000]))

# 3

# def ortacha_baho(ball):
#     return sum(ball)/len(ball)

# print(ortacha_baho([5,4,3,5]))

# 4

# linear 

# balls=[5,4,5,3,5]
# m=max(balls)
# i=0
# count=0
# while i<len(balls):
#     if m==balls[i]:
#         count+=1
#     i+=1
# print(count)

# function

# def count_max_ball(balls):
#     m=max(balls)
#     i=0
#     count=0
#     while i<len(balls):
#         if m==balls[i]:
#             count+=1
#         i+=1
#     return count

# print(f"Eng yuqori ball soni=>{count_max_ball([5,4,5,3,5])} ta")

# 5

# def discounted_price(price,sale):
#     return price*(100-sale)/100

# price=int(input("Mahsulot narxini kiriting:"))
# sale=int(input("Chegirma foizini kiriting:"))
# print(f"Mahsulotning asl narxi=>{price}\nHozirgi chegirmada {discounted_price(price,sale)}")