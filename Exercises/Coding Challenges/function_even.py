#Create a function to print out the highest even number in a list
list1 = [34,10, 2, 3, 4, 8, 11, 14, 16, 18, 19, 21,22,30]
def high_Even(li):
    evens = []
    for i in li:
        if i % 2 == 0:  #Determines if it's even
            evens.append(i) # Places number in the list
    return max(evens)  #Returns highest value in the new list
print(high_Even(list1))
