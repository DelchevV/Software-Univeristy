food_quantity = input().split()
searched_products = input().split()
bakery_dictionary = {}
for index in range(0, len(food_quantity), 2):
    key = food_quantity[index]
    value = food_quantity[index + 1]
    bakery_dictionary[key] = int(value)

for searched in searched_products:
    if searched in bakery_dictionary.keys():
        quantity = bakery_dictionary.get(searched)
        product = searched
        print(f"We have {quantity} of {product} left")
    else:
        print(f"Sorry, we don't have {searched}")

