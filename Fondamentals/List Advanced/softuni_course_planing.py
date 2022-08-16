
lessons=input().split(", ")
schedule_num=1
schedule_item=0
while True:

    data=input().split(":")
    command=data[0]
    if command=="course start":
        break
    if command=="Add":
        item_for_add=data[-1]
        if item_for_add not in lessons:
            lessons.append(item_for_add)
    elif command=="Insert":
        item_for_insert=data[1]
        index=int(data[-1])
        if item_for_insert not in lessons:
            lessons.insert(index,item_for_insert)
    elif command=="Swap":
        first_for_swap=data[1]
        second_for_swap=data[2]
        if first_for_swap in lessons and second_for_swap in lessons:
            first_index=lessons.index(first_for_swap)
            second_index=lessons.index(second_for_swap)
            lessons[first_index],lessons[second_index]=lessons[second_index],lessons[first_index]
    elif command=="Exercise":
        item_for_exercise=data[1]
        if item_for_exercise in lessons:
            index=lessons.index(item_for_exercise)
            lessons[index]+="-Exercise"
        else:
            lessons.append(item_for_exercise)
            lessons.append(item_for_exercise+"-Exercise")
    elif command=="Remove":
        item_for_remove=data[1]
        if item_for_remove in lessons:
            lessons.remove(item_for_remove)

    #трябва да направя упражнението винаги да следва самия лесон, а не да остава някъде

    print(lessons)
    # print(str(schedule_num)+"."+str(lessons[schedule_item]))
    # schedule_num+=1
    # schedule_item+=1



