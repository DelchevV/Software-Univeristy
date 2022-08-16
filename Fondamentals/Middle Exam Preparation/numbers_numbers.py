numbers = list(map(int, input().split()))
average_value = sum(numbers) / len(numbers)
top_numbers = []
for top in numbers:
    if top > average_value:
        top_numbers.append(top)
top_numbers.sort(reverse=True)
if len(top_numbers)==0:
    print("No")
elif len(top_numbers)<5:
    top_numbers=list(map(str,top_numbers))
    print(" ".join(top_numbers))
else:
    top_5_numbers=[top_numbers[num] for num in range(5)]
    top_5_numbers=list(map(str,top_5_numbers))
    print(" ".join(top_5_numbers))


