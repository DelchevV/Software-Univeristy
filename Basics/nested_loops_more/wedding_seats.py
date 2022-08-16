#65-90
#97-122

last_sector=ord(input())
rows_in_first_sector=int(input())
seats_in_odd_row=int(input())
seat_in_even_row=seats_in_odd_row+2
total_seats=0

for sectors in range(65,last_sector+1):
    for rows in range(1,rows_in_first_sector+1):
        print(chr(sectors), rows)
