student_info={}
while True:
    data = input().split(":")
    if len(data) == 1:
        course=data[0]
        break
    name=data[0]
    course=data[2].replace(" ","_")
    course=course.lower()
    key=data[1]
    student_info[key]=name,course

for student in student_info:
    if course in student_info[student]:
        print(f"{student_info[student][0]} - {student}")
