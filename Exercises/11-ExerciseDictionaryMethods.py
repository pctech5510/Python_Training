# Exercise Dictionary Methods
# Scroll to see answers.

# 1 Create a user profile for your new game.
# This user profile will be stored in a dictionary with keys: 'age', 'username', 'weapons', 'is_active' and 'clan'
profile = {
    "age": 29,
    "username": "",
    "weapon0": None,
    "is_active": True,
    "clan": None
}

# 2 iterate and print all the keys in the above user.
print(profile.keys())
print("\n")
# 3 Add a new weapon to your user
profile["weapon0"] = "knife"
print(profile)
print("A weapon has been added to your inventory")
print(profile.get("weapon0"))
print("\n")
# 4 Add a new key to include 'is_banned'. Set it to false
profile["is_banned"] = False
print(profile)
print(profile.get("is_banned"))
print("Thanks for behaving")
print("\n")
# 5 Ban the user by setting the previous key to True
profile["is_banned"] = True
print(profile)
print(profile.get("is_banned"))
print("Well, you cheated!!")
print("\n")

# 6 create a new user2 by copying the previous user and update the age value and username value.
print("Welcome Player 2")
profile2 = profile.copy()
profile2.update({"age": 60})
profile2.update({"username": "jeff"})
print(profile2)
print("\n")

print(profile)
print(profile2)
