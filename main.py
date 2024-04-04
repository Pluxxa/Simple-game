from abc import ABC, abstractmethod
import random


class Fighter():
    def __init__(self, name, st, hp, weapon, money=0):
        self.name = name
        self.st = st
        self.hp = hp
        self.weapon = weapon
        self.money = money

    def change_weapon(self, new_weapon):
        self.weapon = new_weapon
        print(f"Вы сменили оружие на {new_weapon.name}")

    def heal(self):
        self.hp+=20
        print("Вы вылечились на 20 жизней")


class Monster(ABC):
    @abstractmethod
    def attack(self):
        pass

class Zombe(Monster):
    def __init__(self, name, st, hp, weapon, cost=10):
        self.name = name
        self.st = st
        self.hp = hp
        self.weapon = weapon
        self.cost = cost

    def attack(self):
        return f"{self.name} сильно бьёт и наносит {random.randint(1, 10)} урона."

class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass


class Sword(Weapon):
    def __init__(self, apr=2, name="меч", damage=f"{random.randint(1,8)}"):
        self.name = name
        self.damage = damage
        self.apr = apr
    def attack(self):
        return f"Вы ударили и нанесли {random.randint(1,8)} урона"


class Bow(Weapon):
    def __init__(self, apr=3, name="лук", damage=f"{random.randint(1,6)}"):
        self.name = name
        self.damage = damage
        self.apr = apr
    def attack(self):
        return f"Вы выстрелили и нанесли {random.randint(1,8)} урона"

class MonsterAttack(ABC):
    @abstractmethod
    def attack(self):
        pass


class MonstrSword(MonsterAttack):
    def __init__(self, apr=2, name="меч", damage=f"{random.randint(1,6)}"):
        self.name = name
        self.damage = damage
        self.apr = apr
    def attack(self):
        return f"{m1.name} ударил по тебе и нанёс {random.randint(1,6)} урона"


class MonstrBow(MonsterAttack):
    def __init__(self, apr=2, name="ker", damage=f"{random.randint(1,4)}"):
        self.name = name
        self.damage = damage
        self.apr = apr
    def attack(self):
        return f"{m1.name} выстрелил по тебе и нанёс {random.randint(1,4)} урона"

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
        w = input("Выберете оружие из предлоенного списка: меч или лук\n")
name_list = ["жорик", "костехрухт", "мозгоед"]
name_weap = ["лук", "меч"]
w1 = Fighter(name, stren, hp, weap)
w = random.choice(name_weap)
if w.lower() == "лук":
    weap = MonstrBow()
elif w.lower() == "меч":
    weap = MonstrSword()
m1 = Zombe(random.choice(name_list), stren, random.randint(10, 30), weap)

a = input("Вы зашли в подземелье, перед Вами проход вперёд. Вы можете пойти прямо или повернуть назад. Куда вы направитесь?\n1 - прямо\n2 - уйти из подземелья\n")
if a == '1':
    print(f"Вы решили проти дальше. Как только вы отошли от входа подальше на Вас напало чудовище.")
elif a == "2":
    print("Вы как трус убежали из подъземелья и больше никогда сюда не возвращались!")
    exit()
while True:
    a_1 = input("Что ты будешь делать дальше?\n1 - идти дальше\n2 - забрать сокровища и уйти")
    if a_1 == "1":

        while m1.hp > 0:
            b = input(f"что вы делаете?\n1 - атаковать {m1.name}а\n2 - сменить оружие на меч\n3 - сменить оружие на лук\n4 - убежать в панике\n")
            if b == '1':
                for i in range(w1.weapon.apr):
                    c = w1.weapon.attack()
                    for j in c.split():
                        if j.isdigit():
                            d = int(j)
                            m1.hp-=d

                    print(f"{c}\nу {m1.name}а осталось {m1.hp}")
                for i in range(m1.weapon.apr):
                    c = m1.weapon.attack()
                    for j in c.split():
                        if j.isdigit():
                            d = int(j)
                            w1.hp-=d

                    print(f"{c}\nу {w1.name}а осталось {w1.hp}")

            elif b == "2":
                w1.change_weapon(Sword())
            elif b == "3":
                w1.change_weapon(Bow())
            elif b == "4":
                print("Вы как трус убежали из подземелья и больше никогда сюда не возвращались!")
                exit()
        print(f"Вы получили {m1.cost} серебрянных монет.")
        w1.money+=m1.cost
    elif a_1 == "2":
        print(f"После победы над {m1.name}ом Вы нашли сундук с сокровищами и обрели вечную славу!")
        exit()