# ------------------------STR-----------------------
# from itertools import count
from multiprocessing.util import close_all_fds_except

# 1
# print(len("hello world"))

# def calculate_len(word):
#     i=0
#     for w in word:
#        i+=1
#     return i
# print(calculate_len("hello world"))

# 2

# s="Python"
# print(s[0],s[-1])

# 3

# s="Hello world from Python"
# print(s.count(' '))

# 4

# s="Django Rest"
# print(s.upper())

# 5

# s="HeLLo"
# print(s.lower())
# print(s.casefold())

# 6

# s="a1b2c3"
# i=0
# r=0
# while i<len(s):
#     if s[i].isdigit():
#         r+=1
#     i+=1
# print(r)

# 7

# def palindrom(word:str):
#     if word==word[::-1]:
#         result='Palindrom'
#     else:
#         result='Palindrom emas'
#
#     return result
# print(palindrom('levela'))

# 8

# s="I love Python very much"
# l=s.split()
# print(len(l))

# 9

# s="I love programming in python javohirqurbonov"
# words=s.split()
# max_l=max((len(w))for w in words)
# for x in words:
#     if len(x)==max_l:
#         print(x)

# 10

# s='banana'
# ch='a'

# print(s.count('a'))

# i=0
# for w in s:
#    if w==ch:
#        i+=1
# print(i)

# 11

# s='banana'
# print(s.replace('a','@'))

# 12

# s='a1b2c3'
# new_w=''
# for w in s:
#     if not w.isdigit():
#         new_w+=w
# print(new_w)

# 13

# s="phone:99890"
# new=''
# for w in s:
#     if w.isdigit():
#         new+=w
# print(new)

# 14

# s='aaabbccccd'
# new_w=''
# for w in s:
#     if w not in new_w:
#         new_w+=w
# print(new_w)

# 15

# s='I love Python'
# m=s.split()
# new_w=''
# i=1
# while i<=len(m):
#     new_w+=m[-i]+' '
#     i+=1
# print(new_w)

# 16

# s='hello world python'
# print(s.title())

# 17

# s1='evil'
# s2='vile'
#
# def anagram(word1,word2):
#     if len(word1)==len(word2):
#         letter_list=list(w for w in word1)
#         i = 0
#         for letter in letter_list:
#             if letter in word2:
#                 i+=1
#         if len(word1)==i:
#             print("Anagram")
#         else:
#             print("Anagram emas")
#     else:
#         print("Uzunligi bir xil emas!Anagram emas")
#
# anagram(s1,s2)

# 18

# word = 'success'
# count_s = {}
#
# for l in word:
#     count_s[l] = word.count(l)
#
# key, value = max(count_s.items(), key=lambda x: x[1])
# print(key, value)

# 19

# s='Contact me:test@gmail.com'
# if '@gmail.com' in s:
#     print(True)
# else:
#     print(False)

# 20
# userNameEmail

# s='user_name_email'
# word_list=s.split('_')
# new_w=''
# for w in word_list:
#     new_w+=w.title()
# print(new_w)

# 21

# word='aabbcde'
# new_w=''
# for w in word:
#     if word.count(w)==1:
#         new_w+=w
# print(new_w)

# 22
# 23
# 24

# 25

# s='I love python backend programming java php'
# new_w=''
# word_list=s.split()
# word_list.sort(key=lambda x:len(x))
# for word in word_list:
#     new_w+=word+' '
# print(new_w)

# 26

# word='a10b20cc5'
# numbers=[]
# number=''
#
# for w in word:
#     if w.isdigit():
#         number+=w
#     else:
#         if number:
#             numbers.append(int(number))
#             number=''
# if number:
#     numbers.append(int(number))
# print(numbers)
# print(sum(numbers))

# 27

# s='User123'
# number=any(n.isdigit() for n in s)
# letter=any(l.isalpha() for l in s)
# print(number and letter)

# 28

# To'liqmas

# formm="(a+b)*(c+d)"
# symbol={
#     '(':')'
# }
# sym=[]
# opens = False
# closes = False
# for p in formm:
#     if p in symbol.keys():
#         sym.append(p)
#         opens=True
#     if p in symbol.values():
#         if symbol[sym[0]]==p:
#             sym.append(p)
#             closes=True
#     print(opens and closes)

# 29

# s='abc'
# new_s=''
# new_list=[]
# letter=list(x for x in s)
# for l in letter:
#     new_s+=l
#     if new_s not in new_list:
#         new_list.append(new_s)
# print(new_list)

# 30

# word='leetcode'
# word_l=[]
# for w in word:
#     if w not in word_l:
#         word_l.append(w)
#
# for l in word_l:
#     if word.count(l)==1 and ):






