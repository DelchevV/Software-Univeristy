price_bags_over_20kg=float(input())
bags_kg=float(input())
days_till_flight=int(input())
bags=int(input())
bag_price=0

if bags_kg <10:
    bag_price=price_bags_over_20kg*0.20
elif bags_kg <=20:
    bag_price=price_bags_over_20kg*0.50
elif bags_kg>20:
    bag_price=price_bags_over_20kg

if days_till_flight<7:
    bag_price=bag_price+bag_price*0.40
elif days_till_flight<=30:
    bag_price=bag_price + bag_price*0.15
elif days_till_flight>30:
    bag_price=bag_price + bag_price*0.10

final_price=bag_price*bags
print(f" The total price of bags is: {final_price:.2f} lv. ")