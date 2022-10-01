lines = int(input())

students_dict = {}

for line in range(lines):
    name, mark = input().split()
    if name not in students_dict:
        students_dict[name] = []
    students_dict[name].append(float(mark))


for key, value in students_dict.items():
    grades=[" ".join(str(f'{v:.2f}') for v in value)]
    avg=sum(value)/len(value)
    print(f'{key} -> {" ".join(grades)} (avg: {avg:.2f})')