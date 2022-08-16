import math

ball_counts=int(input())
red_balls=0
orange_balls=0
yellow_balls=0
white_balls=0
other_balls=0
black_balls=0
point=0
for ball in range(ball_counts):
    ball_color=input()
    if ball_color=="red":
        point+=5
        red_balls+=1
    elif ball_color=="orange":
        point+=10
        orange_balls+=1
    elif ball_color=="yellow":
        point+=15
        yellow_balls+=1
    elif ball_color=="white":
        point+=20
        white_balls+=1
    elif ball_color=="black":
        point/=2
        math.floor(point)
        black_balls+=1
    else:
        other_balls+=1
print(f"Total points: {int(point)}")
print(f"Red balls: {red_balls}")
print(f"Orange balls: {orange_balls}")
print(f"Yellow balls: {yellow_balls}")
print(f"White balls: {white_balls}")
print(f"Other colors picked: {other_balls}")
print(f"Divides from black balls: {black_balls}")