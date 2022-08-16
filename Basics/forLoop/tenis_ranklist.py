import math

tournaments=int(input())
starting_points=int(input())
wins=0
points=0
for i in range(tournaments):
    position_in_tournament=input()
    if position_in_tournament=="W":
        points+=2000
        wins+=1
    elif position_in_tournament=="F":
        points+=1200
    elif position_in_tournament=="SF":
        points+=720

average=points/tournaments
win_percentage=wins/tournaments*100

print(f"Final points: {points+starting_points}")
print(f"Average points: {math.floor(average)}")
print(f"{win_percentage:.2f}%")