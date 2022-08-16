pen=int(input())
markers=int(input())
liters=int(input())
discount=float(input())/100

pen_price=5.80
markers_price=7.20
liters_price=1.20

sum= pen*pen_price+markers*markers_price+liters*liters_price
total=sum-sum*discount
print(sum)
print(total)