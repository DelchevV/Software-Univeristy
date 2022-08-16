def tax_fun(price):
    tax = price * 0.2
    return tax


tax = 0
price_without_taxes=0
total=0
customer_type=""
while True:
    data = input()
    if data == "special" or data == "regular":
        customer_type=data
        break
    if float(data) < 0:
        print("Invalid price!")
        continue
    tax += tax_fun(float(data))
    price_without_taxes+=float(data)
total=tax+price_without_taxes

if total==0:
    print("Invalid order!")
else:
    if customer_type=="special":
        total*=0.9
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {price_without_taxes:.2f}$")
    print(f"Taxes: {tax:.2f}$")
    print("-----------")
    print(f"Total price: {total:.2f}$")