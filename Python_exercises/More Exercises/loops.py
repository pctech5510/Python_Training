""" #Print only the index of the number 50



for i,char in enumerate(list(range(100))):

    if i and char == 50:

        print(f"The index of {i} is {char}") """

"""

i = 0



while i < 50:

    print(i)

    i += 2

   """

""" # Print the picture below!

picture = [

    [0,0,0,1,0,0,0],

    [0,0,1,1,1,0,0],

    [0,1,1,1,1,1,0],

    [1,1,1,1,1,1,1],

    [0,0,0,1,0,0,0],

    [0,0,0,1,0,0,0]

]

for i in picture:

    for t in i:

        if t == 0:

            print(" ", end="")

        elif t == 1:

            print("*",end="")

    print("")

     """

# Check for duplicates in list:

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

for t in some_list:
    for d in t:
        if d == t:
            print(d)
else:
    print("Try again")