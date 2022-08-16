is_happy_year=False
year=int(input())
while not is_happy_year:
    year+=1
    current_year=set()

    for i in range(len(str(year))):
        current_year.add(str(year)[i])
    if len(current_year)==len(str(year)):
        is_happy_year=True
print(year)
