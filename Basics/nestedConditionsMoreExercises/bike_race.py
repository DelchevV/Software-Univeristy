juniors=int(input())
seniors=int(input())
trace=input()
price=0

if trace=="trail":
    price=juniors*5.50+seniors*7
elif trace=="cross-country":
    if seniors+juniors>=50:
        price=(juniors*8+seniors*9.50)*0.75
    else:
        price = juniors * 8 + seniors * 9.50
elif trace=="downhill":
    price=juniors*12.25+seniors*13.75
elif trace=="road":
    price=juniors*20+seniors*21.50

charity=price*0.95

print(f"{charity:.2f}")