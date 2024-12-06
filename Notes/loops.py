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

#We need to iterate through the list
another_list = []
#We will need to store the duplicates and print them out
for letter in some_list:
    if some_list.count(letter) > 1:
#We will make sure only 1 instance of the duplicate is put i the list
        if letter not in another_list:
            another_list.append(letter)

print(another_list)



