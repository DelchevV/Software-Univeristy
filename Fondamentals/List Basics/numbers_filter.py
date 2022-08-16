EVEN = 'even'
ODD = 'odd'
NEGATIVE = 'negative'
POSITIVE = 'positive'
count_of_numbers = int(input())
numbers = []
filtered_numbers = []
for num in range(count_of_numbers):
    current_number = int(input())
    numbers.append(current_number)
command = input()
for i in numbers:
    if command == EVEN and i % 2 == 0 or \
            command == EVEN and i < 0 or \
            command == ODD and i % 2 != 0 or \
            command == ODD and i < 0 or \
            command == NEGATIVE and i < 0 or \
            command == POSITIVE and i >= 0:
        filtered_numbers.append(i)
print(filtered_numbers)
