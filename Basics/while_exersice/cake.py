width=int(input())
length=int(input())
total_cake_piecec=width*length
cake_is_over=False
command=input()
while command != "STOP":
    current_number_of_pieces=int(command)
    total_cake_piecec -= current_number_of_pieces
    if total_cake_piecec < 0:
        cake_is_over = True
        break
    command=input()
if cake_is_over:
    print(f"No more cake left! You need {abs(total_cake_piecec)} pieces more.")
else:
    print(f"{total_cake_piecec} pieces are left." )