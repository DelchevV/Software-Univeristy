days=5
pocket_money=float(input())
daily_profit=float(input())
all_expenses=float(input())
gift_price=float(input())

earned_money=(daily_profit*days + pocket_money*days)-all_expenses
diff=abs(earned_money-gift_price)

if gift_price<=earned_money:
    print(f"Profit: {earned_money:.2f} BGN, the gift has been purchased.")
else:
    print(f"Insufficient money: {diff:.2f} BGN.")