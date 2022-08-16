town=input()
sales=float(input())
commission=0
is_valid="True"
if town=="Sofia":
    if sales>=0 and sales <=500:
       commission=sales*0.05
    elif sales <=1000:
        commission=sales*0.07
    elif sales <=10000:
        commission=sales*0.08
    elif sales <=10000:
        commission=sales*0.1
    else:
        is_valid="False"
elif town=="Varna":
    if sales>=0 and sales <=500:
       commission=sales*0.045
    elif sales <=1000:
        commission=sales*0.075
    elif sales <=10000:
        commission=sales*0.1
    elif sales >10000:
        commission=sales*0.12
    else:
        is_valid="False"
elif town=="Plovdiv":
    if sales>=0 and sales <=500:
       commission=sales*0.055
    elif sales <=1000:
        commission=sales*0.08
    elif sales <=10000:
        commission=sales*0.12
    elif sales <=10000:
        commission=sales*0.145
    else:
        is_valid="False"
else:
    is_valid="False"

if is_valid=="True":
    print(f"{commission:.2f}")
elif is_valid=="False":
    print("error")
