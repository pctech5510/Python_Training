from fontTools.merge.util import first


class Employee:
    # added a raise variable for better access to raise
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

    def fullname(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


emp1 = Employee('Corey', 'Schafer', 50000)
emp2 = Employee('Test', 'User', 60000)

# print the original pay
print(emp1.pay)
# print the added raise
emp1.apply_raise()
# print out pay with raise
print(emp1.pay)
