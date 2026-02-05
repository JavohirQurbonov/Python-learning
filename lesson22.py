# class Car:
#     def __init__(self, model, price, color):
#         self.model = model
#         self.price = price
#         self.color = color
#
#
#     def __repr__(self):
#         return self.color
#
#
#     def __str__(self):
#         return str(self.price)
#
#
# car = Car('gentra', 14000, 'qora')
# car2 = Car('tico', 4000, 'midnight')
# print(repr(car))
# print(car2)


# class Time:
#     DAY=86400
#     def __init__(self,sec):
#         self.sec = sec
#
#     # def get_time(self):
#     #     sec=self.sec
#     #     print(f"Sec:{sec}")
#     #     minn=self.sec // 60
#     #     min_sec=self.sec % 60
#     #     min_sum=f"{minn}-min {min_sec}-sec"
#     #     print(f"Min:{min_sum}")
#     #     hour=self.sec / 3600
#     #     print(f"Hour:{hour}")
#
#     def get_time(self):
#         s=self.sec%60
#         m=(self.sec//60)%60
#         h=(self.sec//3600)%24
#         return f"{self.get_formatted(h)}:{self.get_formatted(m)}:{self.get_formatted(s)}"
#
#     @classmethod
#     def get_formatted(cls,x):
#         return str(x).rjust(2,"0")
#
#     def __add__(self,other):
#         if isinstance(other,int):
#             return Time(self.sec+other)
#         if isinstance(other,Time):
#             return Time(self.sec+other.sec)
#
#     def __sub__(self,other):
#         if isinstance(other,int):
#             return Time(self.sec-other)
#         if isinstance(other,Time):
#             return Time(self.sec-other.sec)
#
# # obj=Time(160)
# # print(obj.get_time())
#
# obj=Time(40)
# obj2=Time(40)
# obj=obj-23
# print(obj.get_time())


# ----------------------------------Homework---------------------------------

class Player:
    """Player class"""
    def __init__(self, name:str, hp:float, power:float):
        self.name = name.title()
        self.hp = hp
        self.power = power

    def __repr__(self):
        return f"Name: {self.name}, HP: {self.hp}, Power: {self.power}"

    def __sub__(self, other):
        if not isinstance(other, Player):
            return NotImplemented
        self.hp -= other.power
        if self.hp < 0:
            self.hp = 0
        return self

    def __add__(self, value):
        if not isinstance(value, (int, float)):
            return NotImplemented
        self.hp += value
        return self

    def __mul__(self, value):
        if not isinstance(value, (int, float)):
            return NotImplemented
        self.power *= value
        return self

    def __lt__(self, other):
        if not isinstance(other, Player):
            return NotImplemented
        return (self.hp+self.power) < (other.hp+other.power)

    def __le__(self, other):
        if not isinstance(other, Player):
            return NotImplemented
        return (self.hp+self.power) <= (other.hp+other.power)

    def __eq__(self, other):
        if not isinstance(other, Player):
            return NotImplemented
        return (self.hp+self.power) == (other.hp+other.power)

    def __len__(self):
        return int(self.power+self.hp)

    def __abs__(self):
        return self.hp>0

# player1 = Player("Player 1", 100, 100)
# player1.hp+=40
# print(player1)

class Enemy:
    """Enemy class"""
    def __init__(self, name:str, hp:float, power:float):
        self.name = name.title()
        self.hp = hp
        self.power = power

    def __repr__(self):
        return f"Name: {self.name}, HP: {self.hp}, Power: {self.power}"

    def __sub__(self, other):
        self.hp -= other.power
        if self.hp < 0:
            self.hp = 0
        return self

    def __lt__(self, other):
        return (self.hp+self.power) < (other.hp+other.power)

    def __le__(self, other):
        return (self.hp+self.power) <= (other.hp+other.power)

    def __eq__(self, other):
        return (self.hp+self.power) == (other.hp+other.power)

    def __abs__(self):
        return self.hp>0


# Player va Enemy yaratamiz
knight = Player("Knight", 100, 20)
dragon = Enemy("Dragon", 150, 30)

print("=== Boshlang‘ich holat ===")
print(knight)
print(dragon)

# Urush
print("\n--- Urush boshlandi! ---")
knight - dragon
dragon - knight
print(knight)
print(dragon)

# HP qo‘shish
print("\n--- Knight davolandi! ---")
knight + 20
print(knight)

# Kuchaytirish
print("\n--- Knight kuchaytirildi! ---")
knight * 2
print(knight)

# Solishtirish
print("\n--- Solishtirish ---")
if knight > dragon:
    print("Knight kuchliroq!")
elif knight < dragon:
    print("Dragon kuchliroq!")
else:
    print("Ikkalasi teng kuchli!")

# Statistika
print("\n--- Knight statistikasi ---")
print("Umumiy stat:", len(knight))

# Tirik yoki o‘lik
print("\n--- O‘yin holati ---")
if abs(knight):
    print("Knight tirik")
else:
    print("Knight o‘lik")

if abs(dragon):
    print("Dragon tirik")
else:
    print("Dragon o‘lik")

print("\n=== O‘yin tugadi! ===")
