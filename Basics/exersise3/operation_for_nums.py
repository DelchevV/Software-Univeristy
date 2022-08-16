first_number=int(input())
second_number=int(input())
operator=input()
result=0
is_odd_even="odd"

if operator=="+" or operator=="-" or operator=="*":
    if operator=="+":
        result=first_number+second_number
    elif operator=="-":
        result=first_number-second_number
    else:
        result=first_number*second_number
    if result%2==0:
        is_odd_even="even"
    else:
        is_odd_even="odd"
    print(f"{first_number} {operator} {second_number} = {result} - {is_odd_even}")
if operator=="%" or operator=="/":
    if operator=="%":
        if second_number == 0:
            print(f"Cannot divide {first_number} by zero")
        else:
            result = first_number % second_number
            print(f"{first_number} % {second_number} = {result}")
    elif operator=="/":
        if second_number==0:
            print(f"Cannot divide {first_number} by zero")
        else:
            result=first_number/second_number
            print(f"{first_number} / {second_number} = {result:.2f}")