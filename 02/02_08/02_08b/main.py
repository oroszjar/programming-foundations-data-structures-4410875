my_list = [1, 7, 3]
print(sorted(my_list, reverse=True))

student_grades = [('Botond', 91), ('Adam', 82), ('Cecil', 88)]
print(sorted(student_grades))
print(sorted(student_grades, key=lambda x:x[1], reverse=True))