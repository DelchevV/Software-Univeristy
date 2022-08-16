def is_perfect(number):
    approved_numbers = []
    for numb in range(1, number + 1):
        if number % numb == 0:
            approved_numbers.append(numb)
    sum_of_approved_numbers = sum(approved_numbers) / 2
    if sum_of_approved_numbers == number:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")


input_number = int(input())
is_perfect(input_number)
