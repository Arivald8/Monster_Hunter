import sys


class Player:

    def __init__(self, name, player, position, hp, strength, defence, dexterity, intelligence, magic, level, xp):

        self.name = name
        self.player = player
        self.position = position
        self.hp = hp
        self.strength = strength
        self.defence = defence
        self.dexterity = dexterity
        self.intelligence = intelligence
        self.magic = magic

        self.race = ''
        self.race_type = ''

        self.level = level
        self.xp = xp

        self.inventory = []
        self.equipped_items = {"Helmet": None,
                               "Chest": None,
                               "Weapon": None,
                               "Shield": None
                               }
        self.gold = 0

    def levelUp(self):
        new_level = self.xp // 100
        if new_level > self.level:
            levelup = True
            print("You leveled up!")
            print("You can level up one of the following: Health/Strength/Defence/Dexterity/Intelligence/Magic").lower()
            while levelup:
                stat = input("Which will it be? > ")
                if stat == "health":
                    char.hp += 5
                elif stat == "strength":
                    char.strength += 1
                elif stat == "defence":
                    char.defence += 1
                elif stat == "dexterity":
                    char.dexterity += 1
                elif stat == "intelligence":
                    char.intelligence += 5
                elif stat == "magic":
                    char.intelligence += 1
                else:
                    print("Please pick a valid statistic.")
                    continue
                levelup = False

        self.level = new_level


    def add_item(self, item):
        self.inventory.append(item)

    def show_inventory(self):
        print("---------------------")
        print("--Small Leather Bag--")
        print("---------------------")
        print(f"{self.inventory}")
        print("---------------------")
        print("------Equipped-------")
        print("---------------------")
        for listed_item in self.equipped_items:
            print(f'       {listed_item}\n')
            print(f'       {self.equipped_items[listed_item]}')
            print("---------------------")
        print(f"Gold: {round(self.gold, 2)}")

    def showStats(self):
        '''
        Only additional damage is calculated and added here. For other additional attributes like hp or defence
        look at ItemClass.py. Some of the below code is there for later. Might get rid of it, but it works for now.
        '''
        shield = self.equipped_items['Shield']
        try:
            shield_def = shield.defence
            shield_hp = shield.health
            shield_dmg = shield.damage
        except AttributeError:
            shield_def = 0
            shield_hp = 0
            shield_dmg = 0

        helmet = self.equipped_items['Helmet']
        try:
            helmet_def = helmet.defence
            helmet_hp = helmet.health
            helmet_dmg = helmet.damage
        except AttributeError:
            helmet_def = 0
            helmet_hp = 0
            helmet_dmg = 0

        chest = self.equipped_items['Chest']
        try:
            chest_def = chest.defence
            chest_hp = chest.health
            chest_dmg = chest.damage
        except AttributeError:
            chest_def = 0
            chest_hp = 0
            chest_dmg = 0

        weapon = self.equipped_items['Weapon']
        try:
            weapon_dmg = weapon.damage
            weapon_hp = weapon.health
            weapon_def = weapon.defence
        except AttributeError:
            weapon_dmg = 0
            weapon_hp = 0
            weapon_def = 0

        print(f"\nCharacter Card:\n"
              f"-----------------------\n"
              f"Health:                     {round(self.hp, 2):9.2f}\n"
              f"Level:                      {self.level:9d}\n"
              f"Current XP:                 {self.xp:9d}")
        print(f"Name: {self.player:>31s}\n"
              f"Race: {self.race:>31s}\n"
              f"Type: {self.race_type:>31s}\n"
              f"-----------------------\n"
              f"Base/ Total Strength:       ({self.strength:3d}) {(self.strength + weapon_dmg + chest_dmg + helmet_dmg + shield_dmg):3d}\n"
              f"Base/ Total Defence:        ({self.defence:3d}) {self.defence:3d}\n"
              f"Base/ Total Dexterity:      ({self.dexterity:3d}) {self.dexterity:3d}\n"
              f"Base/ Total Intelligence:   ({self.intelligence:3d}) {self.intelligence:3d}\n"
              f"Base/ Total Magic:          ({self.magic:3d}) {self.magic:3d}\n"
              f"-----------------------")


