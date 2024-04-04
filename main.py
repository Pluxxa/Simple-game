from abc import ABC, abstractmethod
import random


class Fighter():
    def __init__(self, name, st, hp, weapon):
        self.name = name
        self.st = st
        self.hp = hp
        self.weapon = weapon


    def change_weapon(self, new_weapon):
        self.weapon = new_weapon
        print(f"Вы сменили оружие на {new_weapon.name}")

    def heal(self):
        self.hp+=20
        print("Вы вылечились на 20 жизней")


class Monster():
    def __init__(self, name, st, hp, weapon):
        self.name = name
        self.st = st
        self.hp = hp
        self.weapon = weapon


class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

class Sword(Weapon):
    def __init__(self, name="меч", damage=f"{random.randint(1,8)}"):
        self.name = name
        self.damage = damage
    def attack(self):
        return f"Вы ударили и нанесли {random.randint(1,8)} урона"


class Bow(Weapon):
    def __init__(self, name="лук", damage=f"{random.randint(1,6)}"):
        self.name = name
        self.damage = damage
    def attack(self):
        return f"Вы выстрелили и нанесли {random.randint(1,6)} урона"


name = input("Введите имя персонажа: ")
w = input("Введите название оружия которым хотите пользоваться(лук или меч): ")
stren = random.randint(10, 25)
hp = random.randint(50, 100)
while True:
    if w.lower() == "лук":
        weap = Bow()
        break
    elif w.lower() == "меч":
        weap = Sword()
        break
    else:
        w = input("Выберете оружие из предлоенного списка: меч или лук")
name_list = ["жорик", "костехрухт", "мозгоед"]
name_weap = ["лук", "меч"]
w1 = Fighter(name, stren, hp, weap)
w = random.choice(name_weap)
if w.lower() == "лук":
    weap = Bow()
elif w.lower() == "меч":
    weap = Sword()
m1 = Monster(random.choice(name_list), stren, random.randint(10, 30), weap)

a = input("Вы зашли в подъземелье, перед Вами проход вперёд. Вы можете пойти прямо или повернуть назад. Куда вы направитесь?\n1 - прямо\n2 - уйти из подземелья\n")
if a == '1':
    print(f"Вы решили проти дальше. Как только вы отошли от входа поальше на Вас напал {m1.name}.")
elif a == "2":
    print("Вы как трус убежали из подъземелья и больше никогда сюда не возвращались!")
    exit()
while m1.hp > 0:
    b = input(f"что вы делаете?\n1 - атаковать {m1.name}а\n2 - сменить оружие на меч\n3 - сменить оружие на лук\n4 - убежать в панике\n")
    if b == '1':
        c = w1.weapon.attack()
        for i in c.split():
            if i.isdigit():
                d = int(i)
                m1.hp-=d
        print(f"{c}\nу {m1.name}а осталось {m1.hp}")
    elif b == "2":
        w1.change_weapon(Sword())
    elif b == "3":
        w1.change_weapon(Bow())
    elif b == "4":
        print("Вы как трус убежали из подъземелья и больше никогда сюда не возвращались!")
        exit()
print(f"После победы над {m1.name}ом Вы нашли сундук и сокровищами и обрели вечную славу!")