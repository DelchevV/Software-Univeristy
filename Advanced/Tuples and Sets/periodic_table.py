lines=int(input())
unique_chems=set()
for line in range(lines):
    entry=input().split()
    for chemical in entry:
        unique_chems.add(chemical)
for unique in unique_chems:
    print(unique)