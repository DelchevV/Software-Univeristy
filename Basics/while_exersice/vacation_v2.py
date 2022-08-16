needed_money=float(input())
current_balance=float(input())
spending_counter=0
total_days=0
spending_5_days_in_row=False
while current_balance<needed_money:
    action=input()
    current_sum=float(input())

    if action=="save":
        current_balance+=current_sum
        spending_counter=0
        total_days += 1
    else:
        current_balance-=current_sum
        spending_counter+=1
        total_days += 1
        if current_balance<current_sum:
            current_balance=0
        if spending_counter==5:
            spending_5_days_in_row=True
            break
if spending_5_days_in_row:
    print(f"You can't save the money.")
    print(f"{total_days}")
else:
    print(f"You saved the money for {total_days} days.")
