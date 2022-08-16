import sys

balls=int(input())
max_snowball_weight=-sys.maxsize
max_snowball_time=-sys.maxsize
max_snowball_quality=-sys.maxsize
max_snowball_value=-sys.maxsize

for ball in range(balls):
    snowball_weight=int(input())
    snowball_time=int(input())
    snowball_quality=int(input())
    current_snowball_value=(snowball_weight/snowball_time)**snowball_quality
    if current_snowball_value>max_snowball_value:
        max_snowball_value=current_snowball_value
        max_snowball_weight=snowball_weight
        max_snowball_time=snowball_time
        max_snowball_quality=snowball_quality

print(f"{max_snowball_weight} : {max_snowball_time} = {int(max_snowball_value)} ({max_snowball_quality})")
