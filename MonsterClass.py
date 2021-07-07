import random


class Monster:
    # The monster class defines a name, position and whether the monster is currently hidden on the board

    def __init__(self, name, symbol, position, hidden, found, hp, attack, defence, defeated, gold_loot, xp):
        self.name = name
        self.symbol = symbol
        self.position = position
        self.hidden = hidden
        self.found = found
        self.hp = hp
        self.attack = attack
        self.defence = defence
        self.defeated = defeated
        self.gold_loot = gold_loot
        self.xp = xp


# Generate a random position for the monsters
def gen_ran_pos():
    random_monster_position = random.randrange(2, 99)
    return random_monster_position


# Create 10 orcs on the board
''' <torbray> ORC STATS
  For Orcs 0 to 9 (variable = i):
  - Attack:     i + 20          20 - 29
  - Defence:    i // 4 + 2      2 - 4
  - Gold:       4 * (i + 15)    60 - 96
  - XP:         3 * (i + 15)    45 - 72
'''
army_of_orcs = [Monster("Bald Orc", 'm', gen_ran_pos(), " ", False, 100, i + 20, i // 4 + 2, False, 4 * (i + 15), 3 * (i + 15)) for i in range(10)]

orc_boss = Monster("Destroyer Orc", "B", 99, "B", False, 500, 45, 8, False, 300, 0)
