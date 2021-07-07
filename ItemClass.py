import PlayerClass
from MonsterClass import gen_ran_pos


class Item:
    # The item class defines an item name, type, whether it is hidden on the board and its position
    trader_items = []

    def __repr__(self):
        return self.name

    def __init__(self, name, i_type, hidden, position, damage, defence, health, dexterity, intelligence, magic,
                 value, rarity, found, level, npc=None):

        self.name = name
        self.i_type = i_type
        self.hidden = hidden
        self.position = position
        self.u_times = 0
        self.defdamage = damage
        self.damage = damage
        self.defdefence = defence
        self.defence = defence
        self.health = health
        self.dexterity = dexterity
        self.intelligence = intelligence
        self.magic = magic
        self.value = value
        self.rarity = rarity
        self.found = found
        self.level = level
        if npc == 'trader':
            Item.trader_items.append(self)


class Spell:

    def __repr__(self):
        return self.name

    def __init__(self, name, hidden, position, found, int_req, value, description):
        self.name = name
        self.hidden = hidden
        self.position = position
        self.found = found
        self.int_req = int_req
        self.value = value
        self.description = description


def showStats():
    # Shows item statistics to the player
    item = input("Lookup item stats for: ").lower()

    if item in item_stats:
        print(f"\n{item_stats[item][0]}: Damage: {item_stats[item][1]} Defence: {item_stats[item][2]} "
              f"Rarity: {item_stats[item][3]}")

    else:
        print("Invalid item.")


def equip():
    # This function allows the user to equip items from inventory to the equipped items dict
    item = input("Which item to equip? ").lower()
    for i in PlayerClass.char.inventory:
        try:
            if item == i.name.lower():
                type_of_item = i.i_type
                # Add item to inventory, before replacing in equipped
                if PlayerClass.char.equipped_items[type_of_item] is not None:
                    PlayerClass.char.inventory.append(PlayerClass.char.equipped_items[type_of_item])
                PlayerClass.char.equipped_items[type_of_item] = i

                # Adjust player statistics
                # PlayerClass.char.hp += i.health
                # PlayerClass.char.defence += i.defence

                print(f"\n{i.name} is now equipped")
                PlayerClass.char.inventory.remove(i)
        except AttributeError:
            pass


def unequip():
    # This function acts as the opposite to the equip function.
    item = input("Which item to unequip? Helmet/Chest/Weapon/Shield ").lower().capitalize()
    if item in ['Helmet', 'Chest', 'Weapon', 'Shield']:
        i = PlayerClass.char.equipped_items[item]

        # Adjust stats for character without item
        # PlayerClass.char.hp -= i.health
        # PlayerClass.char.defence -= i.defence

        PlayerClass.char.equipped_items[item] = None
        print(f"\n{i.name} is now unequipped")
        PlayerClass.char.inventory.append(i)
    else:
        print("Please select one of the available options.")


# name, i_type, hidden, position, damage, defence, health, dexterity, intelligence, magic, value, rarity, found,
# level, NPC
# Create normal items
wooden_stick = Item("Wooden Stick", "Weapon", " ", None, 5, 0, 0, 2, 0, 0, 65, "Normal", False, 0)
wooden_shield = Item("Wooden Shield", "Shield", " ", None, 0, 5, 0, 2, 0, 0, 50, "Normal", False, 0)
leather_cap = Item("Leather Cap", "Helmet", " ", gen_ran_pos(), 0, 7, 2, 0, 0, 0, 45, "Normal", False, 0, 'trader')
leather_armour = Item("Leather Armour", "Chest", " ", gen_ran_pos(), 0, 12, 2, 0, 0, 0, 60, "Normal", False, 0, 'trader')
iron_sword = Item("Iron Sword", "Weapon", " ", None, 25, 0, 0, -1, 0, 0, 180, "Normal", False, 0, 'trader')
iron_armour = Item("Iron Armour", "Chest", " ", None, 0, 27, 0, -3, 0, 0, 160, "Normal", False, 0, 'trader')
iron_shield = Item("Iron Shield", "Shield", " ", None, 0, 22, 0, -2, 0, 0, 120, "Normal", False, 0, 'trader')
iron_helmet = Item("Iron Helmet", "Helmet", " ", None, 0, 17, 0, -1, 0, 0, 100, "Normal", False, 0, 'trader')

