# Write a program that receives a sequence of numbers (a string containing integers separated by ", ") and prints the numbers sorted into lists of 10's in the format "Group of {group}'s: {list_of_numbers}".
# Examples:
# •	The numbers 2, 8, 4, and 10 fall into the group of 10's.
# •	The numbers 13, 19, 14, and 15 fall into the group of 20's.
# For more clarification, see the examples below.


numbers=list(map(int,input().split(', ')))

boundary=10
while len(numbers)!=0:
    current_range=[num for num in numbers if num<=boundary]
    for num in current_range:
        if num in numbers:
            numbers.remove(num)
    print(f"Group of {boundary}'s: {current_range}")
    boundary+=10