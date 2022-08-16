seasson=input()
km_per_month=float(input())
salary=0

if km_per_month<=5000:
    if seasson=="Spring" or seasson=="Autumn":
        salary=km_per_month*0.75
    elif seasson=="Summer":
        salary=km_per_month*0.90
    elif seasson=="Winter":
        salary=km_per_month*1.05
elif km_per_month<=10000:
    if seasson=="Spring" or seasson=="Autumn":
        salary=km_per_month*0.95
    elif seasson=="Summer":
        salary=km_per_month*1.10
    elif seasson=="Winter":
        salary=km_per_month*1.25
elif km_per_month <=20000:
    salary=km_per_month*1.45

salary*=4
salary*=0.90

print(f"{salary:.2f}")
