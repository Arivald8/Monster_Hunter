import sys
import ItemClass
import PlayerClass as PC
from MonsterClass import gen_ran_pos


class Npc:
    def __init__(self, name, symbol, npc_type, position, hidden, found):
        self.name = name
        self.symbol = symbol
        self.npc_type = npc_type
        self.position = position
        self.hidden = hidden
        self.found = found

        self.inventory = []

        self.gold = 0


def tradeItem():
    sell_buy = input("Would you like to [sell] or [buy]? else just [leave]! > ").lower()

    if sell_buy == "exit":
        sys.exit()

    elif sell_buy == "buy":
        print("\nExcellent! Here's what I have:\n")

        items, spells = [], []
        for obj in the_trader.inventory:
            try:
                if obj.rarity in ["Normal", "Rare", "Unique"]:
                    items.append(obj)
            except AttributeError:
                spells.append(obj)

        for item in sorted(items, key=lambda obj: obj.rarity):
            print(f"{item.name}:")
            print("-------------")
            print(f"Damage: {item.damage} \n"
                  f"Defence: {item.defence} \n"
                  f"HP: {item.health} \n"
                  f"Rarity: {item.rarity} \n"
                  f"Price: {item.value}\n")
        for spell in spells:
            print(f"{spell.name}:")
            print("-------------")
            print(f"INT Required: {spell.int_req} \n"
                  f"Desc: {spell.description} \n"
                  f"Price: {spell.value}\n")
        print(f'Player Gold: {round(PC.char.gold), 2}')

        buy_item = input("Which item would you like to buy? > ").lower()
        for i, item in enumerate(the_trader.inventory):
            if item.name.lower() == buy_item:
                if round(PC.char.gold, 2) >= item.value:
                    PC.char.gold -= item.value
                    PC.char.inventory.append(item)
                    print("\nItem added to your inventory.")
                else:
                    print("\nYou don't have enough gold for that item.")
                break
            elif i == len(the_trader.inventory) - 1:
                print("\nI don't know what you're saying")

    elif sell_buy == "sell":
        if len(PC.char.inventory) == 0:
            print("You don't have any items in your inventory")
        else:
            print(f'Inventory: {PC.char.inventory}')
            sell_item = input("\nWhat is it that you would like to sell? > ").lower()
            for index, obj in enumerate(PC.char.inventory, start=1):
                try:
                    if obj.name.lower() == sell_item:
                        the_trader.inventory.append(obj)
                        PC.char.inventory.remove(obj)
                        PC.char.gold += obj.value
                        print("Pleasure to do business with you.")
                        print(f"{obj.value} gold added to your sack")
                        break
                except AttributeError:
                    pass
                if index == len(PC.char.inventory):
                    print("\nYou don't have that item in your backpack.")


def healing():
    heal = input("Welcome to my shack, I can heal you for a small price if you want. [y/n] > ")
    if heal == "y":
        if PC.char.hp >= 100:
            print("You're in a great shape, I can't heal you.")
        else:
            bonus_hp = 0
            for i in PC.char.equipped_items:
                try:
                    item = PC.char.equipped_items[i]
                    bonus_hp += item.health
                except AttributeError:
                    bonus_hp += 0
            healing_need = (100 - PC.char.hp) + bonus_hp
            healing_cost = healing_need / 5
            rounded_cost = round(healing_cost, 2)
            get_healed = input(f"It will cost you {rounded_cost} gold. Deal? [y/n] > ")
            if get_healed == "y":
                if PC.char.gold >= rounded_cost:
                    PC.char.gold -= rounded_cost
                    PC.char.hp += healing_need
                    print("All of your wounds magically disappear...")
                else:
                    print("You don't have enough gold for that.")
            else:
                print("Stop wasting my time!")
    else:
        print("Stop wasting my time!")


def sellSpell():
    buy_spell = input('"Do not meddle in the affairs of Wizards, for they are subtle and quick to anger"\n'
                      'So... Wanna buy some spells? [y/n] > ')
    if buy_spell == "exit":
        sys.exit()

    elif buy_spell == "y":
        print("----------------")
        print("Wizard Inventory")
        for spell in the_wizard.inventory:
            print(f"Spell:       {spell.name}\n"
                  f"Description: {spell.description}\n"
                  f"Price:       {spell.value}")
        print("----------------")

        buy_item = input("Which spell would you like to buy? > ")
        for i in the_wizard.inventory:
            if i.name == buy_item:
                if PC.char.gold >= i.value:
                    PC.char.gold -= i.value
                    PC.char.inventory.append(i)
                    print("\nItem added to your inventory.")
                else:
                    print("\nYou don't have enough gold for that item.")

            elif i.name != buy_item:
                pass
            else:
                print("\nI don't know what you're saying")

    else:
        print("What a waste of time...")


def upgradeItem():
    print("Welcome to my blacksmith shop traveller. We can upgrade most items!"
          " For a cost of course..(Lvl 1 upgrades are free)")
    print("")
    print(f"Your gold: {PC.char.gold}")
    print("")
    print("Items in Inventory")
    print("---------------------")
    print(PC.char.inventory)

    upgrading = True

    while upgrading:
        item_choice = input("Which item would you like to upgrade? > ").lower()
        if item_choice in ["exit", '']:
            break
        for obj in PC.char.inventory:  # Looping through player inventory and inserting into a new table
            try:
                if item_choice == obj.name.lower():
                    if obj.level >= 10:  # If the item is already at max return
                        print("Your item is already maxed out!")
                    else:
                        print(f"{obj.name} Lvl: +{obj.level}")  # Displaying the item
                        proceed = input("It will cost you 100 gold, proceed? [y/n] > ")
                        if proceed == 'y':
                            if PC.char.gold < 100: # Checking if they have enough gold
                                print("You don't have enough gold!")
                            else:
                                obj.level += 1
                                PC.char.gold -= 100
                                if obj.i_type == "Weapon":
                                    obj.damage += 5
                                else:
                                    obj.defence += 5
                                print(f"Here is your upgraded item! {obj.name} +{obj.level}")
                                again = input("Upgrade again? [y/n] > ")
                                if again == 'y':
                                    pass
                                elif again == 'n':
                                    upgrading = False
                        else:
                            print("Come again!")
                            upgrading = False
            except AttributeError:
                pass


# Create an NPC
the_trader = Npc("The Mystical Trader", "T", "Trader", gen_ran_pos(), " ", False)
the_trader.gold = 1000
the_healer = Npc("The Healer", 'H', "Healer", gen_ran_pos(), " ", False)

the_wizard = Npc("The Wizard", "W", "Wizard", gen_ran_pos(), " ", False)

the_blacksmith = Npc("The Blacksmith", "S", "Blacksmith", 1, " ", False)

# Give items to an NPC
# Normal - leather_cap, leather_armour, iron_helmet, iron_shield, iron_armour, iron_sword
# Rare - dragon_plate, half_moon_katana
# Unique - one_hit_wonder
the_trader.inventory = ItemClass.Item.trader_items

# Wizard/Spells
the_wizard.inventory.append(ItemClass.fire_ball)

# Dictionary holding NPC functions
npc_func_dict = {
    the_trader: tradeItem,
    the_healer: healing,
    the_wizard: sellSpell,
    the_blacksmith: upgradeItem,
}

