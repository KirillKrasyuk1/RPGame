# modules for a game
import time
import random


chance_to_escape = 0


# Classes for a game

# Origin class
class Character(object):
    def __init__(self, HP, damage):
        self.HP = HP
        self.damage = damage
    def show_stats(self):
        print(f'Characteristics are: HP - {self.HP}, damage - {self.damage}')

# Enemy class
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


class RaidBoss(Monster):
    def __init__(self, HP, damage, type, crit_chance, regen):
        super().__init__(HP, damage, type)
        self.crit_chance = crit_chance
        self.regen = regen
        self.FullHP = HP
    def attack(self, target):
        CritChance = random.randint(1, 10)
        if CritChance == 10:
            target.HP -= round(self.damage * 1.5)
            print('Босс нанес вам крит. урон.')
        else:
            target.HP -= self.damage
        if target.HP <= 0:
            print('player is dead')
            quit()
        else:
            print(f'player has {target.HP} HP. Damage was {self.damage}')
            self.HP += self.FullHP * 0.01
            print('Босс частично восстановил свое здоровье.')
            time.sleep(1)

# Player class
class Gamer(Character):
    def __init__(self, HP, damage, exp, levels, name, chance_to_escape, Class, money):
        super().__init__(HP, damage)
        self.exp = exp
        self.levels = levels
        self.name = name
        self.chance_to_escape = chance_to_escape
        self.is_equipped = False
        self.backpack = []
        self.Class = Class
        self.money = money

# my modules for a game

# show characteristics
    def show_stats(self):
        print(f'Your characteristics are: HP - {self.HP}, damage - {self.damage}, exp - {self.exp}, level - {self.levels}')

#attack module
    def attack(self,target):
        target.HP -= self.damage
        if target.HP <= 0:
            print('target is dead')
            time.sleep(1)
            if target.type == 'orc':
                exp = 40
                base_drop_chance = 10
                money = random.randint(30, 50)
            if target.type == 'goblin':
                exp = 30
                base_drop_chance = 10
                money = random.randint(15, 30)
            if target.type == 'og':
                exp = 50
                base_drop_chance = 10
                money = random.randint(75, 125)
            drop_chance = base_drop_chance + random.randint(4, 7)
            if drop_chance >= 10:
                drop = random.choice(weapon)
                print(f'you got a {drop}')
                answer = input(f'Do you want to equip {drop}? 1 - да, 2 - нет.')
                if answer == '1':
                    if self.is_equipped == False:
                        if drop == "меч":
                            if self.Class == 'Knight':
                                print('you have equipped the sword.')
                                self.damage += 8
                            else:
                                print('this weapon is not suitable for you.')
                        if drop == 'лук':
                            if self.Class == '1':
                                print('you have equipped the bow.')
                                self.damage += 10
                            else:
                                print('this weapon is not suitable for you.')
                        if drop == 'посох':
                            if self.Class == '3':
                                print('you have equipped the staff.')
                                self.damage += 12
                            else:
                                print('this weapon is not suitable for you.')
                        print(self.damage)
                        self.is_equipped = True
                    elif self.is_equipped == True:
                        print('You have already equipped your weapons.')
                    time.sleep(1)
                elif answer == '2':
                    print('You put it in your bag.')
                    self.backpack.append(drop)
                    print(self.backpack)
                    time.sleep(1)
            self.money += money
            print(f'вы заработали {money}. Общее количество денег {self.money}')
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

# create person
def create_person():
    debug = True
    if debug == True:
        player = Gamer(10000, 10, 0, 0, 'Kirill', 4, '3', 100)
        return player
    else:
        name = input("enter you name, traveler\n")
        while True:
            faith = input('Choose your path:\n 1 - Archer,2 - Knight, 3 - Mage.\n')
            if faith == '1':
                HP, damage, chance_to_escape, Class = 125, 25, 5, "Archer"
            elif faith == '2':
                HP, damage, chance_to_escape, Class = 150, 20, 4, "Knight"
            elif faith == '3':
                HP, damage, chance_to_escape, Class = 100, 30, 3, "Mage"
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

        player = Gamer(HP, damage, 0 , 0, name, chance_to_escape, Class)
        return player

