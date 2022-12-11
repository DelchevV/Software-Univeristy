import sys


jobs = list(map(int, input().split(", ")))
index = int(input())
cycles = 0
is_break = False
while True:
    smallest_num = sys.maxsize
    for job in jobs:
        if isinstance(job, int):
            if job < smallest_num:
                smallest_num = job

    for idx in range(len(jobs)):
        if jobs[idx] == smallest_num:
            cycles += jobs[idx]

            if idx == index:
                is_break = True
                break

            jobs[idx] = "-"
            continue
            
    if is_break:
        break

print(cycles)
