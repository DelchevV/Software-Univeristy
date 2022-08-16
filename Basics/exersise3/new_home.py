flower_type=input()
pieces_of_flower=int(input())
budget=int(input())
price=0

if flower_type=="Roses":
    if pieces_of_flower >80:
        price=(pieces_of_flower*5)*0.9
    else:
        price=pieces_of_flower*5
elif flower_type=="Dahlias":
    if pieces_of_flower > 90:
        price=(pieces_of_flower*3.80)*0.85
    else:
        price = pieces_of_flower * 3.80
elif flower_type=="Tulips":
    if pieces_of_flower > 80:
        price=(pieces_of_flower*2.80)*0.85
    else:
        price=pieces_of_flower*2.80
elif flower_type=="Narcissus":
    if pieces_of_flower<120:
        first_calculation=pieces_of_flower*3
        price=first_calculation+(first_calculation*0.15)
    else:
        price=pieces_of_flower * 3
elif flower_type=="Gladiolus":
    if pieces_of_flower<80:
        first_calculation = pieces_of_flower * 2.50
        price = first_calculation + (first_calculation * 0.2)
    else:
        price = pieces_of_flower * 2.50

diffrence=abs(budget-price)

if budget>=price:
    print(f"Hey, you have a great garden with {pieces_of_flower} {flower_type} and {diffrence:.2f} leva left.")
else:
    print(f"Not enough money, you need {diffrence:.2f} leva more.")