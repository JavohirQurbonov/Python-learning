# my_file=open('new_file.txt','w')
# my_file.write("Hello World")
# my_file.close()
from itertools import count
# from os import write

# with open('with_data.txt','w') as data:
#     data.write('Salom')
# print('Fayl yozildi')

# datas=['nima\n','kim\n','ali\n']
# with open('with_data.txt','a') as data:
#     data.writelines(datas)
# print('Fayl yozildi')

# with open('with_data.txt','r') as file:
#     for line in file:
#         print(line,end="")

# with open('with_data.txt','r') as file:
#     str1=file.readline()
#     print(str1,end="")
#     str2=file.readline()
#     print(str2)

# with open('with_data.txt', 'r') as f:
#     lines = f.readline()
#     while lines:
#         print(lines,end="")
#         lines = f.readline()


# def receive(name):
#     with open('peoples.txt','a') as file:
#         file.write(name+'\n')
#     with open('peoples.txt','r') as file:
#         for line in file:
#             print(line,end="")
#
#
# count=0
# while True:
#     person=input(f"{count+1}.Ismni kiriting:")
#     question=input("Yana odam qo'shasizmi?(y/n)")
#     count+=1
#     if question=="n":
#         break
#
# receive(person)

# FILE="person.txt"
#
# def create_visit_person(name):
#     with open(FILE,"a") as person:
#         person.write(f"{name}\n")
#         print(f"{name} qoshildi")
#
#
# def read_visits(x):
#     if x=='no':
#         with open(FILE,'r+') as read_person:
#             count=0
#             for person in read_person:
#                 count+=1
#                 print(person)
#             print(f"Jami mehmon soni {count}ta")
#
#
# def start_guest():
#     while True:
#
#         mehmon=input("mwhmonni ismini yozing(no):")
#         if mehmon=='no':
#             read_visits(mehmon)
#         elif mehmon!='no':
#             create_visit_person(mehmon)

# start_guest()

# def find(name):
#     result=''
#     with open(FILE,'r+') as people:
#         for person in people:
#             if str(person.strip())==name:
#                 result=f"{person} topildi"
#             else:
#                 result="Bu odam topilamdi"
#     return result
# print(find('sohib'))

# while True:
#     selection=int(input("1.Yozish\t2.O'qish\t3.Chiqish\tTalang:"))
#     match selection:
#         case 1:write()
#         case 2:read()
#         case 3:break
#         case_:print("Noto'g'ri tanlov")

# -------------------Homework--------------------

# 1

# def create_file(filename,text):
#     with open(filename,'w+') as file:
#         file.write(text)
#
#     with open(filename,'r') as read_file:
#         return read_file.read()
#
# print(create_file('test.txt','hello world'))


# 2

# def summ(numbers):
#     with open('summa.txt','w',encoding='utf-8') as file:
#         for n in numbers:
#             file.write(str(n)+'\n')
#
#     summa=0
#     with open('summa.txt','r',encoding='utf-8') as summ_file:
#        for line in summ_file:
#            print(line)
#            summa+=int(line)
#
#     return f"Sonlar yig'indisi=>{summa}"
#
# print(summ([1,2,3,4,5,6]))

# 3
#
# def search_word(words,seek_word):
#     with open('words.txt','w') as file:
#         for word in words:
#             file.write(word+'\n')
#
#     with open('words.txt','r') as file:
#         doc=file.readlines()
#         for line in doc:
#             if seek_word.strip()==line.strip():
#                 return True
#
#     return False
#
#
# print(search_word(['python','java','javas'],'python'))

# 4

# def line_count(text):
#     with open('lines.txt','w') as file:
#         file.write(text)
#
#     count=0
#     with open('lines.txt','r') as read_file:
#         for line in read_file:
#             count+=1
#
#     return count
#
# print(line_count('javohir\nqurbonov\nbahodir\nqurbonov\n'))


# 5

# def find_max(numbers):
#     with open('max_numbers.txt','w') as file:
#         for number in numbers:
#             file.write(str(number)+'\n')
#
#     maxx=0
#     with open('max_numbers.txt','r') as read_file:
#         # print(max(read_file.readlines()))
#         for line in read_file:
#             if int(line)>maxx:
#                 maxx=int(line)
#
#     return maxx
# print(find_max([1,2,3,4,5,23,45]))

# 6

# def find_words(text):
#     with open('new_words.txt','w') as file:
#         file.write(text)
#
#     count=0
#     with open('new_words.txt','r') as read_file:
#         # read_file.read()
#         for word in read_file:
#             count+=len(word.split())
#
#     return count
#
# print(find_words('hello world java '))
