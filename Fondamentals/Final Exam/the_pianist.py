num_of_pieces=int(input())
pieces={}
for num in range(num_of_pieces):
    entry=input().split("|")
    piece=entry[0]
    composer=entry[1]
    key=entry[2]
    pieces[piece]=[composer,key]


def add_func(masterpiece, producer, keys, pieces_dict):
    if masterpiece in pieces_dict:
        print(f"{masterpiece} is already in the collection!")
    else:
        pieces_dict[masterpiece]=[producer,keys]
        print(f"{masterpiece} by {producer} in {keys} added to the collection!")
    return pieces_dict


def remove_func(masterpiece, pieces_dict):
    if masterpiece in pieces_dict:
        del pieces_dict[masterpiece]
        print(f"Successfully removed {masterpiece}!")
    else:
        print(f"Invalid operation! {masterpiece} does not exist in the collection.")
    return pieces_dict


def change_func(masterpiece, new_key, pieces_dict):
    if masterpiece in pieces_dict:
        pieces_dict[masterpiece][1]=new_key
        print(f"Changed the key of {masterpiece} to {new_key}!")
    else:
        print(f"Invalid operation! {masterpiece} does not exist in the collection.")
    return pieces_dict


while True:
    entry=input().split("|")
    command=entry[0]
    if command=="Stop":
        break
    if command=="Add":
        piece = entry[1]
        composer = entry[2]
        key = entry[3]
        pieces=add_func(piece,composer,key,pieces)
    elif command=="Remove":
        piece=entry[1]
        pieces=remove_func(piece,pieces)
    elif command=="ChangeKey":
        piece=entry[1]
        n_key=entry[2]
        pieces=change_func(piece,n_key,pieces)

for key in pieces:
    print(f"{key} -> Composer: {pieces[key][0]}, Key: {pieces[key][1]}")

