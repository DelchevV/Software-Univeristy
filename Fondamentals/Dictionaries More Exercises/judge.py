exam_info={"contests":{},"participants":{}}
contest_dict="contests"
participant_dict="participants"

while True:
    data=input()
    if data=="no more time":
        break
    data=data.split(" -> ")
    name=data[0]
    contest=data[1]
    points=int(data[2])
    if contest not in exam_info[contest_dict]:
        exam_info[contest_dict][contest]={name:points}
    if name not in exam_info[contest_dict][contest]:
        exam_info[contest_dict][contest][name]=points
    else:
        if points > exam_info[contest_dict][contest][name]:
            exam_info[contest_dict][contest][name]=points


for key in exam_info[contest_dict]:
    print(f"{key}: {len(exam_info[contest_dict][key])} participants")
    counter = 1
    for k in exam_info[contest_dict][key]:
        print(f"{counter}. {k} <::> {exam_info[contest_dict][key][k]}")
        counter+=1


total = {}
for match, results in exam_info[contest_dict].items():
    for player, score in results.items():
        total[player] = total.get(player, 0) + score


result={k: v for k, v in sorted(total.items(), key=lambda item: item[1],reverse=True)}
counter=1
print(f'Individual standings:')
for key,value in result.items():
    print(f"{counter}. {key} -> {value}")
    counter+=1


