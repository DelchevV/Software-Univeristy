def convert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    formated_time_of_waling=[hour,minutes,seconds]
    return  formated_time_of_waling


leaving_time = list(map(int, input().split(":")))
total_steps = int(input())
seconds_per_step = int(input())


walking_time=total_steps*seconds_per_step
arr_time=convert(walking_time)

# print(leaving_time)
# print(arr_time)

l_hour=leaving_time[0]
l_minute=leaving_time[1]
l_second=leaving_time[2]

a_hour=arr_time[0]
a_minute=arr_time[1]
a_second=arr_time[2]

home_seconds=0
home_minutes=0
home_hours=0

if a_second+l_second>=60:
    home_seconds=abs((a_second+l_second)-60)
    home_minutes+=1
else:
    home_seconds=a_second+l_second
if a_minute+l_minute>=60:
    home_minutes=abs((a_minute+l_minute)-60)
    home_hours+=1
else:
    home_minutes+=a_minute+l_minute
if a_hour+l_hour>24:
    home_hours=abs(a_hour+l_hour-24)
else:
    home_hours+=a_hour+l_hour

time=[home_hours,home_minutes,home_seconds]

print("Time Arrival: "+"%d:%02d:%02d" % (home_hours, home_minutes, home_seconds))
