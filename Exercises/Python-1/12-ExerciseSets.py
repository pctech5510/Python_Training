# You are working for the school Principal. We have a database of school students:
school = {'Bobby','Tammy','Jammy','Sally','Danny'}

#during class, the teachers take attendance and compile it into a list.
attendance_list = ['Jammy', 'Bobby', 'Danny', 'Sally']

#using what you learned about sets, create a piece of code that the school principal can use to immediately find out who missed class so they can call the parents. (Imagine if the list had 1000s of students. The principal can use the lists generated by the teachers + the school database to use python and make his/her job easier): Find the students that miss class!


# create a piece of code that the school principal can use to immediately find out who missed class

# using set.difference, this will compare both variables, and list the difference,
# or in this use case, it is what is the who's playing hooky or "difference".
print(set.difference(school,attendance_list))
#Another way to do the same thing, less code or refactoring
print(school.difference(attendance_list))