hall_rent=int(input())
statues=hall_rent*0.70
food=statues*0.85
music=food/2
total=hall_rent+statues+food+music
print(f"{total:.2f}")