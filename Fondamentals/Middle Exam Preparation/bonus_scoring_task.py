import math

students=int(input())
lectures=int(input())
bonus=int(input())
student_list=[]
if students>0:
    for student in range(students):
        attendance=int(input())
        student_list.append(attendance)
highest_attendace=0
for high in student_list:
    if high>highest_attendace:
        highest_attendace=high
if lectures>0:
    total_bonus=math.ceil((highest_attendace/lectures)*(5+bonus))
else:
    total_bonus=0

print(f"Max Bonus: {total_bonus}.")
print(f"The student has attended {highest_attendace} lectures.")
# {total bonus} = {student attendances} / {course lectures} * (5 + {additional bonus})