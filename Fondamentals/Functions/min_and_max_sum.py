input_string=input().split(" ")
numbers=[]
for num in input_string:
    numbers.append(int(num))
smallest=min(numbers)
biggest=max(numbers)
sum_of_numbers=sum(numbers)
print(f"The minimum number is {smallest}")
print(f"The maximum number is {biggest}")
print(f"The sum number is: {sum_of_numbers}")