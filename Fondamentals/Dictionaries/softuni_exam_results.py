examine = {}
submissions = {}

while True:
    data = input()
    if data == "exam finished":
        break
    if "banned" in data:
        data = data.split("-")
        name = data[0]
        del examine[name]
        continue
    data = data.split("-")
    username = data[0]
    language = data[1]
    points = int(data[2])
    if language not in submissions:
        submissions[language] = 1
    else:
        submissions[language] += 1
    if username not in examine:
        examine[username] = points

    else:
        if examine[username] <= points:
            examine[username] = points

print("Results:")
for key, value in examine.items():
    print(f'{key} | {value}')

print("Submissions:")
for key, value in submissions.items():
    print(f"{key} - {value}")
