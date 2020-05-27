import PlayerClass


class Item:
    # The item class defines an item name, type, whether it is hidden on the board and its position

    def __repr__(self):
        return self.name

    def __init__(self, name, i_type, hidden, position, damage, defence, health, value, rarity):
        self.name = name
        self.i_type = i_type
        self.hidden = hidden
        self.position = position
        self.damage = damage
        self.defence = defence
        self.health = health
        self.value = value
        self.rarity = rarity


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
    item = input("Which item to equip? ")
    for i in PlayerClass.char.inventory:
        try:
            if item != i.name:
                pass
            elif item == i.name:
                type_of_item = i.i_type
                # Add item to inventory, before replacing in equipped
                PlayerClass.char.inventory.append(PlayerClass.char.equipped_items[type_of_item])
                PlayerClass.char.equipped_items[type_of_item] = i

                # Adjust player statistics
                PlayerClass.char.hp += i.health
                PlayerClass.char.defence += i.defence

                print(f"\n{i.name} is now equipped")
                PlayerClass.char.inventory.remove(i)
        except AttributeError:
            pass


def unequip():
    # This function acts as the opposite to the equip function.
    item = input("Which item to unequip? Helmet/Chest/Weapon/Shield ")
    if item in PlayerClass.char.equipped_items:
        i = PlayerClass.char.equipped_items[item]

        # Adjust stats for character without item
        PlayerClass.char.hp -= i.health
        PlayerClass.char.defence -= i.defence

        PlayerClass.char.equipped_items[item] = None
        print(f"\n{i.name} is now unequipped")
        PlayerClass.char.inventory.append(i)
    else:
        print("Invalid item.")


# Create normal items
wooden_stick = Item("Wooden Stick", "Weapon", " ", None, 5, 0, 0, 10, "Normal")
wooden_shield = Item("Wooden Shield", "Shield", " ", None, 0, 5, 0, 10, "Normal")
leather_cap = Item("Leather Cap", "Helmet", " ", None, 0, 7, 2, 17, "Normal")
leather_armour = Item("Leather Armour", "Chest", " ", None, 0, 12, 2, 28, "Normal")
iron_sword = Item("Iron Sword", "Weapon", " ", None, 25, 0, 0, 120, "Normal")
iron_armour = Item("Iron Armour", "Chest", " ", None, 0, 27, 0, 62, "Normal")
iron_shield = Item("Iron Shield", "Shield", " ", None, 0, 22, 0, 48, "Normal")
iron_helmet = Item("Iron Helmet", "Helmet", " ", None, 0, 17, 0, 32, "Normal")

# Create rare items
dragon_plate = Item("Dragon Plate", "Chest", " ", None, 2, 55, 15, 260, "Rare")
half_moon_katana = Item("Half Moon Katana", "Weapon", " ", None, 60, 3, 0, 280, "Rare")

# Create unique items
one_hit_wonder = Item("One Hit Wonder", "Weapon", " ", None, 500, 0, 0, 5000, "Unique")

# Item statistics dictionary, hold names, damage, defence and rarity stats for an item
item_stats = {
    "wooden stick": [wooden_stick.name, wooden_stick.damage, wooden_stick.defence, wooden_stick.rarity],
    "wooden shield": [wooden_shield.name, wooden_shield.damage, wooden_shield.defence, wooden_stick.rarity],
    "leather cap": [leather_cap.name, leather_cap.damage, leather_cap.defence, leather_cap.rarity],
    "leather armour": [leather_armour.name, leather_armour.damage, leather_armour.rarity],

    "iron sword": [iron_sword.name, iron_sword.damage, iron_sword.defence, iron_sword.rarity],
    "iron armour": [iron_armour.name, iron_armour.damage, iron_armour.defence, iron_armour.rarity],
    "iron shield": [iron_shield.name, iron_shield.damage, iron_shield.defence, iron_shield.rarity],
    "iron helmet": [iron_helmet.name, iron_helmet.damage, iron_helmet.defence, iron_helmet.rarity],

    "dragon plate": [dragon_plate.name, dragon_plate.damage, dragon_plate.defence, dragon_plate.rarity],
    "half moon katana": [half_moon_katana.name, half_moon_katana.damage, half_moon_katana.defence, half_moon_katana.rarity],

    "one hit wonder": [one_hit_wonder.name, one_hit_wonder.damage, one_hit_wonder.defence, one_hit_wonder.rarity]
}

# Give player an item
