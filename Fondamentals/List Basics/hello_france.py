list_of_items_bought = input().split("|")
budget = float(input())
written_budget = budget
new_item_price_list = []
income = 0
string_new_item_price_list=""
for element in list_of_items_bought:
    is_valid = False
    current_product_price = element.split("->")
    product = current_product_price[0]
    price = float(current_product_price[-1])
    if budget < 0:
        break
    if price > budget:
        continue
    if product == "Clothes" and price <= 50:
        is_valid = True
    elif product == "Shoes" and price <= 35:
        is_valid = True
    elif product == "Accessories" and price <= 20.5:
        is_valid = True
    if is_valid:
        budget -= price
        new_price = round(price * 1.4, 2)
        income += new_price
        new_item_price_list.append(new_price)

for n in new_item_price_list:
    print(f"{n:.2f}", end=" ")

profit = (income - written_budget) + budget

print(f"\nProfit: {profit:.2f}")
if profit + written_budget > 150:
    print("Hello, France!")
else:
    print("Not enough money.")
