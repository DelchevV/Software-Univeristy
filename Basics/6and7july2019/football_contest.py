club_name=input()
games=int(input())
havent_played=False
points=0
wins=0
losses=0
draws=0
if games<=0:
    havent_played=True
for game in range(games):
    result=input()
    if result=="W":
        wins+=1
    elif result=="D":
        draws+=1
    elif result=="L":
        losses+=1
points=wins*3+draws*1
if havent_played:
    print(f"{club_name} hasn't played any games during this season.")
else:
    print(f"{club_name} has won {points} points during this season.")
    print("Total stats:")
    print(	f"## W: {wins}")
    print(f"## D: {draws}" )
    print(f"## L: {losses}" )
    print(f"Win rate: {wins/games*100:.2f}%")