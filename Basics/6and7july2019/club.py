wished_profit=float(input())
command=input()
drink_len=0
total_income=0

while command!="Party!":
    drinks=int(input())
    drink_len=len(command)
    current_order=drink_len*drinks
    if current_order %2!=0:
        current_order*=0.75
    total_income += current_order
    if total_income>=wished_profit:
        break

    command=input()
if command=="Party!":
    print(f"We need {wished_profit - total_income:.2f} leva more.")
else:
    print(f"Target acquired.")
print(f"Club income - {total_income:.2f} leva.")