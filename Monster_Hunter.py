
# Monster_Hunter Development Ver 1.5



import sys

# Game imports
import GameBoard
import CombatSystem
import PlayerClass
import MonsterClass
import ItemClass
import NPCClass
from MonsterClass import gen_ran_pos


def startGame():
    GameBoard.draw_board(GameBoard.theBoard)
    gameAction()


def printHelp():
    print("\nAvailable Menu Commands:\n"
          "help         Display help menu\n"
          "start        Start the game\n"
          "exit         Exit the game\n\n"
          "\nAvailable Game Commands:\n"
          "help         Display help menu\n"
          "exit         Exit the game\n"
          "item stats   View stats of an item\n"
          "player stats View player statistics\n"
          "equip        Allows to equip an item\n"
          "unequip      Allows to unequip an item\n"
          "inventory    Check your inventory\n\n"
          "up           Move up\n"
          "down         Move down\n"
          "left         Move left\n"
          "right        Move right\n")


def menuAction():
    """
    Hold a dictionary with available commands in the menu of the game
    """
    menu_action_dict = {
        "help": printHelp, "start": startGame, "exit": sys.exit
    }
    while True:
        menu_action = input("What would you like to do? > ")
        if menu_action in menu_action_dict:
            menu_action_dict[menu_action]()
        else:
            print("Unknown command...")


def gameAction():
    """
    This function holds a game action dictionary, which maps valid user inputs to either other functions
    or converts player movement to equivalent integers. For example: If the player wants to move up the board,
    it has to add 10 to the current position of the player, if the player wants to move left it has to minus 1
    from the current position.
    """
    game_action_dict = {
        "help": printHelp, "exit": sys.exit, "inventory": PlayerClass.char.show_inventory,
        "item stats": ItemClass.showStats,
        "equip": ItemClass.equip, "unequip": ItemClass.unequip, "player stats": PlayerClass.char.showStats,
        "up": 10, "down": -10, "left": -1, "right": 1
    }
    valid_move = False
    while not valid_move:
        game_action = input("\n> ")
        if game_action in game_action_dict:
            # Try calling a function, if the action is not a function, catch the exception and pass it to makeMove()
            try:
                game_action_dict[game_action]()
            except TypeError:
                makeMove(game_action_dict[game_action])
                valid_move = True
        else:
            print("Unknown command...")


def makeMove(move):
    """
    This function defines movement on the board. When a player makes a move, it first moves the player to the new
    position, because now there are two instances of the player on board, it erases the previous position with
    an empty string -> ' '.

    Once the movements are complete, it updates the player object.player_position with the new pos. It then draws the
    board and loops back to take the gameAction() function to take the player input again.
    """
    try:
        # Place the player in a new position
        GameBoard.theBoard[PlayerClass.char.position + move] = PlayerClass.char.name
        # Reset the current position to empty
        GameBoard.theBoard[PlayerClass.char.position] = " "
        # Update player position to the new position
        PlayerClass.char.position = PlayerClass.char.position + move
    except IndexError:
        print("Out of bounds.")

    checkEncounters()
    GameBoard.draw_board(GameBoard.theBoard)
    gameAction()


def checkEncounters():
    # This function checks for any encounters on the board between the player/monster/item.

    if PlayerClass.char.position == NPCClass.the_trader.position:
        print("--------------------------------------")
        print("\nYou found an NPC! The Mystical Trader.\n")
        NPCClass.the_trader.hidden = NPCClass.the_trader.symbol
        NPCClass.the_trader.found = True
        NPCClass.tradeItem()

    if NPCClass.the_trader.found:
        GameBoard.theBoard[NPCClass.the_trader.position] = NPCClass.the_trader.symbol

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


def main():
    # Place player on position 0
    GameBoard.theBoard[PlayerClass.char.position] = PlayerClass.char.name

    # Place orcs in random positions
    for orc in MonsterClass.army_of_orcs:
        GameBoard.theBoard[orc.position] = orc.hidden

    # Boss
    GameBoard.theBoard[99] = MonsterClass.orc_boss.symbol

    # Place NPC
    GameBoard.theBoard[NPCClass.the_trader.position] = NPCClass.the_trader.hidden

    if NPCClass.the_trader.position == GameBoard.theBoard[orc.position]:
        NPCClass.the_trader.position = gen_ran_pos()

    GameBoard.theBoard[NPCClass.the_healer.position] = NPCClass.the_healer.hidden
    if NPCClass.the_healer.position == GameBoard.theBoard[orc.position]:
        NPCClass.the_healer.position = gen_ran_pos()


    # Give player a wooden stick and a wooden shield
    PlayerClass.char.equipped_items["Weapon"] = ItemClass.wooden_stick
    PlayerClass.char.inventory.append(ItemClass.wooden_shield)

    # Place some normal items around the board
    GameBoard.theBoard[ItemClass.leather_armour.position] = ItemClass.leather_armour.hidden

    GameBoard.theBoard[ItemClass.leather_cap.position] = ItemClass.leather_cap.hidden

    print("\nWelcome to Monster_Hunter.\n\n"
          "Kill monsters, gather gold, buy better\n"
          "equipment and battle with the boss.\n\n"
          "Available Commands:\n\n"
          "help     Display help menu\n"
          "start    Start the game\n"
          "exit     Exit the game\n")
    menuAction()


if __name__ == '__main__':
    main()
