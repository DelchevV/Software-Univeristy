budget = float(input())
price_1kg_flour = float(input())
price_per_pack_eggs = price_1kg_flour * 0.75
price_per_1l_milk = (price_1kg_flour * 1.25) / 4
loaves = 0
colored_eggs = 0
money_left=0
cost_per_loaf = price_1kg_flour + price_per_1l_milk + price_per_pack_eggs
while budget != cost_per_loaf or budget < cost_per_loaf:
    if budget<cost_per_loaf:
        break
    budget-=cost_per_loaf
    loaves += 1
    colored_eggs += 3
    if loaves % 3 == 0:
        colored_eggs -= loaves - 2
print(f"You made {loaves} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
