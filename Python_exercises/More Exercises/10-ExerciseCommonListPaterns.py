#fix this code so that it prints a sorted list of all of our friends (alphabetical). Scroll to see answer
friends = ['Simon', 'Patty', 'Joy', 'Carrie', 'Amira', 'Chu']

new_friend = ['Stanley']

friends.sort()
print(friends)  #Assorted alphabetical

#Add Stanley and assort alphabetical
friends.extend(new_friend) #extend will iterate through the new_friend list and add to the original list.
print(friends) #this will print out the added list action seen above
