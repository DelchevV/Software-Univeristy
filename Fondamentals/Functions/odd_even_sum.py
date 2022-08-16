def odd_even_sun(list_of_numbers):
    even_sum=0
    odd_sum=0
    for number in list_of_numbers:
        if number%2==0:
            even_sum+=number
        else:
            odd_sum+=number
    print(f"Odd sum = {odd_sum}, Even sum = {even_sum}")


number=input()
digits=[int(d) for d in str(number)]
odd_even_sun(digits)


