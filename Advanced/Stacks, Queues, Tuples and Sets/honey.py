from collections import deque

bees_que = deque(map(int, input().split()))
nectar_stack = list(map(int, input().split()))
symbol_que = deque(input().split())
total_honey = 0

while bees_que and nectar_stack and symbol_que:
    if nectar_stack[-1] >= bees_que[0]:
        current_nectar = nectar_stack.pop()
        current_bee = bees_que.popleft()
    else:
        nectar_stack.pop()

        continue
    current_symbol = symbol_que.popleft()
    if current_symbol == "+":
        total_honey += abs(current_bee + current_nectar)
    elif current_symbol == "-":
        total_honey += abs(current_bee - current_nectar)
    elif current_symbol == "*":
        total_honey += abs(current_bee * current_nectar)
    elif current_symbol == "/":
        if current_nectar==0:
            total_honey+=0
        else:
            total_honey += abs(current_bee / current_nectar)

print(f'Total honey made: {total_honey}')
if nectar_stack:
    print(f'Nectar left: {", ".join(map(str, nectar_stack))}')
if bees_que:
    print(f'Bees left: {", ".join(map(str, bees_que))}')
