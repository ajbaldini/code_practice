import random

class Weapon:

    def __init__(self, name, damage, attack_bonus):
        self.name = name
        self.damage = damage
        self.attack_bonus = attack_bonus

    def get_attack_bonus(self):
        return self.damage


class Character:

    def __init__(self, char_class, weapon, athletics ,arcana ,quickness, life):
        self.char_class = char_class
        self.weapon = weapon
        self.athletics = athletics
        self.arcana = arcana
        self.quickness = quickness
        self.life = life

    def attack(self, target):

        hero_life = target.life
        monster_life = self.life

        while hero_life > 0 and monster_life > 0:

            print(f"{self.char_class} attacks {target.name}")
            roll = random.randint(1,100)
            if roll + self.weapon.attack_bonus > 60:
                print(f"HIT! {self.weapon.damage} to {target.name}")
                hero_life -= self.weapon.damage
                print(f"{target.name} has {hero_life} life left.")
            else:
                print(f"{self.char_class} misses")

            print(f"{target.name} attacks {self.char_class}")
            roll = random.randint(1,100)
            if roll + target.weapon.attack_bonus > 60:
                print(f"HIT! {self.weapon.damage} to {self.char_class}")
                monster_life -= target.weapon.damage
                print(f"{self.char_class} has {monster_life} life left")
            else:
                print(f"{target.name} misses")

        if hero_life < 0 and monster_life < 0:
            print(f"A DOUBLE KNOCK OUT!")
        elif hero_life < 0:
            print(f"{target.name} lost the fight.")
        else:
            print(f"{self.char_class} defeated. ")

class PlayerCharacter(Character):

    inventory = []
    spells_known = []

    def __init__(self, name, weapon, char_class, athletics, arcana, quickness, life):
        self.name = name
        Character.__init__(self, char_class, weapon, athletics, arcana, quickness, life)

class Monster(Character):

    def __init__(self, char_class, weapon, athletics,arcana,quickness, life):
        Character.__init__(self,char_class, weapon, athletics,arcana,quickness, life)

badguy = Monster("orc",Weapon("claws", 10, 10),15,5,10,30)
hero = PlayerCharacter("antius",Weapon("hands", 5, 15),"human",10,10,10,25)

badguy.attack(hero)

print(f"{hero.name} gets a short sword!")

hero.weapon.name = "short sword"
hero.weapon.damage = 20
hero.weapon.attack_bonus = 20

badguy.attack(hero)