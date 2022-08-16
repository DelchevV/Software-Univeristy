import sys

command=input()
most_goals=-sys.maxsize
best_player=""
is_het_trick=False
while command!="END":
    goals = int(input())
    if goals>most_goals:
        most_goals=goals
        best_player=command
        if goals>=3:
            is_het_trick=True
        else:
            is_het_trick=False
        if goals>=10:
            break
    command = input()


print(f"{best_player} is the best player!")
if is_het_trick:
    print(f"He has scored {most_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {most_goals} goals.")