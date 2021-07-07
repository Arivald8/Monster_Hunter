import random
import Monster_Hunter
import PlayerClass
import time
import sys
import GameBoard
import ItemClass


def dice_roll(level=None):
    if level is None:  # Player - D10 roll
        return random.randrange(1, 11)
    elif level == 'monster':  # Monster - D8 roll
        return random.randrange(1, 9)
    else:  # Monster Special - L1: no roll, L2: D8 roll, L3: D10 roll
        level_dict = {1: 0,
                      2: random.randrange(1, 9),
                      3: random.randrange(1, 11)}
        return level_dict[level]


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
    # <torbray> Monster DEF can be 2, 3, 4 or (boss) 8. Orc DEF is a reduction modifier
    reduced_hit = player_hit / some_monster.defence

    some_monster.hp -= reduced_hit
    print("-------------------------------------------------")
    print(f"You hit {some_monster.name} for {round(reduced_hit, 2)} damage... {some_monster.name}"
          f" has {max(round(some_monster.hp, 2), 0)}hp remaining")
    print("-------------------------------------------------")
    # time.sleep(4)


def castSpell(a_spell, monster):
    if a_spell in ItemClass.spell_dict:
        ItemClass.spell_dict[a_spell](monster)


def monster_attack(monster, level, defence):
    # This function is the same as the attack(), but it is used to perform attacks by monsters.
    def g(self):
        return self / 10

    monster_roll = dice_roll('monster')
    monster_special_roll = dice_roll(level)
    print(f"\nThe monster rolls a D8 die: {monster_roll}")
    # time.sleep(2)
    if monster_roll > 6 and monster_special_roll > 6:
        print("The monster was able to use his special move!")
        ''' <torbray> MONSTER_HIT CALCULATIONS
          - (level + g(level)):                       Modifier: Level 1 = 1.1, Level 2 = 1.2, Level 3 = 1.3
          - monster.attack:                           20 - 29
          - g(monster_roll):                          monster_roll / 10
          - (optional) g(monster_special_roll) / 5:   (monster_special_roll / 10) / 5
        '''
        monster_hit = (level + g(level)) * monster.attack * (g(monster_roll) + g(monster_special_roll) / 5)
    else:
        monster_hit = (level + g(level)) * monster.attack * g(monster_roll)
    ''' <torbray> REDUCED_HIT CALCULATIONS
      - monster_hit:    (as above)
      - defence * 0.7:  Player Defence * 0.7 modifier
      if REDUCED_HIT < 0, value is 0
    '''
    reduced_hit = max(monster_hit - defence * 0.7, 0)

    # --- Decide whether it's a hit or miss (Dexterity) --- ###
    chance_to_avoid = (PlayerClass.char.dexterity / g(monster_roll)) / 3
    x = random.randint(0, 100)

    # <torbray> print(f'#TESTING - NOR: {monster_roll} SPE: {monster_special_roll} HIT: {monster_hit}, RED_HIT {reduced_hit} #')
    if x < chance_to_avoid:
        print("\n-------------------------------------------------")
        print("You were able to avoid the attack!")
        print("-------------------------------------------------")
        return

    PlayerClass.char.hp -= reduced_hit
    print("\n-------------------------------------------------")
    print(f"You get hit for {round(reduced_hit, 2)} damage... You have {max(round(PlayerClass.char.hp, 2), 0)}hp remaining")
    print("-------------------------------------------------")
    # time.sleep(4)


def battle(monster, monster_level):
    """
    This function is the core of the combat system. Whenever a fight is to occur, this function gets called.
    As long as the monster or the player are above 0hp, it will keep asking the player to roll the dice or to flee.
    """
    fight = True
    while fight:
        # <torbray> PLAYER DEFENCE - Adds Player DEF to Shield, Helmet and Chest DEF
        player_def = PlayerClass.char.defence
        for armour in ['Shield', 'Helmet', 'Chest']:
            arm_def = PlayerClass.char.equipped_items[armour]
            if arm_def is not None:
                player_def += arm_def.defence

        while monster.hp > 0:
            # <torbray> print(f'#TESTING - ATK: {monster.attack}, HP: {monster.hp} #')

            if PlayerClass.char.hp <= 0:
                print("You're dead, game over.")
                sys.exit()
            else:
                action = input("\nDo you want to [roll], use a [spell] or [flee]? > ")
                if action == "roll":
                    print("\nYou roll a D10 die... \n")
                    # time.sleep(2)
                    player_hit = attack()
                    deal_dmg(monster, player_hit)

                elif action == 'spell':
                    spells = [obj for obj in PlayerClass.char.inventory if isinstance(obj, ItemClass.Spell)]
                    if len(spells) == 0:
                        print("You don't have any spells to cast!")
                    else:
                        print(f"\n---Spell Menu---\n{PlayerClass.char.player} has {PlayerClass.char.intelligence} INT\n")
                        for spell in spells:
                            print(f' - {spell} (requires {spell.int_req} INT)')
                        while 1:
                            cast_spell = input("\nWhich spell to cast? (type 'exit' to exit)\n>> ").lower()
                            if cast_spell == 'exit':
                                break
                            else:
                                cast_attempt = False
                                for spell in spells:
                                    if cast_spell == spell.name.lower():
                                        if PlayerClass.char.intelligence < spell.int_req:
                                            print("You don't have enough intelligence to cast this spell")
                                        else:
                                            castSpell(cast_spell, monster)
                                        cast_attempt = True
                                        break
                            if not cast_attempt:
                                print('Invalid input, try again.')
                            else:
                                break

                elif action == "flee":
                    print("You run away like a coward!")
                    return

                elif action == "exit":
                    sys.exit()

                else:
                    print("Unknown command...")
            if monster.hp > 0:
                monster_attack(monster, level=monster_level, defence=player_def)

        monster.defeated = True
        print("Monster defeated.")
        PlayerClass.char.gold += monster.gold_loot
        PlayerClass.char.xp += monster.xp
        print(f"You pick up {monster.gold_loot} gold")
        print(f'You gained {monster.xp} experience')
        PlayerClass.char.levelUp()
        fight = False
