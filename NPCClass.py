import sys
import ItemClass
import PlayerClass
from MonsterClass import gen_ran_pos
import GameBoard


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
    sell_buy = input("Would you like to [sell] or [buy]? else just [leave]! > ")

    if sell_buy == "exit":
        sys.exit()
    elif sell_buy == "leave":
        pass

    elif sell_buy == "buy":
        print("\nExcellent! Here's what I have:\n")
        for attr in sorted(the_trader.inventory, key=lambda obj: obj.rarity):
            if attr.rarity == "Normal":
                print(f"{attr.name}:")
                print("-------------")
                print(f"Damage: {attr.damage} \n"
                      f"Defence: {attr.defence} \n"
                      f"HP: {attr.health} \n"
                      f"Rarity: {attr.rarity} \n"
                      f"Price: {attr.value}\n")

            elif attr.rarity == "Rare":
                print(f"{attr.name}:")
                print("-------------")
                print(f"Damage: {attr.damage} \n"
                      f"Defence: {attr.defence} \n"
                      f"HP: {attr.health} \n"
                      f"Rarity: {attr.rarity} \n"
                      f"Price: {attr.value}\n")

            if attr.rarity == "Unique":
                print(f"{attr.name}:")
                print("-------------")
                print(f"Damage: {attr.damage} \n"
                      f"Defence: {attr.defence} \n"
                      f"HP: {attr.health} \n"
                      f"Rarity: {attr.rarity} \n"
                      f"Price: {attr.value}\n")

        buy_item = input("Which item would you like to buy? > ")
        for i in the_trader.inventory:
            if i.name == buy_item:
                if PlayerClass.char.gold >= i.value:
                    PlayerClass.char.gold -= i.value
                    PlayerClass.char.inventory.append(i)
                    print("\nItem added to your inventory.")
                else:
                    print("\nYou don't have enough gold for that item.")

            elif i.name != buy_item:
                pass
            else:
                print("\nI don't know what you're saying")

    elif sell_buy == "sell":
        sell_item = input("\nWhat is it that you would like to sell? > ")
        for i in PlayerClass.char.inventory:
            try:
                if i.name == sell_item:
                    the_trader.inventory.append(i)
                    PlayerClass.char.inventory.remove(i)
                    PlayerClass.char.gold += i.value
                    print("Pleasure to do business with you.")
                    print(f"{i.value} gold added to your sack")
                elif i.name != sell_item:
                    print("\nYou don't have that item in your backpack.")
                else:
                    print("\nI don't understand.")
            except AttributeError:

                pass


def healing():
    heal = input("Welcome to my shack, I can heal you for a small price if you want. [y/n] > ")
    if heal == "y":
        if PlayerClass.char.hp >= 100:
            print("You're in a great shape, I can't heal you.")
        else:
            bonus_hp = 0
            for i in PlayerClass.char.equipped_items:
                try:
                    item = PlayerClass.char.equipped_items[i]
                    bonus_hp += item.health
                except AttributeError:
                    bonus_hp += 0
            healing_need = (100 - PlayerClass.char.hp) + bonus_hp

            healing_cost = healing_need / 5
            rounded_cost = round(healing_cost, 2)
            get_healed = input(f"It will cost you {rounded_cost} gold. Deal? [y/n] > ")
            if get_healed == "y":
                if PlayerClass.char.gold >= rounded_cost:
                    PlayerClass.char.gold -= rounded_cost
                    PlayerClass.char.hp += healing_need
                    print("All of your wounds magically disappear...")
                else:
                    print("You don't have enough gold for that.")
            else:
                print("Stop wasting my time!")
    else:
        print("Stop wasting my time!")


# Create an NPC
the_trader = Npc("Mystic Trader", "T", "Trader", gen_ran_pos(), " ", False)
the_trader.gold = 1000

the_healer = Npc("The Healer", "H", "Healer", gen_ran_pos(), " ", False)

# Give items to an NPC
the_trader.inventory.append(ItemClass.leather_cap)
the_trader.inventory.append(ItemClass.leather_armour)
the_trader.inventory.append(ItemClass.iron_helmet)
the_trader.inventory.append(ItemClass.iron_shield)
the_trader.inventory.append(ItemClass.iron_armour)
the_trader.inventory.append(ItemClass.iron_sword)

the_trader.inventory.append(ItemClass.dragon_plate)
the_trader.inventory.append(ItemClass.half_moon_katana)

the_trader.inventory.append(ItemClass.one_hit_wonder)

