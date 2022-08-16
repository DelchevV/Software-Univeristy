def factorial(number):
    factorial_list = []
    result = 1
    for num in range(number, 0, -1):
        factorial_list.append(num)
    for item in factorial_list:
        result = result * item
    return result


def division_of_factorial(first_factorial, second_factorial):
    division = first_factorial / second_factorial
    return f"{division:.2f}"


first_number = int(input())
second_number = int(input())
print(division_of_factorial(factorial(first_number), factorial(second_number)))
