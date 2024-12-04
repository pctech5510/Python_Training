#What is the output of this code?
#Before you click RUN, guess the output of each print statement!
new_list = ['a', 'b', 'c']
print(new_list[1]) #b
print(new_list[-2]) #b
print(new_list[1:3]) #b [b, c]  It's using zero index, and 1:3 B, C
new_list[0] = 'z' 
print(new_list) #[empty  # z, b, c  This placed Z in A's position to the begining of the new_list

my_list = [1,2,3]
bonus = my_list + [5]
my_list[0] = 'z' 
print(my_list)
print(bonus) #1,2,3,5 This added 5 to the end of the list my_list var + 5.. as in the above example, we used index 0 to put in Z