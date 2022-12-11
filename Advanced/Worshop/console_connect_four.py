import colorama

rows, cols = 6, 7
playground = [["0"] * cols for row in range(rows)]

movements = (
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1),
    (-1, -1),
    (-1, 1),
    (1, -1),
    (1, 1)
)
players = [["player 1", 1], ['player 2', 2]]

while True:
    is_won = False
    player, sign = players.pop(0)
    row = 0
    picked_column = int(input(f"{player} please choose a column: ")) - 1

    while True:

        if row == rows - 1 or playground[row + 1][picked_column] != '0':
            playground[row][picked_column] = sign
            break

        row += 1

    for row in range(rows):
        for col in range(cols):
            if playground[row][col] != picked_column:
                continue

            for move in movements:
                r, c = row, col

                for _ in range(3):
                    r, c = r + move[0], c + move[1]

                    if not (0 <= r < rows and 0 <= c < cols):
                        break

                    if playground[r][c] != sign:
                        break
                else:
                    print()
                    [print(f'[ {", ".join(map(str, row))} ]') for row in playground]

                    if sign == 1:
                        print(colorama.Fore.GREEN + f"{player} wins!")
                    else:
                        print(colorama.Fore.YELLOW + f"{player} wins!")

                    is_won = True

    if is_won:
        break
    else:
        [print(f'[ {", ".join(map(str, row))} ]') for row in playground]
        print()
        players.append([player, sign])
