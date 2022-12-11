from collections import deque

bomb_effects = deque(map(int, input().split(", ")))
bomb_casing = deque(map(int, input().split(", ")))

types_of_bombs={
    'Cherry Bombs':0,
    'Datura Bombs':0,
    'Smoke Decoy Bombs':0,
}

is_pouched=False

while bomb_effects and bomb_casing:
    effect=bomb_effects.popleft()
    casing=bomb_casing.pop()
    value=effect+casing
    if value==40:
        types_of_bombs['Datura Bombs']+=1
    elif  value==60:
        types_of_bombs['Cherry Bombs']+=1
    elif value==120:
        types_of_bombs['Smoke Decoy Bombs']+=1
    else:
        casing-=5
        bomb_casing.append(casing)
        bomb_effects.appendleft(effect)

    for val in types_of_bombs.values():
        if val<3:
            break
    else:
        is_pouched=True

    if is_pouched:
        break

if is_pouched:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if bomb_effects:
    print(f'Bomb Effects: {", ".join(map(str,bomb_effects))}')
else:
    print("Bomb Effects: empty")

if bomb_casing:
    print(f'Bomb Casings: {", ".join(map(str,bomb_casing))}')
else:
    print("Bomb Casings: empty")

for key,value in types_of_bombs.items():
    print(f'{key}: {value}')