# Gives a choice in a fight
def fight_choice(monster):
     print(monster.HP)
     choice = input('choose your next action\n 1 - run, 2 - fight 3 - regen\n')
     if choice == '1' and monster.type != 'raid_boss':
        run = random.randint(0,4)
        player.chance_to_escape += run
        if player.chance_to_escape >= 7:
            print("we're escape")
            return
        else:
            print('escape failed.')
            monster.attack(player)
            monster.attack(player)
            fight_choice(monster)
     elif choice == '2':
         is_target_alive = player.attack(monster)
         if is_target_alive:
             time.sleep(0.5)
             monster.attack(player)
             fight_choice(monster)
     elif choice == '3':
         choice = input('Какое зелье вы хотите выпить? 1 - LHP 2 - MHP 3 - HHP')
         if choice == '1' and players_health_potions['low potion'] >= 1:
             player.HP += 20
             players_health_potions['low potion'] -= 1
         if choice == '2' and players_health_potions['medium potion'] >= 1:
             player.HP += 35
             players_health_potions['medium potion'] -= 1
         if choice == '3' and players_health_potions['high potion'] >= 1:
             player.HP += 60
             players_health_potions['high potion'] -= 1
         else:
             print('У вас нет зелий данного типа.')
         fight_choice(monster)
     else:
        print('От босса невозможно убежать')
        is_target_alive = player.attack(monster)
        if is_target_alive:
            time.sleep(0.5)
            monster.attack(player)
            fight_choice(monster)

def go_to_merchant():
    choice = input('choose your next action\n 1 - go to merchant, 2 - continue adventure\n')
    costs = [10, 20, 40]
    if choice == '1':
        choice = input('что вы хотите сделать?\n 1 - купить 2 - продать')
        if choice == '1':
            while True:
                print(f'{player.money} - your money')
                print(f"{'Press number to buy':<30}{'good':<20} {'chars':<20} {'money':<20}{'amount':<20}")
                for i in range(3):
                    print(f'{i + 1:<30}{list(health_potions.keys())[i]:<22}{20 * (i + 1):<22}{costs[i]:<20}{list(health_potions.values())[i]:<20}')
                print('нажмите 4 чтобы выйти')
                choice = input('')
                if choice == "1":
                    if player.money >= costs[0] and health_potions['low potion'] >= 1:
                        players_health_potions['low potion'] += 1
                        player.money -= costs[0]
                        health_potions['low potion'] -= 1
                        print('покупка совершена успешно')
                        #TODO добавить вывод осатльных хилок
                        print(f'LHP - {players_health_potions["low potion"]}')
                    else:
                        print('Невозможно купить в данный момент')
                if choice == "2":
                    if player.money >= costs[1] and health_potions['medium potion'] >= 1:
                        players_health_potions['medium potion'] += 1
                        player.money -= costs[1]
                        health_potions['medium potion'] -= 1
                    else:
                        print('Невозможно купить в данный момент')
                if choice == "3":
                    if player.money >= costs[2] and health_potions['high potion'] >= 1:
                        players_health_potions['high potion'] += 1
                        player.money -= costs[2]
                        health_potions['high potion'] -= 1
                    else:
                        print('Невозможно купить в данный момент')
                if choice == '4':
                    break
        if choice == '2':
            choice = input('вы хотите продать свои вещи? 1 - да/ любая другая клавиша - нет')
            if choice == '1':
                player.money += len(player.backpack) * 30
                print(f'вы получили {len(player.backpack) * 30}. Ваш капитал составляет {player.money}')



def go_to_raid_boss(HP, damage, crit_chance, regen):
    bosses = ['Скелетрона',"Эндер Дракона",'Судию Гундир']
    boss = random.choice(bosses)
    print(f'вы встретили {boss}')
    monster = RaidBoss(HP, damage, 'raid_boss', crit_chance, regen)
    fight_choice(monster)
# Game

print('There are legends about certain dungeons that can make anyone rich who enters them and gets out alive, but legends\n are legends, and there will always be a person who wants to refute them.\n You turn out to be such a person and go to these creepy dungeonsto refute the lies.')
player = create_person()
player.show_stats()
weapon = ['sword',"bow","staff"]
health_potions = {'low potion' : 15, 'medium potion' : 10, 'high potion': 5}
players_health_potions = {'low potion' : 0, 'medium potion' : 0, 'high potion': 0}
counter = 0
stage = 1
is_allowed_to_go_to_merchant = True
while True:
    if is_allowed_to_go_to_merchant == True:
        go_to_merchant()
    if counter >= 2:
        answer = input('вы хотите отправиться в комнатку с боссом?\n 1 -да 2 - нет\n')
        if answer == "1":
            go_to_raid_boss(500, 45, 20, 25)

    rnd = random.randint(0,1)
    if rnd == 0:
        print("you didn't meet anyone along the way.")
        is_allowed_to_go_to_merchant = False
        time.sleep(1)
    if rnd == 1:
        monster_chance = random.randint(0,2)
        if monster_chance == 0:
            print('You met an orc')
            monster = Monster(100,15,'orc')
            monster.show_stats()
        if monster_chance == 1:
            print('You met an goblin')
            monster = Monster(70,20,'goblin')
            monster.show_stats()
        if monster_chance == 2:
            print('You met the og')
            monster = Monster(200,30,'og')
            monster.show_stats()
        fight_choice(monster)
        #del monster
    counter += 1