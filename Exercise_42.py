#Create a password Checker, and hide the user's password from the output.


username = input('Please enter your username: ')
password = input('Please enter your password: ')
length = len(password)
hidden = "*" * length



print(f"{username}, your password {hidden} is {length} letters long")