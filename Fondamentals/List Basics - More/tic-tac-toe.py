first_line = input().split()
second_line = input().split()
third_line = input().split()


def who_is_winner_row(first_line):
    winner = ""
    if first_line[0] == "1":
        winner = "First"
    elif first_line[0] == "2":
        winner = "Second"
    return winner


def who_is_winner_column(first_line, second_line, third_line):
    winner = ""
    if first_line[0] == "1" and second_line[0] == "1" and third_line[0] == "1":
        winner = "First"
    elif first_line[1] == "1" and second_line[1] == "1" and third_line[1] == "1":
        winner = "First"
    elif first_line[2] == "1" and second_line[2] == "1" and third_line[2] == "1":
        winner = "First"

    elif first_line[0] == "2" and second_line[0] == "2" and third_line[0] == "2":
        winner = "Second"
    elif first_line[1] == "2" and second_line[1] == "2" and third_line[1] == "2":
        winner = "Second"
    elif first_line[2] == "2" and second_line[2] == "2" and third_line[2] == "2":
        winner = "Second"
    return winner


def who_is_winner_diagonal(first_line, second_line, third_line):
    winner = ""
    if first_line[0] == "1" and second_line[1] == "1" and third_line[2] == "1":
        winner = "First"
    elif first_line[2] == "1" and second_line[1] == "1" and third_line[0] == "1":
        winner = "First"

    if first_line[0] == "2" and second_line[1] == "12" and third_line[2] == "12":
        winner = "Second"
    elif first_line[2] == "2" and second_line[1] == "2" and third_line[0] == "2":
        winner = "Second"
    return winner


if  first_line[0] != "0" and first_line[0] == first_line[1] and first_line[0] == first_line[2]:
    print(f"{who_is_winner_row(first_line)} player won")
elif second_line[0] != "0" and second_line[0] == second_line[1] and second_line[0] == second_line[2]:
    print(f"{who_is_winner_row(second_line)} player won")
elif third_line[0] != "0" and third_line[0] == third_line[1] and third_line[0] == third_line[2]:
    print(f"{who_is_winner_row(third_line)} player won")

elif  first_line[0] != "0" and first_line[0] == second_line[0] and first_line[0] == third_line[0]:
    print(f"{who_is_winner_column(first_line, second_line, third_line)} player won")
elif  first_line[1] != "0" and first_line[1] == second_line[1] and first_line[1] == third_line[1]:
    print(f"{who_is_winner_column(first_line, second_line, third_line)} player won")
elif  first_line[2] != "0" and first_line[2] == second_line[2] and first_line[2] == third_line[2]:
    print(f"{who_is_winner_column(first_line, second_line, third_line)} player won")

elif first_line[0] != "0" and first_line[0] == second_line[1] and first_line[0] == third_line[2]:
    print(f"{who_is_winner_diagonal(first_line, second_line, third_line)} player won")
elif first_line[2] != "0" and first_line[2] == second_line[1] and first_line[2] == third_line[0]:
    print(f"{who_is_winner_diagonal(first_line, second_line, third_line)} player won")
else:
    print("Draw!")
