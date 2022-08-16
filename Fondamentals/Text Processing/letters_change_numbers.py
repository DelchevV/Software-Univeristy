data = input().split()
result = 0
for ele in data:
    current_result=0
    start_letter = ele[0]
    number = int(ele[1:-1])
    end_letter = ele[-1]
    if start_letter.isupper():
        division = ord(start_letter.upper()) - 64
        current_result = number / division
    elif start_letter.islower():
        multiply = ord(start_letter.upper()) - 64
        current_result = number * multiply

    if end_letter.isupper():
        subtract=ord(end_letter.upper()) - 64
        current_result-=subtract
    elif end_letter.islower():
        add=ord(end_letter.upper()) - 64
        current_result += add
    result+=current_result
print(f"{result:.2f}")