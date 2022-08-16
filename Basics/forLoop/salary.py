open_tabs=int(input())
salary=float(input())
punishment=0

for num in range(open_tabs):
    site_name=input()
    if site_name=="Facebook":
        punishment+=150
    elif site_name=="Instagram":
        punishment+=100
    elif site_name=="Reddit":
        punishment+=50
    if punishment>=salary:
        break
diffrence=abs(salary-punishment)
if salary>punishment:
    print(f"{diffrence:.0f}")
else:
    print("You have lost your salary.")