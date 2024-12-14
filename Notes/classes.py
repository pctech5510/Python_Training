### **Classes and Inheritance Example:**

'''In this example, we'll have a **base class** called `Character`, and then different **subclasses** like `Warrior`, `Mage`, and `Archer`, which will inherit from `Character` and add their own specific behaviors.'''

### 1. **The Base Class:**

#First, let's create the `Character` class that will serve as the base for other character types.


class Character:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def attack_enemy(self, enemy):
        print(f"{self.name} attacks {enemy.name} for {self.attack} damage.")
        enemy.health -= self.attack

    def is_alive(self):
        return self.health > 0

'''
In this base class:
- We define basic **attributes** like `name`, `health`, and `attack` that every character will have.
- We define **methods** like `attack_enemy()` for attacking and `is_alive()` to check if the character is still alive.

### 2. **Subclasses Using Inheritance:**

Now, let's define specific character types, such as `Warrior`, `Mage`, and `Archer`, that inherit from `Character` and override or extend functionality. '''

#### **Warrior Class:**

class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack=25)  # Calling the parent class constructor

    def use_shield(self):
        print(f"{self.name} uses a shield to block attacks!")

'''
- `Warrior` inherits from `Character`.
- We call the **parent class constructor** using `super()` to initialize the warrior with higher health and attack values.
- The `Warrior` also has an additional method `use_shield()` specific to warriors. '''

#### **Mage Class:**

class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack=40)  # Mage has lower health but higher attack

    def cast_spell(self):
        print(f"{self.name} casts a powerful fireball spell!")


# `Mage` inherits from `Character` and has its own `cast_spell()` method to perform magic attacks.

#### **Archer Class:**

class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=120, attack=20)  # Archer has moderate health and attack

    def shoot_arrow(self):
        print(f"{self.name} shoots an arrow from a distance!")


            #Archer` also inherits from `Character` and has a unique method `shoot_arrow()`.



### 3. **Using Inheritance to Create Objects:**

'''Now, we can create different types of characters using inheritance. They share common behavior (like attacking and checking health) but have their own unique actions.'''

# Creating instances of each character type
warrior = Warrior("Conan")
mage = Mage("Gandalf")
archer = Archer("Legolas")

# Warrior attacks Mage
warrior.attack_enemy(mage)

# Mage casts a spell
mage.cast_spell()

# Archer shoots an arrow
archer.shoot_arrow()

# Check if Mage is still alive
if not mage.is_alive():
    print(f"{mage.name} has been defeated.")

\


'''
**How Inheritance Works Here:** 

- **Base Class (`Character`)**: Contains shared attributes and methods for all characters.
- **Subclasses (`Warrior`, `Mage`, `Archer`)**: Each subclass inherits from `Character` and adds their own unique methods (e.g., `use_shield()`, `cast_spell()`, and `shoot_arrow()`).
- **`super().__init__()`**: This is used to call the constructor of the parent (`Character`), initializing shared attributes like health and attack, and allowing for subclass customization. 

**Key Points to Remember:**
- **Inheritance** allows subclasses to reuse code from a parent class.
- Subclasses can **override methods** from the parent class or **add new methods** specific to that subclass.
- This makes your code more **modular** and **extensible**, allowing you to easily add more character types without duplicating code.

**Why Use Inheritance in Games?
- It reduces code repetition. You only need to write shared behavior once in the base class.
- It allows for more flexible and scalable game design. For example, you can easily add new types of characters without modifying existing code.
- It encourages **separation of concerns**, making each class responsible for a specific aspect of the game. '''