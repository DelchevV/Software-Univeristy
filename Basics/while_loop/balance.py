input_line=input()
sum=0
balance=0
while input_line!="NoMoreMoney":
    amount=float(input_line)
    if amount<0:
        print("Invalid operation!")
        break
    else:
        balance=balance+amount
        print(f"Increase: {amount:.2f}")

    input_line=input()

print(f"Total: {balance:.2f}")