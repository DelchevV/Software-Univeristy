from collections import deque

fireworks = {
    "Palm Fireworks": 0,
    "Willow Fireworks": 0,
    "Crossette Fireworks": 0
}
perfect_fireworks = False

effects = deque(map(int, input().split(", ")))
powers = list(map(int, input().split(", ")))

while effects and powers:

    current_effect = effects.popleft()
    current_power = powers.pop()
    if current_power <= 0 and current_effect > 0:
        effects.appendleft(current_effect)
        continue
    if current_power > 0 and current_effect <= 0:
        powers.append(current_power)
        continue

    sum = current_power + current_effect
    if sum % 15 == 0:
        fireworks["Crossette Fireworks"] += 1
    elif sum % 5 == 0:
        fireworks["Willow Fireworks"] += 1
    elif sum % 3 == 0:
        fireworks["Palm Fireworks"] += 1
    else:
        current_effect -= 1
        effects.append(current_effect)
        powers.append(current_power)

    perfect = 0
    for f_type in fireworks:
        if fireworks[f_type] >= 3:
            perfect += 1

    if perfect == 3:
        perfect_fireworks = True
        break

if perfect_fireworks:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")

if effects:
    print(f"Firework Effects left: {', '.join(map(str, effects))}")
if powers:
    print(f"Explosive Power left: {', '.join(map(str, powers))}")

for key, value in fireworks.items():
    print(f"{key}: {value}")
