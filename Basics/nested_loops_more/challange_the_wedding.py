men_count=int(input())
women_count=int(input())
max_tables=int(input())
counter=1
for men in range(1,men_count+1):
    for women in range(1,women_count+1):
        if counter>max_tables:
            break
        else:
            print(f"({men} <-> {women})", end=" ")
        counter+=1