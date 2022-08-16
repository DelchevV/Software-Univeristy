list_input=list(input().split())
time_intervals=[]
left_racer=[]
right_racer=[]
sum_left_racer=0
sum_right_racer=0
split_index=len(list_input)//2+1
for item in list_input:
    time_intervals.append(int(item))
left_racer=time_intervals[:split_index-1]
right_racer=time_intervals[split_index:]
right_racer.reverse()
for step in left_racer:
    if step==0:
        sum_left_racer*=0.8
    else:
        sum_left_racer+=step
for step in right_racer:
    if step==0:
        sum_right_racer*=0.8
    else:
        sum_right_racer+=step

if sum_right_racer<sum_left_racer:
    print(f"The winner is right with total time: {sum_right_racer:.1f}")
else:
    print(f"The winner is left with total time: {sum_left_racer:.1f}")