students_heights = input("Input a list of students heights \n").split() # 123 234 121 142 129
# for n in students_heights:
#     print(type(int(n)))
# print(students_heights)

total_height = 0
for height in students_heights:
    total_height += int(height)
    
print(total_height)

number_of_students = 0
for student in students_heights:
    number_of_students += 1
    
print(number_of_students)

average_height = total_height / number_of_students
print(round(average_height))