from collections import deque

pizzas = deque(map(int, input().split(", ")))
employees = list(map(int, input().split(", ")))
total_pizzas = 0

while pizzas and employees:
    current_pizza = pizzas.popleft()
    if current_pizza<=0 or current_pizza>10:
        continue

    current_employee=employees.pop()
    if current_pizza<=current_employee:
        total_pizzas+=current_pizza
    elif current_pizza>current_employee:
        total_pizzas+=current_employee
        pizzas.appendleft(current_pizza-current_employee)

if pizzas:
    print(f'Not all orders are completed.')
    print(f'Orders left: {", ".join(map(str, pizzas))}')
else:
    print('All orders are successfully completed!')
    print(f'Total pizzas made: {total_pizzas}')
    print(f'Employees: {", ".join(map(str, employees))}')


