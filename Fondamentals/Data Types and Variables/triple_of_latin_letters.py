letters=int(input())
for i in range(letters):
    for z in range(letters):
        for b in range(letters):
            print(f"{chr(97+i)}{chr(97+z)}{chr(97+b)}")