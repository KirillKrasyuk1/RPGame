# Classes for a game
import time
import random


global faith
global damage
chance_to_escape = 0
class Character(object):
    def __init__(self, HP, damage):
        self.HP = HP
        self.damage = damage
    def show_stats(self):
        print(f'Characteristics are: HP - {self.HP}, damage - {self.damage}')

class Monster(Character):
    def __init__(self, HP,  damage, type):
        super().__init__(HP, damage)
        self.type = type
    def attack(self, target):
        target.HP -= self.damage
        if target.HP <= 0:
            print('player is dead')
            quit()
        else:
            print(f'player has {target.HP} HP. Damage was {self.damage}')
            time.sleep(1)

class Gamer(Character):
    def __init__(self, HP, damage, exp, levels, name, chance_to_escape):
        super().__init__(HP, damage)
        self.exp = exp
        self.levels = levels
        self.name = name
        self.chance_to_escape = chance_to_escape

    def show_stats(self):
        print(f'Your characteristics are: HP - {self.HP}, damage - {self.damage}, exp - {self.exp}, level - {self.levels}')

    def attack(self,target,):
        target.HP -= self.damage
        if target.HP <= 0:
            print('target is dead')
            time.sleep(1)
            if target.type == 'орк':
                exp = 40
                base_drop_chance = 4
            if target.type == 'гоблин':
                exp = 30
                base_drop_chance = 3
            if target.type == 'огр':
                exp = 50
                base_drop_chance = 6
            drop_chance = base_drop_chance + random.randint(4, 7)
            if drop_chance >= 10:
                drop = random.choice(weapon)
                print(f'вам выпал {drop}')
                answer = input(f'вы хотите экипировать {drop}?1 - да, 2 - нет.')
                if answer == 'да':
                    if drop == "меч":
                        if faith == '2':
                            print('вы экипировали меч')
                            damage += 8
                        else:
                            print('это оружие вам не подходит')
                    if drop == 'лук':
                        if faith == '1':
                            print('вы экипировали лук')
                            damage += 10
                        else:
                            print('это оружие вам не подходит')
                    if drop == 'посох':
                        if faith == '3':
                            print('вы экипировали посох')
                            damage += 12
                        else:
                            print('это оружие вам не подходит')
                    time.sleep(1)
                elif answer == 'нет':
                    print('Вы пололжили это к себе в сумку.')
                    backpack.append(drop)
            self.exp += exp
            if self.exp >= 100:
                self.levels += 1
                self.HP += 1
                self.damage += 1
                self.exp = 0
                print(f'Congratulations, You have achieved {self.levels} level. Each of your characteristics is increased by 1')
                return False
        else:
            print(f'target has {target.HP} HP. Damage was {self.damage}')
            time.sleep(1)
            return True


# modules separate from classes
def create_person():
    debug = True
    if debug == True:
        player = Gamer(100, 25, 0, 0, 'Kirill', 4,)
        return player
    else:
        name = input("enter you name, traveler\n")
        while True:
            faith = input('Choose your path:\n 1 - Archer,2 - Knight, 3 - Mage.\n')
            if faith == '1':
                HP, damage, chance_to_escape = 125, 25, 5
            elif faith == '2':
                HP, damage, chance_to_escape = 150, 20, 4
            elif faith == '3':
                HP, damage, chance_to_escape = 100, 30, 3
            else:
                print("You made a mistake.")
                continue
            break
        while True:
            race = input("choose you race:\n 1 - Elf, 2 - Dwarf, 3 - Human\n")
            if race == '1':
                if faith == '1':
                    damage += 10
                    print('you get a racial bonus to the class')
            elif race == '2':
                if faith == '2':
                    HP += 20
                    print('you get a racial bonus to the class')
            elif race == '3':
                if faith == '3':
                    damage += 15
                    print('you get a racial bonus to the class')
            else:
                print('You made a mistake.')
                continue
            break

        player = Gamer(HP, damage, 0 , 0, name, chance_to_escape)
        return player

def fight_choice():
     choice = input('выберете свое дальнейшее действие\n 1 - бежать, 2 - драться\n')
     if choice == '1':
        run = random.randint(0,4)
        player.chance_to_escape += run
        if player.chance_to_escape >= 7:
            print('мы бежим')
            return
        else:
            print('сбежать не удалось.')
            monster.attack(player)
            monster.attack(player)
            fight_choice()
     elif choice == '2':
         is_target_alive = player.attack(monster)
         if is_target_alive:
             time.sleep(0.5)
             monster.attack(player)
             fight_choice()

# game

print('There are legends about certain dungeons that can make anyone rich who enters them and gets out alive, but legends\n are legends, and there will always be a person who wants to refute them.\n You turn out to be such a person and go to these creepy dungeonsto refute the lies.')
player = create_person()
player.show_stats()
#создать функцию create_monster по аналогии с crate_person или в ветках if задавать параметры и создавать экземпляры класса.
weapon = ['меч',"лук","посох"]
backpack = []
while True:
        rnd = random.randint(0,1)
        if rnd == 0:
            print('по пути вам никто не встрeтился.')
            time.sleep(1)
        if rnd == 1:
            monster_chance = random.randint(0,2)
            if monster_chance == 0:
                print('Вам встретился орк')
                monster = Monster(100,15,'орк')
                monster.show_stats()
            if monster_chance == 1:
                print('Вам встретился гоблин')
                monster = Monster(70,20,'гоблин')
                monster.show_stats()
            if monster_chance == 2:
                print('Вам встретился огр')
                monster = Monster(200,30,'огр')
                monster.show_stats()
            fight_choice()