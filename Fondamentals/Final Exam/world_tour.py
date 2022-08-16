stops=input()


def add_func(stop, index, string):
    if 0 <= index < len(stop):
        stop=stop[:index]+string+stop[index:]
    print(stop)
    return stop


def remove_func(stop, start,end):
    if 0 <= start and end<len(stop):
        stop=stop[:start]+stop[end+1:]
    print(stop)
    return stop


def switch(old,new,stop):
    if old in stop:
        stop=stop.replace(old,new)
    print(stop)
    return stop


while True:
    entry=input().split(":")
    command=entry[0]
    if command=="Travel":
        break
    elif command=='Add Stop':
        indexes=int(entry[1])
        strings=entry[2]
        stops=add_func(stops,indexes,strings)
    elif command=='Remove Stop':
        start_index=int(entry[1])
        end_index=int(entry[2])
        stops=remove_func(stops, start_index,end_index)
    elif command=='Switch':
        old_str=entry[1]
        new_str=entry[2]
        stops=switch(old_str,new_str,stops)
print(f"Ready for world tour! Planned stops: {stops}")