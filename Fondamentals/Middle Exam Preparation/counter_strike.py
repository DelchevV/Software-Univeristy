energy = int(input())
won_wars = 0
not_enough_energy=False
while True:
    command = input()
    if command == "End of battle":
        break
    current_war_energy = int(command)
    if current_war_energy>energy:
        not_enough_energy=True
        break
    if current_war_energy <= energy:
        won_wars += 1
        energy -= current_war_energy
    if won_wars%3==0:
        energy+=won_wars
if not_enough_energy:
    print(f"Not enough energy! Game ends with {won_wars} won battles and {energy} energy")
else:
    print(f"Won battles: {won_wars}. Energy left: {energy}" )
