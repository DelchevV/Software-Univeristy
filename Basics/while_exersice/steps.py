daily_step_goal=10000
current_steps=0
command=input()
while command!="Going home":

    current_steps+=int(command)
    if current_steps>=daily_step_goal:
        break
    command = input()
if command=="Going home":
    current_steps+=int(input())
diffrence=abs(daily_step_goal-current_steps)
if daily_step_goal>current_steps:
    print(f"{diffrence} more steps to reach goal.")
else:
    print("Goal reached! Good job!")
    print(f"{diffrence} steps over the goal!")
