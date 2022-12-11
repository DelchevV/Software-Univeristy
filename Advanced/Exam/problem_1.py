from collections import deque

milligrams_of_caffeine = list(map(int, input().split(", ")))
energy_drinks = deque(map(int, input().split(", ")))
drank_caffeine = 0

while milligrams_of_caffeine and energy_drinks:
    caffeine = milligrams_of_caffeine.pop()
    drink = energy_drinks.popleft()

    if (caffeine * drink + drank_caffeine) <= 300:
        drank_caffeine += caffeine * drink
    else:
        energy_drinks.append(drink)
        if drank_caffeine - 30 < 0:
            drank_caffeine = 0
        else:
            drank_caffeine -= 30

if energy_drinks:
    print(f'Drinks left: {", ".join(map(str, energy_drinks))}')
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with { drank_caffeine } mg caffeine.")