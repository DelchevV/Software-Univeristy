first_set=set(input().split())
second_set=set(input().split())
lines=int(input())
for line in range(lines):
    entry=input()
    numbers=entry.split()[2:]
    if "Add First" in entry:
        first_set=first_set.union(numbers)
    elif"Add Second" in entry:
        second_set=second_set.union(numbers)
    elif "Remove First" in entry:
        for num in numbers:
            if num in first_set:
                first_set.remove(num)
    elif "Remove Second" in entry:
        for num in numbers:
            if num in second_set:
                second_set.remove(num)
    elif "Check Subset" in entry:
        print("True" if first_set<second_set or second_set<first_set else "False")

print(', '.join(map(str,sorted(map(int,first_set)))))
print(', '.join(map(str,sorted(map(int,second_set)))))



