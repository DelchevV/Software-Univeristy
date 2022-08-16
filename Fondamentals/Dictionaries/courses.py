courses={}
while True:
    data=input()
    if data=="end":
        break
    data=data.split(" : ")
    course=data[0]
    name=data[1]
    if course not in courses:
        courses[course]=[]
        courses[course].append(name)
    else:
        courses[course].append(name)
for key,value in courses.items():
    print(f"{key}: {len(value)}")
    for item in value:
        print(f"-- {item}")

