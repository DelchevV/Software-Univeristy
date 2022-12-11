from fibonacci import *

while True:
    sequence = []
    info = input()

    if info == "Stop":
        break
    info = info.split()

    if info[0] == "Create":
        seq_length = int(info[2])
        sequence = create(seq_length)
        print(" ".join(map(str, sequence)))
    elif info[0] == "Locate":
        searched_idx = int(info[1])
        sequence = create(seq_length)
        print(locate(searched_idx, sequence))
