height=float(input())
width=float(input())
not_covered_area=int(input())
needed_liters=((height*width)*4)
needed_liters=int(needed_liters-(needed_liters*not_covered_area/100))
current_liters=0
command=input()
while command!="Tired!":
    current_liters+=int(command)
    if current_liters>=needed_liters:
        break
    command=input()
diffrence=abs(current_liters-needed_liters)
if diffrence==0:
    print(f"All walls are painted! Great job, Pesho!" )
else:
    if command=="Tired!":
        print(f"{diffrence} quadratic m left.")
    else:
        print(f"All walls are painted and you have {diffrence} l paint left!")

