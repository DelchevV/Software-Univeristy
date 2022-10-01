size = int(input())
bunny_pos = []
field = []
best_sum = 0
best_sum_pos = {
    'left': [],
    'right': [],
    'up': [],
    'down': []
}
directions = {
    "up": (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}
for row in range(size):
    line = input().split()
    field.append(line)
    if 'B' in line:
        p1 = row
        p2 = line.index("B")
        bunny_pos = [p1, p2]

r, c = bunny_pos
sum_u = 0
# up
while True:
    r -= 1
    if 0 <= r < size and 0 <= c < size:
        if field[r][c] == "X":
            break
        else:
            if int(field[r][c]) > 0:
                sum_u += int(field[r][c])
                best_sum_pos['up'].append([r, c])
    else:
        break

r, c = bunny_pos
sum_d = 0
# down
while True:
    r += 1
    if 0 <= r < size and 0 <= c < size:
        if field[r][c] == "X":
            break
        else:
            if int(field[r][c]) > 0:
                sum_d += int(field[r][c])
                best_sum_pos['down'].append([r, c])
    else:
        break

r, c = bunny_pos
sum_l = 0
# left
while True:
    c -= 1
    if 0 <= r < size and 0 <= c < size:
        if field[r][c] == "X":
            break
        else:
            if int(field[r][c]) > 0:
                sum_l += int(field[r][c])
                best_sum_pos['left'].append([r, c])
    else:
        break

r, c = bunny_pos
sum_r = 0
# down
while True:
    c += 1
    if 0 <= r < size and 0 <= c < size:
        if field[r][c] == "X":
            break
        else:
            if int(field[r][c]) > 0:
                sum_r += int(field[r][c])
                best_sum_pos['right'].append([r, c])
    else:
        break

if sum_l > sum_r and sum_l > sum_u and sum_l > sum_d:
    print('left')
    for result in best_sum_pos['left']:
        print(result)
    print(sum_l)

elif sum_r > sum_l and sum_r > sum_u and sum_r > sum_d:
    print('right')
    for result in best_sum_pos['right']:
        print(result)
    print(sum_r)

elif sum_u > sum_l and sum_u > sum_d and sum_u > sum_r:
    print('up')
    for result in best_sum_pos['up']:
        print(result)
    print(sum_u)

elif sum_d > sum_l and sum_d > sum_u and sum_d > sum_r:
    print('down')
    for result in best_sum_pos['down']:
        print(result)
    print(sum_d)
