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


# Generate random amount of gold for orcs
def gen_orc_gold():
    random_gold = random.randrange(10, 31)
    return random_gold


# Generate a random position for the monsters
def gen_ran_pos():
    random_monster_position = random.randrange(1, 99)
    return random_monster_position


# Create 10 orcs on the board
army_of_orcs = [Monster("Bald Orc", "m", gen_ran_pos(), " ", False, 100, 32, 2, False, gen_orc_gold(), 49) for _ in range(10)]

orc_boss = Monster("Destroyer Orc", "B", 99, "B", False, 500, 65, 10, False, 300, 100)
