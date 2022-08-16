# You will receive a string with even integers, separated by a "@" - this is our neighborhood. After that, a series of Jump commands will follow until you receive "Love!". Every house in the neighborhood needs a certain number of hearts delivered by Cupid so it can celebrate Valentine's day. The integers in the neighborhood indicate those needed hearts.
# Cupid starts at the position of the first house (index 0) and must jump by a given length. The jump commands will be in this format: "Jump {length}".
# Every time he jumps from one house to another, the needed hearts for the visited house are decreased by 2:
# •	If the needed hearts for a certain house become equal to 0, print on the console "Place {house_index} has Valentine's day."
# •	If Cupid jumps to a house where the needed hearts are already 0, print on the console "Place {house_index} already had Valentine's day."
# •	Keep in mind that Cupid can have a larger jump length than the size of the neighborhood, and if he does jump outside of it, he should start from the first house again (index 0)
# For example, we are given this neighborhood: 6@6@6. Cupid is at the start and jumps with a length of 2. He will end up at index 2 and decrease the needed hearts by 2: [6, 6, 4]. Next, he jumps again with a length of 2 and goes outside the neighborhood, so he goes back to the first house (index 0) and again decreases the needed hearts there: [4, 6, 4].

def jump_func(start, house, ):
    already_had = False
    if start < len(house):
        if house[start] <= 0:
            print(f"Place {start} already had Valentine's day.")
            already_had = True
        if not already_had:
            house[start] -= 2
            if house[start] <= 0:
                print(f"Place {start} has Valentine's day.")
        pass
    return house


def validator_func(jump, start_position, house):
    if jump + start_position < len(house):
        start_position += jump_len
    else:
        start_position = 0
    return start_position


def final_print(house):
    houses_had_valentine = 0
    for element in house:
        if element <= 0:
            houses_had_valentine += 1
    print(f"Cupid's last position was {start_index}.")
    if houses_had_valentine == len(house):
        print("Mission was successful.")
    else:
        missed_houses = len(house) - houses_had_valentine
        print(f"Cupid has failed {missed_houses} places.")


houses = (list(map(int, input().split("@"))))
start_index = 0
while True:
    data = input().split()
    command = data[0]
    if command == "Love!":
        break
    if command == "Jump":
        jump_len = int(data[1])
        start_index = validator_func(jump_len, start_index, houses)
        houses = jump_func(start_index, houses)

final_print(houses)
