import PlayerClass
import MonsterClass
import NPCClass
import ItemClass
import GameBoard
import pickle
import CombatSystem


def checkEncounters():
    # This function checks for any encounters on the board between the player/monster/item.

    if PlayerClass.char.position == NPCClass.the_trader.position:
        print("--------------------------------------")
        print("\nYou found an NPC! The Mystical Trader.\n")
        NPCClass.the_trader.found = True
        NPCClass.tradeItem()

    if NPCClass.the_trader.found:
        GameBoard.theBoard[NPCClass.the_trader.position] = NPCClass.the_trader.symbol
    elif not NPCClass.the_trader.found:
        GameBoard.theBoard[NPCClass.the_trader.position] = NPCClass.the_trader.hidden

    if PlayerClass.char.position == NPCClass.the_healer.position:
        print("--------------------------------------")
        print("\nYou found an NPC! The Healer.\n")
        NPCClass.the_healer.hidden = NPCClass.the_healer.symbol
        NPCClass.the_healer.found = True
        NPCClass.healing()

    if NPCClass.the_healer.found:
        GameBoard.theBoard[NPCClass.the_healer.position] = NPCClass.the_healer.symbol

    # All items that are on the board are in the on_board_items list. If player pos == item pos -> find item.
    for i in ItemClass.on_board_items:
        if not i.found:
            if PlayerClass.char.position == i.position:
                i.found = True
                print("You found something!")
                PlayerClass.char.add_item(i)
                print(f"{i.name} was added to your inventory")
        else:
            pass

    # For every orc in the army, if the orc pos is same as player pos, but not defeated, discover the monster
    for orc in MonsterClass.army_of_orcs:
        if orc.defeated:
            pass
        else:
            if orc.position == PlayerClass.char.position:
                print("\nYou found the monster!")
                print(f"The {orc.name}")
                orc.found = True

                fight_flee = input("\nDo you want to fight? [y/n] > ")
                if fight_flee == "y":
                    GameBoard.theBoard[orc.position] = orc.symbol
                    CombatSystem.battle(orc)

                elif fight_flee == "n":
                    pass
                else:
                    print("You stutter something as you run away in fear...")
    # If an orc is found, leave a symbol on the board
    for orc in MonsterClass.army_of_orcs:
        if orc.found:
            GameBoard.theBoard[orc.position] = orc.symbol
        if orc.defeated:
            if PlayerClass.char.position == orc.position:
                GameBoard.theBoard[orc.position] = PlayerClass.char.name
            else:
                GameBoard.theBoard[orc.position] = " "

    if MonsterClass.orc_boss.defeated:
        print("You killed the boss, you win!")
        sys.exit()
    else:
        if MonsterClass.orc_boss.position == PlayerClass.char.position:
            print("\nYou found the Destroyer Orc!")
            print("Be careful, he's not like the other Orcs!")
            MonsterClass.orc_boss.found = True

            boss_fight = input("\nDo you want to fight the boss? [y/n] > ")
            if boss_fight == "y":
                GameBoard.theBoard[MonsterClass.orc_boss.position] = MonsterClass.orc_boss.symbol
                CombatSystem.battle(MonsterClass.orc_boss)

            elif boss_fight == "n":
                pass
            else:
                print("You stutter something as you run away in fear...")
    if MonsterClass.orc_boss.found:
        GameBoard.theBoard[MonsterClass.orc_boss.position] = MonsterClass.orc_boss.symbol


def makeSave():
    inventory_list = []
    for obj in PlayerClass.char.inventory:
        inventory_list.append(obj)

    save_dict = {
        # --- Player --- #
        "player_pos": PlayerClass.char.position,
        "player_inventory": inventory_list,
        "player_eq": PlayerClass.char.equipped_items,
        "player_hp": PlayerClass.char.hp,
        "player_gold": PlayerClass.char.gold,
        "player_xp": PlayerClass.char.xp,
        "player_lvl": PlayerClass.char.level,
        "player_def": PlayerClass.char.defence,
        "player_str": PlayerClass.char.strength,
        # --- NPC --- #
        "trader_pos": NPCClass.the_trader.position,
        "trader_found": NPCClass.the_trader.found,
        "healer_pos": NPCClass.the_healer.position,
        "healer_found": NPCClass.the_healer.found,
        # --- Monsters --- #
        "monster1": MonsterClass.army_of_orcs[0],
        "monster2": MonsterClass.army_of_orcs[1],
        "monster3": MonsterClass.army_of_orcs[2],
        "monster4": MonsterClass.army_of_orcs[3],
        "monster5": MonsterClass.army_of_orcs[4],
        "monster6": MonsterClass.army_of_orcs[5],
        "monster7": MonsterClass.army_of_orcs[6],
        "monster8": MonsterClass.army_of_orcs[7],
        "monster9": MonsterClass.army_of_orcs[8],
    }

    pickle.dump(save_dict, open("save.p", "wb"))


