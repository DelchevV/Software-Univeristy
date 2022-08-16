numbers=list(map(int,input().split()))
while True:
    data=input().split()
    command=data[0]
    if command=="end":
        break
    if command=="swap":
        first_index = int(data[1])
        second_index = int(data[2])
        numbers[first_index], numbers[second_index] = numbers[second_index], numbers[first_index]
    elif command=="multiply":
        first_index = int(data[1])
        second_index = int(data[2])
        product=numbers[first_index]*numbers[second_index]
        numbers[first_index]=product
    elif command=="decrease":
        numbers=[num-1 for num in numbers]
result=list(map(str,numbers))
print(", ".join(result))