budget=float(input())
category=input()
people_in_group=int(input())

vip_ticket=499.99
normal_ticket=249.99

money_for_transport=0
cost_of_ticket=0

if people_in_group>=1 and people_in_group<=4:
    money_for_transport=budget*0.75
elif people_in_group<=9:
    money_for_transport=budget*0.60
elif people_in_group<=24:
    money_for_transport=budget*0.50
elif people_in_group<=49:
    money_for_transport=budget*0.40
elif people_in_group>=50:
    money_for_transport=budget*0.25

if category=="VIP":
    cost_of_ticket=people_in_group*vip_ticket
elif category=="Normal":
    cost_of_ticket=people_in_group*normal_ticket

total=money_for_transport+cost_of_ticket
diffrence=abs(budget-total)

if budget>=total:
    print(f"Yes! You have {diffrence:.2f} leva left.")
else:
    print(f"Not enough money! You need {diffrence:.2f} leva.")


