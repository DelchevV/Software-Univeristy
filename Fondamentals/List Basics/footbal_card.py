players_cards=input()
team_a=11
team_b=11
evicted_players=[]
is_terminated=False
player_card=players_cards.split(" ")
for player in player_card:
    if player in evicted_players:
        continue
    if player.startswith("A"):
        team_a-=1
    elif player.startswith("B"):
        team_b-=1
    if player not in evicted_players:
        evicted_players.append(player)
    if team_a<7 or team_b<7:
        is_terminated=True
        break
if is_terminated:
    print(f"Team A - {team_a}; Team B - {team_b}")
    print("Game was terminated")
else:
    print(f"Team A - {team_a}; Team B - {team_b}")