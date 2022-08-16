lines=int(input())
sum=0
for line in range(lines):
    current_letter=input()
    sum+=ord(current_letter)
print(f"The sum equals: {sum}")