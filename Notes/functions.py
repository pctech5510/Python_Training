#Functions

def funky():
    print("Dis be funky mon")
    print("\n")
funky()

##########################################

# Using arguments and parameters
#parameters go here
 #positional parameters
def funky(name, stank):
    print(f"Dis be funky mon {name}, you smell worse than {stank}")

#arguments go here, which mean you need to fill in the
#parameters with arguments when you call the function
#positional parameters : means the arguments and parameters
# have to match or else they will not make sense
#Look at tim for the example

funky("jim", "rotten eggs")
funky( "cat litter", "tim")
funky("bob", "liver town")
print("\n")


#default parameters= incase you forget to use arguments or
#don't need them.
def funky2(name="forgetful", stank="flowers"):
    print(f"Dis be funky mon {name}, you smell worse than {stank}")



#keyword arguments are used when position doesn't matter
funky2(stank="poop", name="william")
funky2()
print("\n")

#############################
#Function Return

def sum1(num1, num2):
    num1+num2
sum1(4,5)
print("no output")
print("\n")

#Using Return NOTE when using return it will exit the function
def sum2(num1, num2):
    return num1+num2
print(sum2(4,5))

