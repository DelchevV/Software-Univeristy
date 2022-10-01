green_duration=int(input())
free_window=int(input())
free_till_red=green_duration
is_crashed=False
passed_cars=0
reamining_time=green_duration+free_window
while True:
    car=''
    if is_crashed:
        break
    entry=input()
    if entry=="END":
        break
    elif entry=="green":
        reamining_time=green_duration+free_window
        free_till_red=green_duration
        continue
    if free_till_red>0:
        car=entry
    if car:
        for ch in car:
            reamining_time-=1
            free_till_red-=1
            if reamining_time<0:
                print('A crash happened!')
                print(f"{car} was hit at {ch}.")
                is_crashed=True
                break
        passed_cars+=1
if not is_crashed:
    print('Everyone is safe.')
    print(f'{passed_cars} total cars passed the crossroads.')
