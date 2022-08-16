movie_name=input()
hall_type=input()
bought_tickets=int(input())
price_per_ticket=0

if movie_name=="A Star Is Born":
    if hall_type=="normal":
       price_per_ticket=7.5
    elif hall_type=="luxury":
        price_per_ticket=10.5
    elif hall_type=="ultra luxury":
        price_per_ticket=13.5
elif movie_name=="Bohemian Rhapsody":
    if hall_type=="normal":
       price_per_ticket=7.35
    elif hall_type=="luxury":
        price_per_ticket=9.45
    elif hall_type=="ultra luxury":
        price_per_ticket=12.75
elif movie_name=="Green Book":
    if hall_type=="normal":
       price_per_ticket=8.15
    elif hall_type=="luxury":
        price_per_ticket=10.25
    elif hall_type=="ultra luxury":
        price_per_ticket=13.25
elif movie_name=="The Favourite":
    if hall_type=="normal":
       price_per_ticket=8.75
    elif hall_type=="luxury":
        price_per_ticket=11.55
    elif hall_type=="ultra luxury":
        price_per_ticket=13.95
total=bought_tickets*price_per_ticket
print(f"{movie_name} -> {total:.2f} lv.")