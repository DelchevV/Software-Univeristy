sold_games=int(input())
heartstone=0
fortnite=0
overwatch=0
others=0
for game in range(sold_games):
    game_name=input()
    if game_name=="Hearthstone":
        heartstone+=1
    elif game_name=="Fornite":
        fortnite+=1
    elif game_name=="Overwatch":
        overwatch+=1
    else:
        others+=1
print(f"Hearthstone - {heartstone/sold_games*100:.2f}%")
print(f"Fornite - {fortnite/sold_games*100:.2f}%")
print(f"Overwatch - {overwatch/sold_games*100:.2f}%")
print(f"Others - {others/sold_games*100:.2f}%")