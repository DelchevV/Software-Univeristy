data=input().upper()

result=""
letters=""
numbers=""
for index in range(len(data)):
    if not data[index].isdigit():
        letters+=data[index]

    elif data[index].isdigit():
        for check_for_next_ch in range(index,len(data)):
            if not data[check_for_next_ch].isdigit():
                break
            numbers+=str(data[check_for_next_ch])

        result+=letters*int(numbers)
        letters=""
        numbers=""
print(f"Unique symbols used: {len(set(result))}")
print(result)


