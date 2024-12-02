# For every ( it needs to = 1
# for every ) it needs to = -1
# calulate the total until it hits -1
# print out the index / position when it hits -1

line = open("santa_list.txt").readline()
total = 1
for i, x in enumerate(line, 0):
    if x == '(':
        total += 1
    else:
        if total == 0:
            print(i)
            break
        total -= 1

    result = line.count('(') - line.count(')')
    print(result)


