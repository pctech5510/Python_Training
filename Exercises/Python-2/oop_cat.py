# Given the below class:
class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cat1 = Cat('Garfield', 4)
cat2 = Cat('Toni', 5)
cat3 = Cat('Mittens', 10)


# 2 Create a function that finds the oldest cat
def oldest_cat():
    return max(cat1.age, cat2.age, cat3.age)


def alternative_Old_Cat(*args):
    return max(args)


# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
print(f'Oldest Cat is {oldest_cat()} years old')
print(f'Oldest Cat is {alternative_Old_Cat(cat1.age, cat2.age, cat3.age)} years old!')
