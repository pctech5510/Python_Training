#Create a password Checker, and hide the user's password from the output.


username = input('Please enter your username: ')
password = input('Please enter your password: ')
password_length = len(password)
hidden_password = "*" * password_length



print(f"{username}, your password {hidden_password} is {password_length} letters long")