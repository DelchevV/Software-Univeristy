enherited_money=float(input())
year_till_dead=int(input())
age_of_ivan=18
year=1800


for i in range(year,year_till_dead+1):
    if i%2==0:
        enherited_money-=12000
    else:
        enherited_money-= 12000 + 50 * age_of_ivan
    age_of_ivan += 1

if enherited_money<0:
    print(f"He will need {abs(enherited_money):.2f} dollars to survive.")
else:
    print(f"Yes! He will live a carefree life and will have {enherited_money:.2f} dollars left.")

