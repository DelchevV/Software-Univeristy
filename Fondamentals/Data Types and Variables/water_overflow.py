tank_capacity=255
pours=int(input())
liters=0
for pour in range(pours):
    current_liters=int(input())
    liters += current_liters
    if liters>tank_capacity:
        print(f"Insufficient capacity!")
        liters-=current_liters
        continue

print(liters)
