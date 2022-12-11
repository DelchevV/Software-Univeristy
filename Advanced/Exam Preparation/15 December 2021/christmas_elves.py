from collections import deque

elf_energy = deque(map(int, input().split()))
material_boxes = list(map(int, input().split()))
gifts = 0
counter = 1
spent_energy = 0
while elf_energy and material_boxes:
    cookie_reward = 1
    if elf_energy[0] < 5:
        elf_energy.popleft()
        counter += 1
        continue

    if counter % 3 == 0:
        if elf_energy[0] >= material_boxes[-1] * 2:
            if counter % 5 != 0:
                cookie_reward = 0
                gifts += 2

            energy = elf_energy.popleft()
            spent_energy += material_boxes[-1] * 2
            energy -= (material_boxes.pop() - cookie_reward)
            elf_energy.append(energy)

        else:
            elf_energy.append(elf_energy.popleft() * 2)

    elif elf_energy[0] >= material_boxes[-1]:
        if counter % 5 != 0:
            gifts += 1
            cookie_reward = 0

        energy = elf_energy.popleft()
        spent_energy += material_boxes[-1]
        energy -= (material_boxes.pop() - cookie_reward)
        elf_energy.append(energy)



    else:
        elf_energy.append(elf_energy.popleft() * 2)

    counter += 1

print(f"Toys: {gifts}")
print(f"Energy: {spent_energy}")
if elf_energy:
    print(f'Elves left: {", ".join(map(str, elf_energy))}')
if material_boxes:
    print(f'Boxes left: {", ".join(map(str, material_boxes))}')
