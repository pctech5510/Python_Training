#This will be the starting point of the game and battle system
from weapon import short_bow, iron_sword #Imported weapons from the weapons file
# this will import your character class to use in this file.
from class_character import Hero,Enemy #removed character class

#We are giving the characters life now
hero = Hero(name="Hero", health=100) #removed damage to use weapon damage instead.
hero.equip(iron_sword)
#hero = Character(name="Hero", health=100) #removed damage to use weapon damage instead.
enemy = Enemy(name="Enemy", health=100, weapon=short_bow) #removed damage to use weapon damage instead.
#enemy = Character(name="Enemy", health=100) #removed damage to use weapon damage instead.

while True:
    hero.attack(enemy)
    enemy.attack(hero)

    print(f"Health of {hero.name}: {hero.health}")
    print(f"Health of {enemy.name}: {enemy.health}")

    if enemy.health == 0:
        print(f"{hero.name} has won!")
        break
    if hero.health == 0:
        print(f"{hero.name} has won!")
        break



    #hero.drop() Enable this to see the drop function in action
    input() #Press enter to continue the while loop in the terminal
