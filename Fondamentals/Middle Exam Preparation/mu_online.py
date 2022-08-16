# You have initial health 100 and initial bitcoins 0. You will be given a string representing the dungeon's rooms. Each room is separated with '|' (vertical bar): "room1|room2|room3…"
# Each room contains a command and a number, separated by space. The command can be:
# •	"potion"
# o	You are healed with the number in the second part. But your health cannot exceed your initial health (100).
# o	First print: "You healed for {amount} hp."
# o	After that, print your current health: "Current health: {health} hp."
# •	"chest"
# o	You've found some bitcoins, the number in the second part.
# o	Print: "You found {amount} bitcoins."
# •	In any other case, you are facing a monster, which you will fight. The second part of the room contains the attack of the monster. You should remove the monster's attack from your health.
# o	If you are not dead (health <= 0), you've slain the monster, and you should print: "You slayed {monster}."
# o	If you've died, print "You died! Killed by {monster}." and your quest is over. Print the best room you've manage to reach: "Best room: {room}"
# If you managed to go through all the rooms in the dungeon, print on the following three lines:
# "You've made it!"
# "Bitcoins: {bitcoins}"
# "Health: {health}"

health=100
bitcoins=0
dungeons_room=input().split("|")

completed_dungeons=1


def potion_func(current_health, healing):

    if current_health+healing>100:
        print(f"You healed for {100-current_health} hp.")
        current_health=100
    else:
        print(f"You healed for {healing} hp.")
        current_health+=healing
    print(f"Current health: {current_health} hp.")
    return current_health


def chest_func(bitcoin, found_coins):
    bitcoin+=found_coins
    print(f"You found {found_coins} bitcoins.")
    return bitcoin


def enemy_func(current_health,enemy_name, enemy_damage,best_room):
    if current_health-enemy_damage<=0:
        print(f"You died! Killed by {enemy_name}.")
        print(f"Best room: {best_room}")
        exit()
    else:
        current_health-=enemy_damage
        print(f"You slayed {enemy_name}.")
    return current_health


while True:
    if health<=0 or completed_dungeons>=len(dungeons_room):
        break
    for room in range(len(dungeons_room)):
        current_room=dungeons_room[room].split()
        command=current_room[0]
        stats=int(current_room[1])
        # print(current_room)
        # print(command)
        # print(stats)
        if command=="potion":
            health=potion_func(health, stats)
        elif command=="chest":
            bitcoins=chest_func(bitcoins, stats)
        else:
            health=enemy_func(health,command,stats,completed_dungeons)
        completed_dungeons+=1
if health>0:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")
