first_player_egs=int(input())
second_player_egs=int(input())
command=input()
while command!="End of battle":
    if command=="one":
        second_player_egs-=1
    elif command=="two":
        first_player_egs-=1
    if first_player_egs<=0 or second_player_egs<=0:
        break
    command=input()
if command=="End of battle":
    print(f"Player one has {first_player_egs} eggs left.")
    print(f"Player two has {second_player_egs} eggs left.")
else:
    if first_player_egs<=0:
        print(f"Player one is out of eggs. Player two has {second_player_egs} eggs left.")
    elif second_player_egs<=0:
        print(f"Player two is out of eggs. Player one has {first_player_egs} eggs left.")
