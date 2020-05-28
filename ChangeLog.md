# Monster_Hunter Change Log

**Monster_Hunter Dev Change v1.0** 

* Added gold to the game
* Added gold to inventory display
* Changed inventory display
* Player class is now stored as a separate file
* Monster class is now stored as a separate file
* Item class is now stored as a separate file

**Monster_Hunter Dev Change v1.1**

* Game board is now stored as a separate file
* Main file code cleanup
* Player is now able to view item stats given that they are either in the inventory, or equipped

**Monster_Hunter Dev Change v1.2**

* Player is now able to equip/unequip items in the inventory
* Commands "equip", "unequip" added to the available game commands
* Bug fixes
* Changed Combat System diplay to allow more clarity

**Monster_Hunter Dev Change v1.3**

* Added "player stats" as a game command
* Player is now able to check player statistics. Total statistic displays stats including equipped item bonuses. 
* A Mystical Trader NCP added
* Player can now buy or sell items.
* Monsters will now drop a random amount of gold once defeated.

**Monster_Hunter Dev Change v1.4**

* Fixed player stats bug, where bonuses were not taken into account while in combat.
* Added HP bonus to items. Items with the hp bonus, will now increase Players overall health
* The Mystical Trader now has more items for sale.
* The Mystical Trader will now display the stats for all items that he sells as well as the price.
* Added The Healer NPC: Will heal for a small price
* Items can now be classified according to their rarirty: "Normal", "Rare", "Unique".
* Added a boss to the map
* First final objective introduced: Defeat the boss
* Minor bug fixes
* The Mystical Trader sells more items
* Minor bug fixes

**Monster_Hunter Dev Change v1.5**

* Simplified theBoard list
* Added few normal items to be found around the board
* Fixed item stats bug where looking up the Leather Armour breaks the game
* When placing items on the board, each item needed a separate if statement in the Monster_Hunter.py checkEncounters function. This has been replaced with a single for loop that iterates over items in a new list -> on_board_items located in ItemClass.py.

**Monster_Hunter Dev Change v1.6**

* Added player level and xp to PlayerClass
* Added a simple level up function
* Player is now able to pick a statistic to level up
* Adjusted Bald Orc and Destroyer Orc stats to account for items on the board