def createCharacter():
    the_player = [0, 0, 0, 0, 0]
    race = ""
    race_type = ""

    creation = True
    while creation:
        line = "------------------------"

        print(line * 2)
        print("---Character Creation---")
        print(line * 2)
        user_input = input("Type any key to continue... > ")
        if user_input == 'exit':
            sys.exit()
        else:
            name = input("\nEnter Your Name: ")
            print(line)
            print("You're going to have to choose a race...\n")
            print("\nHuman: \n"
                  "Humans (Homo sapiens) are the only extant members of the subtribe Hominina. Together with chimpanzees, gorillas \n"
                  "and orangutans, they are part of the Hominidae family. Humans are terrestrial animals, characterized by their \n"
                  "erect posture and bipedal locomotion; high manual dexterity and heavy tool use compared to other animals; \n"
                  "open-ended and complex language use compared to other animal communications; larger, more complex brains than \n"
                  "other animals; and highly advanced and organized societies\n"
                  "\n"
                  "Human base statistics: \n"
                  "Strength:        5\n"
                  "Defence:         2\n"
                  "Dexterity:       3\n"
                  "Intelligence:    4\n"
                  "Magic            0\n")
            print(line * 4)
            input("Type any key to continue... > ")
            print("\nElf: \n"
                  "An elf is a type of human-like supernatural being in Germanic mythology and folklore. In medieval \n"
                  "Germanic-speaking cultures, elves seem generally to have been thought of as beings with magical powers and \n"
                  "supernatural beauty, ambivalent towards everyday people and capable of either helping or hindering them. \n"
                  "However, the details of these beliefs have varied considerably over time and space, and have flourished in both \n"
                  "pre-Christian and Christian cultures. \n"
                  "\n"
                  "Elf base statistics: \n"
                  "Strength:        1\n"
                  "Defence:         2\n"
                  "Dexterity:       4\n"
                  "Intelligence:    5\n"
                  "Magic            2\n")
            print(line * 4)
            input("Type any key to continue... > ")

            print("\nUndead: \n"
                  "The undead are beings in mythology, legend, and fiction that are deceased but behave as if they were alive. The \n"
                  "undead are featured in the belief systems of most cultures, and appear in many works of fantasy and horror. The \n"
                  "term is also occasionally used for putative non-supernatural cases of re-animation.\n"
                  "\n"
                  "Undead base statistics: \n"
                  "Strength:        3\n"
                  "Defence:         5\n"
                  "Dexterity:       1\n"
                  "Intelligence:    0\n"
                  "Magic            5\n")
            print(line * 4)
            input("Type any key to continue... > ")

            print("\nAlien: \n"
                  "Alien life, such as microorganisms, has been hypothesized to exist in the Solar System and throughout the \n"
                  "universe. This hypothesis relies on the vast size and consistent physical laws of the observable universe. \n"
                  "According to this argument, made by scientists such as Carl Sagan and Stephen Hawking, it would be improbable \n"
                  "for life not to exist somewhere other than Earth. Such life might range from simple prokaryotes to beings with \n"
                  "civilizations far more advanced than humanity.\n"
                  "\n"
                  "Alien base statistics: \n"
                  "Strength:        1\n"
                  "Defence:         1\n"
                  "Dexterity:       1\n"
                  "Intelligence:    10\n"
                  "Magic            1\n")
            print(line * 4)

            correct_pick = False
            while not correct_pick:
                race = input("And who might you be? [Human/Elf/Undead/Alien]: ").lower().capitalize()
                valid_picks = ['Human', 'Elf', 'Undead', 'Alien']
                if race in valid_picks:
                    if race == 'Human':
                        the_player = [5, 2, 3, 4, 0]
                    elif race == 'Elf':
                        the_player = [1, 2, 4, 5, 2]
                    elif race == 'Undead':
                        the_player = [3, 5, 1, 0, 5]
                    elif race == 'Alien':
                        the_player = [1, 1, 1, 10, 1]
                    correct_pick = True
                else:
                    print("Invalid race choice. Try again.")

            print("\nWhat is your specialty?\n")
            print("Warrior:\n"
                  "\n"
                  "Warriors seem to have been present in the earliest pre-state societies. Along with hunting, war was considered \n"
                  "to be a definitive male activity. No matter the pretext for combat, it seemed to have been a rite of passage for\n"
                  "a boy to become a man. Warriors took upon costumes and equipment that seemed to have a symbolic significance; \n"
                  "combat itself would be preceded by ritual or sacrifice. Men of fighting age often lived apart in order to \n"
                  "encourage bonding, and would ritualise combat in order to demonstrate individual prowess among one another.\n"
                  "\n"
                  "Warrior specific stats: \n"
                  "Strength +3\n"
                  "Defence  +3\n")
            print(line * 4)
            input("Type any key to continue... > ")

            print("\nMage: \n"
                  "\n"
                  "A Mage is someone who uses or practices magic derived from supernatural, occult, or arcane sources. The wizard \n"
                  "often appears as a wise old man and acts as a mentor, who is often depicted as old, white-haired, and with a long\n"
                  "white beard, majestic enough to occasionally host lurking woodland creatures.\n"
                  "\n"
                  "Mage specific stats: \n"
                  "Intelligence + 3\n"
                  "Magic        + 3\n")
            print(line * 4)
            input("Type any key to continue... > ")

            print("\nPaladin: \n"
                  "\n"
                  "The Paladin (alternatively sometimes called Templar or Crusader) is a Holy Warrior, combining aspects of both \n"
                  "a Warrior and a Cleric. First and foremost, Paladin is proficient with heavy arms and armor. Yet at the same time\n"
                  "a Paladin is gifted with blessings or magical capabilities such as healing, protection, and countering evil magic.\n"
                  "\n"
                  "Paladin specific stats: \n"
                  "Strength +3\n"
                  "Magic    +3\n")
            print(line * 4)
            input("Type any key to continue... > ")

            print("\nThief: \n"
                  "\n"
                  "Thieves are usually stealthy and dexterous. They are nimble melee or ranged combatants, and tend to be\n"
                  "focused on dodging attacks rather than withstanding damage. They often attack by dual-wielding daggers or with \n"
                  "other small one-handed and/or concealable weapons, relying on speed and rapid strikes rather than sheer damage \n"
                  "output. Thieves usually work in small groups or guilds.\n"
                  "\n"
                  "Thief specific stats: \n"
                  "Dexterity    +3\n"
                  "Intelligence +3\n")

            correct_pick2 = False
            while not correct_pick2:
                race_type = input("You are a [Warrior/Mage/Paladin/Thief]: ").lower().capitalize()
                valid_picks = ['Warrior', 'Mage', 'Paladin', 'Thief']
                if race_type in valid_picks:
                    if race_type == 'Warrior':
                        the_player[0] += 3
                        the_player[1] += 3
                    elif race_type == 'Mage':
                        the_player[3] += 3
                        the_player[4] += 3
                    elif race_type == 'Paladin':
                        the_player[0] += 3
                        the_player[4] += 3
                    elif race_type == 'Thief':
                        the_player[2] += 3
                        the_player[3] += 3
                    correct_pick2 = True
                else:
                    print("Invalid choice. Try again.")
            print(line * 3)
            print(f"\nAnd just like that, {name} was born.\n")

            return the_player, name, race, race_type


# name, player, position, hp, strength, defence, dexterity, intelligence, magic, level, xp

char = Player("P", " ", 0, 100, 0, 0, 0, 0, 0, 0, 0)
