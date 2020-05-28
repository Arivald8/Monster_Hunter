import random
import Monster_Hunter
import PlayerClass
import time
import sys
import GameBoard

def dice_roll():
    # Simple dice roll function
    dice_number = random.randrange(1, 11)
    return dice_number


def attack():
    """
    This function defines the strength of the player hit. It does so by multiplying player strength by the attack
    statistic of the currently equipped weapon. It then multiplies that by the dice_dict value of the player_roll.
    """
    dice_dict = {1: 0.1, 2: 0.2, 3: 0.3, 4: 0.4, 5: 0.5, 6: 0.6, 7: 0.7, 8: 0.8, 9: 0.9, 10: 1}

    player_roll = dice_roll()
    print(f"You rolled {player_roll} \n")
    # time.sleep(2)

    # Hit damage calculation
    player_hit = PlayerClass.char.strength * PlayerClass.char.equipped_items["Weapon"].damage * dice_dict[player_roll]
    return player_hit


def deal_dmg(some_monster, player_hit):
    # The purpose of this function is to apply defensive bonus, deal damage to some_monster and to print the result.
    reduced_hit = player_hit - some_monster.defence
    if reduced_hit <= 0:
        reduced_hit = 0
    some_monster.hp -= reduced_hit
    print("-------------------------------------------------")
    print(f"You hit {some_monster.name} for {round(reduced_hit, 2)} damage... {some_monster.name}"
          f" has {round(some_monster.hp, 2)}hp remaining")
    print("-------------------------------------------------")
    # time.sleep(4)


def monster_attack(monster):
    # This function is the same as the attack(), but it is used to perform attacks by monsters.
    dice_dict = {1: 0.1, 2: 0.2, 3: 0.3, 4: 0.4, 5: 0.5, 6: 0.6, 7: 0.7, 8: 0.8, 9: 0.9, 10: 1}

    monster_roll = dice_roll()
    print(f"\nThe monster rolled {monster_roll} \n")
    # time.sleep(2)

    monster_hit = monster.attack * dice_dict[monster_roll]
    reduced_hit = monster_hit - PlayerClass.char.defence
    if reduced_hit <= 0:
        reduced_hit = 0

    PlayerClass.char.hp -= reduced_hit
    print("-------------------------------------------------")
    print(f"You get hit for {round(reduced_hit, 2)} damage... You have {round(PlayerClass.char.hp, 2)}hp remaining")
    print("-------------------------------------------------")
    # time.sleep(4)


def battle(monster):
    """
    This function is the core of the combat system. Whenever a fight is to occur, this function gets called.
    As long as the monster or the player are above 0hp, it will keep asking the player to roll the dice or to flee.
    """
    fight = True
    while fight:
        while monster.hp > 0:
            if PlayerClass.char.hp <= 0:
                print("You're dead, game over.")
                sys.exit()
            else:

                action = input("\nroll/flee? > ")
                if action == "roll":
                    print("\nIt's your turn to roll the dice... \n")
                    # time.sleep(2)
                    player_hit = attack()
                    deal_dmg(monster, player_hit)
                    monster_attack(monster)

                elif action == "flee":
                    GameBoard.draw_board(GameBoard.theBoard)
                    print("You run away like a coward!")
                    fight = False
                    Monster_Hunter.gameAction()

                elif action == "exit":
                    sys.exit()

                else:
                    print("Unknown command...")

        monster.defeated = True
        print("Monster defeated.")
        PlayerClass.char.gold += monster.gold_loot
        PlayerClass.char.xp += monster.xp
        print(f"You pick up {monster.gold_loot} gold")
        PlayerClass.char.levelUp()
        fight = False
