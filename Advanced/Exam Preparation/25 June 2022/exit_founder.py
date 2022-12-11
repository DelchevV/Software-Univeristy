rows=6
names=input().split(', ')
maze=[input().split()for row in range(rows)]
take_rest=[]
while True:

    p1,p2=input().strip("(").strip(")").split(', ')
    p1,p2=int(p1),int(p2)

    player=names.pop(0)
    if player=="rest":
        continue

    if maze[p1][p2]=='E':
        print(f"{player} found the Exit and wins the game!")
        break

    elif maze[p1][p2]=="T":
        print(f'{player} is out of the game! The winner is {names[0]}.')
        break

    elif maze[p1][p2]=="W":
        print(f'{player} hits a wall and needs to rest.')
        if player=="Tom":
            inserted_one="Jerry"
        else:
            inserted_one="Tom"
        names.insert(1,'rest')
        names.insert(2,inserted_one)

    names.append(player)


    


