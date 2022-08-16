first_employee=int(input())
second_employee=int(input())
third_employee=int(input())
question=int(input())
working_hour=0
answered_questions=0
question_per_hour=first_employee+second_employee+third_employee
while True:
    if question<=0:
        break
    if working_hour%4==0:
        working_hour+=1
        continue
    answered_questions+=question_per_hour
    if answered_questions>=question:
        break
    working_hour+=1
print(f"Time needed: {working_hour}h.")

