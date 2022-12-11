seats = input().split(", ")
first_line_numbers = list(map(int, input().split(", ")))
second_line_numbers = list(map(int, input().split(", ")))

rotations = 0
matched_seats = []

while True:
    if rotations == 10 or len(matched_seats) == 3:
        break

    first_num = first_line_numbers.pop(0)
    second_num = second_line_numbers.pop(-1)
    ch = chr(first_num + second_num)
    first_seat = str(first_num) + ch
    second_seat = str(second_num) + ch

    if first_seat in seats:
        if first_seat not in matched_seats:
            matched_seats.append(first_seat)
    elif second_seat in seats:
        if second_seat not in matched_seats:
            matched_seats.append(second_seat)
    else:
        first_line_numbers.append(first_num)
        second_line_numbers.insert(0, second_num)

    rotations += 1

print(f'Seat matches: {", ".join(matched_seats)}')
print(f"Rotations count: {rotations}")
