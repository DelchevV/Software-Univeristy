energy=100
coins=100
list_of_events=input().split("|")
number_of_events=len(list_of_events)
for event in range(number_of_events):
    for element in list_of_events:
        current_energy=0
        command_amount_list=element.split("-")
        command=command_amount_list[0]
        amount=int(command_amount_list[-1])
        if command=="rest":
            current_energy=amount
            if energy+current_energy>=100:
                pass
            else:
                pass

