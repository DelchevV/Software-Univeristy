old_record=float(input())
distance=float(input())
time_per_meter=float(input())
delay=distance//15 *12.5
total_time= distance*time_per_meter+delay

if total_time<old_record:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    diffrence=abs(total_time-old_record)
    print(f"No, he failed! He was {diffrence:.2f} seconds slower.")