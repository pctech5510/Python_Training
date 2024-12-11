# Create a script to easily add multiple employee information into a system.

# create the class
class Employee:
    # print out the number of employees
    num_employees = 0
    # adds raise amount
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = "first" + "." + "last" + "@company.com"

        Employee.num_employees += 1

    # Method to print out first and last name
    def fullname(self):
        return f"{self.first} {self.last}"

    # Add an annual raise for employees
    def apply_Raise(self):
        self.pay = int(self.pay * self.raise_amount)


emp1 = Employee('Jeff', 'Jones', 50000)
emp2 = Employee('Roger', "backenfeel", 30000)

emp1.apply_Raise()
print(f"There are {Employee.num_employees} employees in the company.")
print(f"{emp1.fullname()} will receive {emp1.raise_amount} which will bring the total pay"
      f" too {emp1.pay}")

emp2.apply_Raise()
print(f"{emp2.fullname()} will receive {emp2.raise_amount} which will bring the total pay"
      f" too {emp2.pay}")
