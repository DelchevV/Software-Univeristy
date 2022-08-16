count_of_numbers=int(input())
negatives=[]
positives=[]
for i in range(count_of_numbers):
    current_num=int(input())
    if current_num>=0:
        positives.append(current_num)
    else:
        negatives.append(current_num)
print(positives)
print(negatives)
print(f"Count of positives: {len(positives)}")
print(f"Sum of negatives: {sum(negatives)}")