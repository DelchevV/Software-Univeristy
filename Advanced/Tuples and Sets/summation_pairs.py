
numbers = list(map(int, input().split()))
target_sum = int(input())

while numbers:
    current_num = numbers.pop(0)
    for num in numbers:
        if num + current_num == target_sum:
            print(f"{current_num} + {num} = {target_sum}")
            numbers.remove(num)
            break
