from collections import deque

males = list(map(int, input().split()))
females = deque(map(int, input().split()))
matches = 0

while females and males:

    if females[0] <= 0 or males[-1] <= 0:
        if females[0] <= 0 and males[-1] > 0:
            females.popleft()
        if males[-1] <= 0 and females[0] > 0:
            males.pop()
        continue

    elif females[0] % 25 == 0 or males[-1] % 25 == 0:
        if females[0] % 25 == 0:
            females.popleft()
            if females:
                females.popleft()

        if males[-1] % 25 == 0:
            males.pop()
            if males:
                males.pop()

    elif females[0] == males[-1]:
        females.popleft()
        males.pop()
        matches += 1

    else:
        males[-1] -= 2
        females.popleft()

print(f'Matches: {matches}')
if males:
    print(f'Males left: {", ".join(map(str, reversed(males)))}')
else:
    print('Males left: none')

if females:
    print(f'Females left: {", ".join(map(str, females))}')
else:
    print('Females left: none')
