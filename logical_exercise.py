is_magician = False
is_expert = True

#check if magician AND expert: "You are a master magician"
if is_magician and is_expert:
    print("You are a master magician")

#check if magician but not expert: "At least you're getting there"
elif is_magician and not is_expert:
    print("At least you're getting there")

#if you're not a magician: "You need magical powers"
elif  not is_magician:
    print("You need magical powers")