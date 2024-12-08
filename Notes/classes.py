#OOP
class PlayerCharacter:
    membership = True   #Class Object Attribute
    def __init__(self, name, age):
        self.name = name #attributes
        self.age = age

    def shout(self):
        print(f"You have entered {self.name}")
        print(f"You are {self.age} old")


player1 = PlayerCharacter('Cindy', 44)
player2 = PlayerCharacter('Tom', 21)

print(player1.shout())
print(player2.shout())