# Create rare items
dragon_plate = Item("Dragon Plate", "Chest", " ", None, 0, 35, 15, -3, 5, 10, 350, "Rare", False, 0, 'trader')
half_moon_katana = Item("Half Moon Katana", "Weapon", " ", None, 40, 0, 0, 6, 6, 6, 480, "Rare", False, 0, 'trader')

# Create unique items
one_hit_wonder = Item("One Hit Wonder", "Weapon", " ", None, 500, 0, 0, 0, 10, 10, 5000, "Unique", False, 0, 'trader')

# Item statistics dictionary, hold names, damage, defence and rarity stats for an item
item_stats = {
    "wooden stick": [wooden_stick.name,
                     wooden_stick.damage,
                     wooden_stick.defence,
                     wooden_stick.dexterity,
                     wooden_stick.intelligence,
                     wooden_stick.magic,
                     wooden_stick.rarity],

    "wooden shield": [wooden_shield.name,
                      wooden_shield.damage,
                      wooden_shield.defence,
                      wooden_shield.dexterity,
                      wooden_shield.intelligence,
                      wooden_shield.magic,
                      wooden_stick.rarity],

    "leather cap": [leather_cap.name,
                    leather_cap.damage,
                    leather_cap.defence,
                    leather_cap.dexterity,
                    leather_cap.intelligence,
                    leather_cap.magic,
                    leather_cap.rarity],

    "leather armour": [leather_armour.name,
                       leather_armour.damage,
                       leather_armour.defence,
                       leather_armour.dexterity,
                       leather_armour.intelligence,
                       leather_armour.magic,
                       leather_armour.rarity],

    "iron sword": [iron_sword.name,
                   iron_sword.damage,
                   iron_sword.defence,
                   iron_sword.dexterity,
                   iron_sword.intelligence,
                   iron_sword.magic,
                   iron_sword.rarity],

    "iron armour": [iron_armour.name,
                    iron_armour.damage,
                    iron_armour.defence,
                    iron_armour.dexterity,
                    iron_armour.intelligence,
                    iron_armour.magic,
                    iron_armour.rarity],

    "iron shield": [iron_shield.name,
                    iron_shield.damage,
                    iron_shield.defence,
                    iron_shield.dexterity,
                    iron_shield.intelligence,
                    iron_shield.magic,
                    iron_shield.rarity],

    "iron helmet": [iron_helmet.name,
                    iron_helmet.damage,
                    iron_helmet.defence,
                    iron_helmet.dexterity,
                    iron_helmet.intelligence,
                    iron_helmet.magic,
                    iron_helmet.rarity],

    "dragon plate": [dragon_plate.name,
                     dragon_plate.damage,
                     dragon_plate.defence,
                     dragon_plate.dexterity,
                     dragon_plate.intelligence,
                     dragon_plate.magic,
                     dragon_plate.rarity],

    "half moon katana": [half_moon_katana.name,
                         half_moon_katana.damage,
                         half_moon_katana.defence,
                         half_moon_katana.dexterity,
                         half_moon_katana.intelligence,
                         half_moon_katana.magic,
                         half_moon_katana.rarity],

    "one hit wonder": [one_hit_wonder.name,
                       one_hit_wonder.damage,
                       one_hit_wonder.defence,
                       one_hit_wonder.dexterity,
                       one_hit_wonder.intelligence,
                       one_hit_wonder.magic,
                       one_hit_wonder.rarity]
}

on_board_items = [leather_cap, leather_armour]


# --- Spell functions below - should start with s_followed_by_name --- #

def s_fire_ball(monster):
    # Cast a fireball that deals 60 base damage

    reduced_hit = max((PlayerClass.char.magic + 60) / monster.defence, 0)
    monster.hp -= reduced_hit
    print("\nYou cast a spell...")
    print("\n-------------------------------------------------")
    print(f"You hit {monster.name} for {round(reduced_hit, 2)} damage... {monster.name}"
          f" has {round(monster.hp, 2)}hp remaining")
    print("-------------------------------------------------")


# --- Spell Dictionary ---#
spell_dict = {
    "Fire Ball": s_fire_ball,
}

# Create a spell
fire_ball = Spell("Fire Ball", " ", None, False, 10, 50, "Cast a Fire Ball that deals 60 base damage to any enemy.")
