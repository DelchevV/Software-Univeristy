rows = 7
names = input().split(", ")
board = [input().split() for _ in range(rows)]
player_1 = [501, 0]
player_2 = [501, 0]
ch = ["D", "T", "B"]


def corresponding_nums(current_row, current_col):
    numbers = [int(board[current_row][0]),
               int(board[current_row][6]),
               int(board[0][current_col]),
               int(board[6][current_col])]
    return sum(numbers)


def check_win(player):
    if player[0] <= 0:
        return True


while True:

    first_r, first_c = list(map(int, input().strip("(").strip(")").split(", ")))
    if 0 <= first_r < rows and 0 <= first_c < rows:
        if board[first_r][first_c] == "B":
            player_1[1] += 1
            print(f"{names[0]} won the game with {player_1[1]} throws!")
            break
        elif board[first_r][first_c] == "D":
            res = corresponding_nums(first_r, first_c)
            player_1[0] -= (res * 2)

        elif board[first_r][first_c] == "T":
            res = corresponding_nums(first_r, first_c)
            player_1[0] -= (res * 3)

        else:
            player_1[0] -= int(board[first_r][first_c])

    player_1[1] += 1

    if check_win(player_1):
        print(f"{names[0]} won the game with {player_1[1]} throws!")
        break

    second_r, second_c = list(map(int, input().strip("(").strip(")").split(", ")))
    if 0 <= second_r < rows and 0 <= second_c < rows:
        if board[second_r][second_c] == "B":
            player_2[1] += 1
            print(f"{names[1]} won the game with {player_2[1]} throws!")
            break
        elif board[second_r][second_c] == "D":
            res = corresponding_nums(second_r, second_c)
            player_2[0] -= (res * 2)

        elif board[second_r][second_c] == "T":
            res = corresponding_nums(second_r, second_c)
            player_2[0] -= (res * 3)

        else:
            player_2[0] -= int(board[second_r][second_c])

    player_2[1] += 1

    if check_win(player_2):
        print(f"{names[1]} won the game with {player_2[1]} throws!")
        break
