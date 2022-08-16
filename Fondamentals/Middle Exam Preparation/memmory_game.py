elements = input().split()
moves = 0
while True:
    data = input().split()
    if data[0] == "end" or len(elements)==0:
        break
    moves += 1
    first_index = int(data[0])
    second_index = int(data[1])
    if first_index == second_index or first_index >= len(elements) or second_index >= len(elements) or first_index < 0 or second_index < 0:
        print("Invalid input! Adding additional elements to the board")
        middle_of_list = len(elements) // 2
        element_to_add = "-"+str(moves) + "a"
        elements.insert(middle_of_list, element_to_add)
        elements.insert(middle_of_list, element_to_add)
        continue
    if elements[first_index]==elements[second_index] and elements[first_index] in elements and elements[second_index] in elements:
        print(f"Congrats! You have found matching elements - {elements[first_index]}!")
        number_for_remove=elements[first_index]
        elements.remove(number_for_remove)
        elements.remove(number_for_remove)
    else:
        print("Try again!")
if len(elements)>0:
    print(f"Sorry you lose :(")
    print(" ".join(elements))
else:
    print(f"You have won in {moves} turns!")