def loadSave():
    load_dict = pickle.load(open("save.p", "rb"))

    # --- Player --- #
    # First reset old position to -> " "
    GameBoard.theBoard[PlayerClass.char.position] = " "
    # Now the position is updated
    PlayerClass.char.position = load_dict['player_pos']
    # Now place the player
    GameBoard.theBoard[PlayerClass.char.position] = PlayerClass.char.name

    PlayerClass.char.inventory = load_dict['player_inventory']
    PlayerClass.char.equipped_items = load_dict['player_eq']
    PlayerClass.char.hp = load_dict['player_hp']
    PlayerClass.char.gold = load_dict['player_gold']
    PlayerClass.char.xp = load_dict['player_xp']
    PlayerClass.char.lvl = load_dict['player_lvl']
    PlayerClass.char.defence = load_dict['player_def']
    PlayerClass.char.strength = load_dict['player_str']

    # --- NPC --- #
    # Set Found
    NPCClass.the_trader.found = load_dict['trader_found']
    # Now the position is updated
    NPCClass.the_trader.position = load_dict['trader_pos']

    NPCClass.the_healer.found = load_dict['healer_found']
    NPCClass.the_healer.position = load_dict['healer_pos']

    # --- Monsters --- #
    MonsterClass.army_of_orcs = []

    # Separate all monsters
    monster1 = load_dict['monster1']
    monster2 = load_dict['monster2']
    monster3 = load_dict['monster3']
    monster4 = load_dict['monster4']
    monster5 = load_dict['monster5']
    monster6 = load_dict['monster6']
    monster7 = load_dict['monster7']
    monster8 = load_dict['monster8']
    monster9 = load_dict['monster9']

    new_monster1 = MonsterClass.Monster("Bald Orc", "m", monster1.position, " ", monster1.found, monster1.hp, 32, 2,
                                        monster1.defeated, MonsterClass.gen_orc_gold(), 49)
    new_monster2 = MonsterClass.Monster("Bald Orc", "m", monster2.position, " ", monster2.found, monster2.hp, 32, 2,
                                        monster1.defeated, MonsterClass.gen_orc_gold(), 49)
    new_monster3 = MonsterClass.Monster("Bald Orc", "m", monster3.position, " ", monster3.found, monster3.hp, 32, 2,
                                        monster1.defeated, MonsterClass.gen_orc_gold(), 49)
    new_monster4 = MonsterClass.Monster("Bald Orc", "m", monster4.position, " ", monster4.found, monster4.hp, 32, 2,
                                        monster1.defeated, MonsterClass.gen_orc_gold(), 49)
    new_monster5 = MonsterClass.Monster("Bald Orc", "m", monster5.position, " ", monster5.found, monster5.hp, 32, 2,
                                        monster1.defeated, MonsterClass.gen_orc_gold(), 49)
    new_monster6 = MonsterClass.Monster("Bald Orc", "m", monster6.position, " ", monster6.found, monster6.hp, 32, 2,
                                        monster1.defeated, MonsterClass.gen_orc_gold(), 49)
    new_monster7 = MonsterClass.Monster("Bald Orc", "m", monster7.position, " ", monster7.found, monster7.hp, 32, 2,
                                        monster1.defeated, MonsterClass.gen_orc_gold(), 49)
    new_monster8 = MonsterClass.Monster("Bald Orc", "m", monster8.position, " ", monster8.found, monster8.hp, 32, 2,
                                        monster1.defeated, MonsterClass.gen_orc_gold(), 49)
    new_monster9 = MonsterClass.Monster("Bald Orc", "m", monster9.position, " ", monster9.found, monster9.hp, 32, 2,
                                        monster1.defeated, MonsterClass.gen_orc_gold(), 49)

    MonsterClass.army_of_orcs.append(new_monster1)
    MonsterClass.army_of_orcs.append(new_monster2)
    MonsterClass.army_of_orcs.append(new_monster3)
    MonsterClass.army_of_orcs.append(new_monster4)
    MonsterClass.army_of_orcs.append(new_monster5)
    MonsterClass.army_of_orcs.append(new_monster6)
    MonsterClass.army_of_orcs.append(new_monster7)
    MonsterClass.army_of_orcs.append(new_monster8)
    MonsterClass.army_of_orcs.append(new_monster9)

    # Place saved monsters on the board
    for monster in MonsterClass.army_of_orcs:
        if monster.found:
            GameBoard.theBoard[monster.position] = monster.symbol
        else:
            GameBoard.theBoard[monster.position] = monster.hidden

    checkEncounters()

    # Finally draw the board
    GameBoard.draw_board(GameBoard.theBoard)
