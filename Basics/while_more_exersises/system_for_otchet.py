charity_goal=int(input())
command=0
counter=1
card_money=0
cash_money=0
total_money=0
card_transactions=0
cash_transactions=0
current_cash=0
current_card=0
is_failed=True
while command!="End":
    counter += 1
    command = input()
    if command == "End":
        is_failed = True
        break
    if counter%2==0:
        if int(command)>100:
            print("Error in transaction!")
            continue
        else:
            current_cash=int(command)
            print("Product sold!")
            total_money+=current_cash
            cash_money+=current_cash
            cash_transactions+=1
    else:
        if int(command)<10:
            print("Error in transaction!")
            continue

        else:
            current_card=int(command)
            print("Product sold!")
            total_money+=current_card
            card_money+=current_card
            card_transactions+=1
    if total_money>=charity_goal:
        is_failed=False
        break


if is_failed:
    print(f"Failed to collect required money for charity.")
else:
    print(f"Average CS: {cash_money / cash_transactions:.2f}")
    print(f"Average CC: {card_money / card_transactions:.2f}")

