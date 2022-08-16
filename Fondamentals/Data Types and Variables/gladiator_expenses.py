lost_fights=int(input())
helmet_price=float(input())
sword_price=float(input())
shield_price=float(input())
armor_price=float(input())

total_helmets=lost_fights//2
total_sword=lost_fights//3
total_shield=lost_fights//6
total_armor=total_shield//2
total_price=total_helmets*helmet_price +\
    total_sword*sword_price +\
    total_shield*shield_price +\
    total_armor*armor_price
print(f"Gladiator expenses: {total_price:.2f} aureus")
