days=int(input())
losses=0
wins=0
total_money=0
winner_days=0
loser_days=0
for day in range(days):
    command = input()
    daily_money = 0
    while command!="Finish":
        result=input()
        if result=="win":
            daily_money+=20
            wins+=1
        else:
            losses+=1
        command=input()
    if wins>losses:
      total_money+=daily_money*1.1
      winner_days+=1
    else:
        total_money+=daily_money
        loser_days+=1
    losses=0
    wins=0
if winner_days>loser_days:
    total_money*=1.2
    print(f"You won the tournament! Total raised money: {total_money:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total_money:.2f}")
