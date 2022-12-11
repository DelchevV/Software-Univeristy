def shopping_cart(*args):
    products = {
        'Soup': [],
        'Pizza': [],
        'Dessert': []
    }
    for element in args:
        if element == "Stop":
            break

        meal, product = element

        if meal == "Pizza":
            if len(products[meal]) < 4 and product not in products[meal]:
                products[meal].append(product)

        elif meal == "Soup":
            if len(products[meal]) < 3 and product not in products[meal]:
                products[meal].append(product)
        elif meal == "Dessert":
            if len(products[meal]) < 2 and product not in products[meal]:
                products[meal].append(product)
    result = sorted(products.items(), key=lambda x: (-len(x[1]), x[0]))

    final_print = ''

    if len(products['Soup']) != 0 or len(products["Pizza"]) != 0 or len(products["Dessert"]) != 0:

        for res in result:
            final_print += f'{res[0]}:' + '\n'
            for prod in sorted(res[1], key=lambda x: x):
                final_print += f' - {prod}' + '\n'

        return final_print
    else:
        return 'No products in the cart!'


print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))
