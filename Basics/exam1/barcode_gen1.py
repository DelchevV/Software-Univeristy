start=input()
end=input()
first_digit_start=start[0]
first_digit_end=end[0]
second_digit_start = start[1]
second_digit_end = end[1]
third_digit_start = start[2]
third_digit_end = end[2]
forth_digit_start = start[3]
forth_digit_end = end[3]
for number1 in range(int(first_digit_start),int(first_digit_end)+1):
    for number2 in range(int(second_digit_start),int(second_digit_end)+1):
        for number3 in range(int(third_digit_start),int(third_digit_end)+1):
            for number4 in range(int(forth_digit_start),int(forth_digit_end)+1):
                if number1 % 2 != 0 and number2 % 2 != 0 and number3 % 2 != 0 and number4 % 2 != 0:
                    print(f"{number1}{number2}{number3}{number4}", end=" ")

