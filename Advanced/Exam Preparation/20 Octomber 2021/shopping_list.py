def shopping_list(budget, **kwargs):
    products = []
    result = ''

    if budget < 100:
        return "You do not have enough budget."

    for p_name, cost in kwargs.items():

        current_sum = cost[0] * cost[1]
        if current_sum <= budget and len(products) < 5:
            result += f'You bought {p_name} for {current_sum:.2f} leva.' + '\n'
            budget -= current_sum

            if p_name not in products:
                products.append(p_name)

    return result


print(shopping_list(100,
                    microwave=(70, 2),
                    skirts=(15, 4),
                    coffee=(1.50, 10),
                    ))

print()
print(shopping_list(20,
                    jeans=(19.99, 1),
                    ))
print()
print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))

