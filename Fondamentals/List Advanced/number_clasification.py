# Using a list comprehension, write a program that receives numbers, separated by comma and space ", ", and prints all the positive, negative, even, and odd numbers on separate lines as shown below.
# Note: Zero is counted for a positive number


number_list=list(map(int,input().split(', ')))
positive_numbers_list=[num for num in number_list if num>=0]
negative_numbers_list=[num for num in number_list if num<0]
even_numbers_list=[num for num in number_list if num%2==0]
odd_numbers_list=[num for num in number_list if num%2!=0]
positive_numbers=str(positive_numbers_list)[1:-1]
negative_numbers=str(negative_numbers_list)[1:-1]
even_numbers=str(even_numbers_list)[1:-1]
odd_numbers=str(odd_numbers_list)[1:-1]
print(f"Positive: {positive_numbers}")
print(f"Negative: {negative_numbers}")
print(f"Even: {even_numbers}")
print(f"Odd: {odd_numbers}")
