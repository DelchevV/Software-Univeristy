name=input()
year=1
sum=0
expel=0
while year<=12:
    if expel>1:
        break
    grades=float(input())
    if grades<4:
        expel+=1
        continue
    sum+=grades
    if expel>1:
        break
    if grades<2:
        break
    if year==12:
        break
    year += 1
if year!=12:
    print(f"{name} has been excluded at {year} grade")
else:
    average=sum/12
    print(f"{name} graduated. Average grade: {average:.2f}")