import math

name_of_serial=input()
duration_of_series=int(input())
duration_of_break=int(input())
time_for_lunch=duration_of_break/8
time_for_breath=duration_of_break/4
remaining_time=duration_of_break-time_for_breath-time_for_lunch

diffrence=abs(duration_of_series-remaining_time)

if duration_of_series>remaining_time:
    print(f"You don't have enough time to watch {name_of_serial}, you need {math.ceil(diffrence)} more minutes.")
else:
    print(f"You have enough time to watch {name_of_serial} and left with {int(diffrence)} minutes free time.")