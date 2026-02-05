# class Grandparent:
#     def method1(self):
#         print("Bu bobomizning metodi")
#
# class Parent(Grandparent):
#     def method2(self):
#         print("Bu otamizning metodi")
#
# class Child(Parent):
#     def method3(self):
#         print("Bu farzandning metodi")
#
# obj = Child()
# obj.method1()  # Bu bobomizning metodi
# obj.method2()  # Bu otamizning metodi
# obj.method3()  # Bu farzandning metodi


# Ota sinf: Person
# class Person:
#     def __init__(self, name, id):
#         self.name = name
#         self.id = id
#
#     def display(self):
#         print(self.name, self.id)
#
# # Obyekt yaratish
# emp = Person("Satyam", 102)
# emp.display()
#
# class Employee(Person):
#

# class Person:
#     def __init__(self, name):
#         self.name = name
#
# class Employee(Person):  # Person sinfidan meros oladi
#     def __init__(self, name, salary):
#         super().__init__(name)
#         self.salary = salary
# class Job:
#     def __init__(self, salary):
#         self.salary = salary
#
# class Employee(Person, Job):  # Ikkita ota sinfdan meros oladi
#     def __init__(self, name, salary):
#         Person.__init__(self, name)
#         Job.__init__(self, salary)
#
# class Manager(Employee):  # Employee sinfidan meros oladi
#     def __init__(self, name, salary, department):
#         Employee.__init__(self, name, salary)
#         self.department = department
# class AssistantManager(Employee):
#     def __init__(self, name, salary, team_size):
#         Employee.__init__(self, name, salary)
#         self.team_size = team_size
#
# class SeniorManager(Manager, AssistantManager):  # Ikkita sinfdan meros oladi
#     def __init__(self, name, salary, department, team_size):
#         Manager.__init__(self, name, salary, department)
#         AssistantManager.__init__(self, name, salary, team_size)


# class Mato:
#     def made(self):
#         return None
#
# class Romol(Mato):
#     def __init__(self,color,types):
#         self.color = color
#         self.type = types
#
#     def made(self):
#         return f"Rangi:{self.color}\nMato turi:{self.type}"
#
# class Clothes(Mato):
#     def __init__(self,size):
#         self.size = size
#
#     def made(self):
#         return f"Ko'ylak o'lchami:{self.size}"
#
# products=[Romol("blue",'cotton'),Clothes(42)]
# for pro in products:
#     print(f"Info{pro.made()}")

# class Shape:
#     def perimetr(self):
#         return None
#
# class Rectangle(Shape):
#     def __init__(self,width,height):
#         self.width = width
#         self.height = height
#
#     def perimetr(self):
#         return 2*(self.width+self.height)
#
# class Uchburchak(Shape):
#     def __init__(self,a,b,c):
#         self.a=a
#         self.b=b
#         self.c=c
#
#     def perimetr(self):
#         return self.a+self.b+self.c
#
# shapes=[Rectangle(5,10),Uchburchak(6,8,10)]
# for sh in shapes:
#     print(f"Perimetr:{sh.perimetr()}")

class Library:
    def __init__(self,title,author,part,column,row):
        self.title=title
        self.author=author
        self.part=part
        self.column=column
        self.row=row

    def get_location(self):
        return f"{self.title} nomli assar bo'limi {self.part}ning {self.row} qatori {self.column}  ustunida turibdi"


class Book(Library):
    def __init__(self,title,author,part,column,row,page):
        super().__init__(title,author,part,column,row)
        self.page = page

class AudioBook(Library):
    def __init__(self,title,author,part,column,row,mp3):
        super().__init__(title,author,part,column,row)
        self.mp3 = mp3

class VideoBook(Library):
    def __init__(self,title,author,part,column,row,mp4):
        super().__init__(title,author,part,column,row)
        self.mp4 = mp4

class Magazine(Library):
    def __init__(self,title,author,part,column,row,number):
        super().__init__(title,author,part,column,row)
        self.number = number


class Category:
    def __init__(self,title):
        self.title=title
        self.books=list()