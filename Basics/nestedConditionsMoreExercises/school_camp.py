season=input()
type_of_group=input()
students_count=int(input())
sleepovers_count=int(input())
sport_type=" "
price=0

if season=="Winter":
    if type_of_group=="boys" or type_of_group=="girls":
        price=students_count*sleepovers_count*9.60
    elif type_of_group=="mixed":
        price = students_count * sleepovers_count * 10
elif season=="Spring":
    if type_of_group=="boys" or type_of_group=="girls":
        price=students_count*sleepovers_count*7.20
    elif type_of_group=="mixed":
        price = students_count * sleepovers_count * 9.50
elif season=="Summer":
    if type_of_group=="boys" or type_of_group=="girls":
        price=students_count*sleepovers_count*15
    elif type_of_group=="mixed":
        price = students_count * sleepovers_count * 20

if students_count>=50:
    price*=0.50
elif 20<= students_count <50:
    price*=0.85
elif 10<= students_count<20:
    price*=0.95

if season=="Winter":
    if type_of_group=="girls":
        sport_type="Gymnastics"
    elif type_of_group=="boys":
        sport_type="Judo"
    elif type_of_group=="mixed":
        sport_type="Ski"
elif season=="Spring":
    if type_of_group=="girls":
        sport_type="Athletics"
    elif type_of_group=="boys":
        sport_type="Tennis"
    elif type_of_group=="mixed":
        sport_type="Cycling"
elif season=="Summer":
    if type_of_group=="girls":
        sport_type="Volleyball"
    elif type_of_group=="boys":
        sport_type="Football"
    elif type_of_group=="mixed":
        sport_type="Swimming"

print(f"{sport_type} {price:.2f} lv.")
