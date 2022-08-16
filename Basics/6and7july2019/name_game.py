command=input()
points=0
first_player_points=0
first_player_name=""
second_player_points=0
second_player_name=""
counter=0
while command!="Stop":
    for character in command:
        character=ord(character)
        guess=int(input())
        if guess==character:
            points+=10
        else:
            points+=2
    if counter==0:
        first_player_points=points
        first_player_name=command
    elif counter==1:
        second_player_points=points
        second_player_name=command
    points = 0
    counter+=1
    command = input()
if first_player_points==second_player_points:
    print(f"The winner is {second_player_name} with {second_player_points} points!")
elif first_player_points>second_player_points:
    print(f"The winner is {first_player_name} with {first_player_points} points!")
elif second_player_points>first_player_points:
    print(f"The winner is {second_player_points} with {second_player_points} points!")