days_off=int(input())
days_at_work=365-days_off
day_off_play_time=127
day_at_work_play_time=63
tom_max_play_time=30000
played_time_per_year= days_at_work*day_at_work_play_time+days_off*day_off_play_time
if played_time_per_year>tom_max_play_time:
    print('Tom will run away')
    remains=played_time_per_year-tom_max_play_time

    hours = remains // 60
    minutes = remains - hours * 60
    print(f"{hours} hours and {minutes} minutes more for play")
else:
    print("Tom sleeps well")
    remains=tom_max_play_time-played_time_per_year

    hours=remains//60
    minutes=remains-hours*60
    print(f"{hours} hours and {minutes} minutes less for play")

