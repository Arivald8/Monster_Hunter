# Monster_Hunter - Development branch (v1.5)
To start the game **_you will need all the .py files the same directory._** Then simply open your favourite command terminal and navigate to the directory of the Monster_Hunter.py. Once in the correct directory use:

    python Monster_Hunnter.py
          
# Development Start
The player starts with a basic weapon already equipped.

For testing purposes time.sleep() has been commented out to speed up the process.

# The Game

The player can move around the board in the search of monsters. Initially the monsters are invisble to the player, but once a monster is found, it will stay visible until killed.

If the player encounters a monster it can choose to fight or flee. If the player picks to fight, a choice between roll or flee appears. Flee is self explanatory, fight on the other hand starts the battle where the player and monster take turns in rolling the dice. Each time a dice is rolled, damage is calculated, dealt to the opposing party and the player is informed of how much hp the monster has left as well as how much hp the player has left. After each roll the player can flee or keep rolling until the monster or the player dies.

There are items available in the game, Helmet, Armour, Shield and Weapon. Each item has unique statistics for Damage and Defence. Damage and Defence statistics are considered when dealing hits to enemies, the better the statistics of an item, the higher the hit damage. 

The game starts with a menu:

    Welcome to Monster_Hunter.

    Kill monsters, gather gold, upgrade your
    equipment and battle with the bosses.

    Available Commands:

    help     Display help menu
    start    Start the game
    exit     Exit the game

    What would you like to do? >
    
The help command displays available menu and game commands:
 
    Available Menu Commands:
    help         Display help menu
    start        Start the game
    exit         Exit the game


    Available Game Commands:
    help         Display help menu
    exit         Exit the game
    stats        View stats of an item
    equip        Allows to equip an item
    unequip      Allows to unequip an item
    inventory    Check your inventory

    up           Move up
    down         Move down
    left         Move left
    right        Move right

The board is a 10x10 grid with cells.

P - Player
m - Monster

    ----------------------------------------
    ----------------------------------------
    ----------------------------------------
       |   |   |   |   |   |   |   |   |   |
    ----------------------------------------
       |   |   |   |   |   |   |   |   |   |
    ----------------------------------------
       |   |   |   |   |   |   |   |   |   |
    ----------------------------------------
       |   |   |   |   |   |   |   |   |   |
    ----------------------------------------
       |   |   |   |   |   |   |   |   |   |
    ----------------------------------------
       |   |   |   |   |   |   |   |   |   |
    ----------------------------------------
       |   |   |   |   |   |   |   |   |   |
    ----------------------------------------
       |   |   |   |   |   |   |   |   |   |
    ----------------------------------------
       |   | m |   |   |   |   |   |   |   |
    ----------------------------------------
     P |   |   |   |   |   |   |   |   |   |
    ----------------------------------------
    ----------------------------------------
    ----------------------------------------
    

This is the inventory display. "Small Leather Bag" holds unequipped items

    ---------------------
    
    --Small Leather Bag--
    
    ---------------------
    
    [Wooden Shield]
    
    ---------------------
    
    ------Equipped-------
    
    ---------------------
    
           Helmet

           None
    ---------------------
           Armour

           None
    ---------------------
           Weapon

           Wooden Stick
    ---------------------
           Shield

           None
    ---------------------
    Gold: 0

The combat system looks like so

    You found the monster!

    Do you want to fight? [y/n] > y

    roll/flee? > roll

    It's your turn to roll the dice...

    You rolled 8

    -------------------------------------------------
    You hit m for 10.0 damage... m has 90.0hp remaining
    -------------------------------------------------

    The monster rolled 10

    -------------------------------------------------
    You get hit for 10 damage... You have 90hp remaining
    -------------------------------------------------

    roll/flee? >

The player statistics

    -----------------------
    --Character Statistic--
    -----------------------
    Your base Health: 90
    Your base Attack: 3
    Your base Defence: 1
    -----------------------
    Your Total Health: 90
    Your Total Strength: 8
    Your Total Defence: 1
    -----------------------

# TBC
