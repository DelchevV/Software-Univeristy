keys = [int(a) for a in input().split()]
treasure = []
treasure_dict = {}
while True:
    result = ""
    index = 0
    text = input()
    if text == "find":
        break
    for ch in text:
        if index >= len(keys):
            index = 0
        symbol = ord(ch) - keys[index]
        result += chr(symbol)
        index += 1
    treasure.append(result)

for item in treasure:
    split_by_name = item.split("&")
    name = split_by_name[1]
    start_coord = item.index("<")
    end_coord = item.index(">")
    coordinate = item[start_coord + 1:end_coord]
    treasure_dict[name] = coordinate

for type, coordinates in treasure_dict.items():
    print(f"Found {type} at {coordinates}")
