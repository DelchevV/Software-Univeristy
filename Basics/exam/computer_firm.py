pc_count=int(input())
made_sells=0
average_rating=0
for pc in range(pc_count):
    current_input=int(input())
    rating=current_input%10
    possible_sells=current_input // 10
    if rating==2:
        made_sells+=0
    elif rating==3:
        made_sells+=possible_sells/2
    elif rating==4:
        made_sells+=possible_sells*0.7
    elif rating==5:
        made_sells+=possible_sells*0.85
    elif rating==6:
        made_sells+= possible_sells
    average_rating+=rating
average_rating/=pc_count
print(f"{made_sells:.2f}")
print(f"{average_rating:.2f}")