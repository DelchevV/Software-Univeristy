students=int(input())
top_students=0
btw_4_5=0
btw_3_4=0
failed=0
average=0
for i in range(students):
    grade=float(input())
    if grade<=2.99:
        failed+=1
    elif grade<=3.99:
        btw_3_4+=1
    elif grade<=4.99:
        btw_4_5+=1
    else:
        top_students+=1
    average+=grade
average/=students
print(f"Top students: {top_students/students*100:.2f}%")
print(f"Between 4.00 and 4.99: {btw_4_5/students*100:.2f}%")
print(f"Between 3.00 and 3.99: {btw_3_4/students*100:.2f}%")
print(f"Fail: {failed/students*100:.2f}%")
print(f"Average: {average:.2f}")