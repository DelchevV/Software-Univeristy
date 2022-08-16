last_number=int(input())
delimeter= '->'

for number in range(1, last_number + 1):
    sum_of_digit = 0
    for digit in str(number):
        sum_of_digit+=int(digit)
    if sum_of_digit==5 or sum_of_digit==7 or sum_of_digit==11:
        print(f"{number} {delimeter} True")
    else:
        print(f"{number} {delimeter} False")