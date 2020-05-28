class Player:
    """
        Player class defines the name, position and whether a player has found the monster.
        The class also holds an inventory for a player.
        There are two methods, one which adds an item to the inventory
        and another which displays the content of the inventory
    """

    def __init__(self, name, position, hp, strength, defence, level, xp):
        self.name = name
        self.position = position
        self.hp = hp
        self.strength = strength
        self.defence = defence
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
            print("You can level up one of the following: Health/Strength/Defence")
            while levelup:
                stat = input("Which will it be? > ")
                if stat == "Health":
                    char.hp += 5
                    levelup = False
                elif stat == "Strength":
                    char.strength += 5
                    levelup = False
                elif stat == "Defence":
                    char.defence += 5
                    levelup = False
                else:
                    print("Please pick a valid statistic.")

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
        print("       Helmet        \n")
        print(f"       {self.equipped_items['Helmet']}")
        print("---------------------")
        print("       Armour        \n")
        print(f"       {self.equipped_items['Chest']}")
        print("---------------------")
        print("       Weapon        \n")
        print(f"       {self.equipped_items['Weapon']}")
        print("---------------------")
        print("       Shield        \n")
        print(f"       {self.equipped_items['Shield']}")
        print("---------------------")
        print(f"Gold: {round(self.gold, 2)}")

    def showStats(self):
        print("-----------------------")
        print("--Character Statistic--")
        print("-----------------------")
        print(f"Your base Attack: {self.strength}")
        print("-----------------------")

        # Calculate defence and damage stats from items
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

        print(f"Your Total Health: {round(self.hp, 2)}")
        print(f"Your Total Attack: {self.strength + weapon_dmg + chest_dmg + helmet_dmg + shield_dmg}")
        print(f"Your Total Defence: {self.defence}")
        print(f"Level: {self.level}")
        print(f"Current XP: {self.xp}")
        print("-----------------------")


char = Player("P", 0, 100, 3, 1, 0, 0)
