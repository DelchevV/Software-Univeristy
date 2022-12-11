def stock_availability(inventory, command, *args):
    if command == "sell":
        if len(args) > 0:

            if isinstance(args[-1], int):
                for _ in range(args[-1]):
                    inventory.pop(0)

            elif args[0].isalpha():
                for el in args:
                    try:
                        while True:
                            inventory.remove(el)
                    except ValueError:
                        pass

        else:
            inventory.pop(0)

    elif command == "delivery":
        for el in args:
            inventory.append(el)

    return inventory


# print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie", "banana"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
# print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
# print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
