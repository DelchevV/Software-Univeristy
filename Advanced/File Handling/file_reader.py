numbers_sum = 0

with open('sources/numbers.txt', 'r') as numbers:
    try:
        for line in numbers:
            numbers_sum += int(line.strip())
    except TypeError:
        print("This isn't a num")
print(numbers_sum)
