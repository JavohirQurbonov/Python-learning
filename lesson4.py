# # # 1

# # students=("Ali","Zebo","Javohir","Ali","Zebo","Ali")
# # print(students.count("Zebo"))

# # # 2

# # score=(85,90,78,92,88)
# # score=list(score)
# # score.sort()
# # score=tuple(score)
# # print(score)

# # 1.elementni qoshish
# # (.add)->metodi
# # 2.elementni ochirish
# # (.remove)element mavjud bolsa ochiradi,bolmasa xato qaytaradi
# # .discard->element mavjud bolmasa xato qaytaradi

# # 3.tozalash
# # .clear->set ni tozalaydi

# # fruits={"apple","banana"}
# # fruits.clear()
# # print(fruits)

# # a={1,2,3}
# # b={4,5,6}
# # print(a.union(b))

# # a={1,2,3}
# # b={2,3,4}
# # print(a.intersection(b))

# # a={1,2,3}
# # b={2,3,4}
# # print(a.difference(b))

# # a={1,2,3}
# # b={2,3,4}
# # print(a.symmetric_difference(b))

# # math_students={"ali","zebo","said"}
# # english_students={"said","Javohir","ali"}
# # print(math_students.intersection(english_students))

# # all_players={"ali","zebo","said","javohir"}
# # violators={"said","javohir"}
# # print(all_players.symmetric_difference(violators))


# # Homework

# # 1

# nums=[1,2,3,2,4,1,5]
# nums=set(nums)
# nums=list(nums)
# print(nums)

# # 2

# a=[1,2,3,4]
# b=[3,4,5,6]
# a=set(a)
# b=set(b)
# print(a.intersection(b))

# # 3

# a = [1, 2, 3, 4]
# b = [3, 4, 5, 6]
# a=set(a)
# b=set(b)
# print(a.difference(b))

# # 4

# data=[1,2,2,3,4,4,5]
# data=set(data)
# print(len(data))

# # 5

# query=int(input("Nechta so'z kiritasiz=>"))
# words=[]
# for i in range(query):
#     ask=input(f"{i+1}-chi so'zni kiriting=>")
#     words.append(ask)
# words=set(words)
# print(len(words))

# # 6

# query=input("Matnni kiriting=>")
# words=set(query.replace(" ",""))
# print(words)
