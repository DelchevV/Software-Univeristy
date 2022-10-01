lines= int(input())

longest_len=0
longest_intersection=[]
for line in range(lines):
    first_set = set()
    second_set = set()

    first_range,second_range=input().split('-')

    first_start,first_end=first_range.split(",")
    for i in range(int(first_start),int(first_end)+1):
        first_set.add(i)

    second_start, second_end = second_range.split(",")
    for i in range(int(second_start),int(second_end)+1):
        second_set.add(i)

    intersection=first_set&second_set

    if len(intersection)>longest_len:
        longest_len=len(intersection)
        longest_intersection=intersection

print(f'Longest intersection is [{", ".join(map(str,longest_intersection))}] with length {longest_len}')