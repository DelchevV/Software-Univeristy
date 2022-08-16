formatted_deck=input().split()
shuffling_times=int(input())
left_side=[]
right_side=[]
split_index=len(formatted_deck)//2

for shuffle in range(shuffling_times):
    shuffled_deck=[]
    left_side=formatted_deck[:split_index]
    right_side=formatted_deck[split_index:]
    for card in range(len(left_side)):
        shuffled_deck.append(left_side[card])
        shuffled_deck.append(right_side[card])
    formatted_deck=shuffled_deck
print(formatted_deck)
