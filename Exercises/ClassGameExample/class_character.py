from weapon import fists # We are bringing in weapons for the character


class Character:
    def __init__(self, name, health): #removed damage
        self.name = name
        self.health = health
        self.health_max = health
        #self.damage = damage // Removing self.damage as we want to use weapons


        self.weapon = fists #All character will have fists as a weapon

    def attack(self, target) -> None:
        #target.health -= self.damage # this will reduce the health by damage taken // This too
        target.health -= self.weapon.damage # this will reduce the health by damage taken by the weapon
        target.health = max(target.health, 0) #This will prevent health going into the negative
        #prints attacks to the screen
        print(f"{self.name} dealt {self.weapon.damage} damage to {target.name} with {self.weapon.name}")


#Class Inheritance / Creating sub classes based of the parent class

class Hero(Character): #adding Character means it will use all the attributes from it
    def __init__(self, name, health) -> None:
        # This will use the variables from the parent class instead of creating new ones
        super().__init__(name=name, health=health)

        self.default_weapon = self.weapon # Creating the default weapon

    def equip(self, weapon)-> None:
        self.weapon = weapon
        print(f"{self.name} equipped a(n) {self.weapon.name}!")

    def drop(self)-> None: #If hero drops their weapon, they will use fists
        print(f"{self.name} dropped the {self.weapon.name} !")
        self.weapon = self.default_weapon

class Enemy(Character): #adding Character means it will use all the attributes from it
    def __init__(self, name, health,weapon) -> None:  #adding a weapon for enemy
        # This will use the variables from the parent class instead of creating new ones
        super().__init__(name=name, health=health)
        self.weapon = weapon #added weapon option here