student_scores = input("Input a list of student scores \n").split() # 33 45 67 79 97 83 91 25 101
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
    
# ******************* It's the system of find out an max or min number automatically ********************
# print(min(student_scores))
# print(max(student_scores))

# ******************* But we need to do it's manually ***************************

max_number = 0
for top_number in student_scores:
    if max_number <= top_number:
        max_number = top_number
print(max_number)

