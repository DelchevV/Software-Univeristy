def operate(operator, *args):
    def add():
        result = sum(args)
        return result

    def multiply():
        result = 1
        for num in args:
            result *= num
        return result

    def subtract():
        number_list = list(args)
        result = number_list.pop(0)
        for num in number_list:
            result -= num
        return result

    def divide():
        number_list = list(args)
        result = number_list.pop(0)
        for num in number_list:
            result /= num
        return result

    if operator=="+":
        return add()
    elif operator=='-':
        return subtract()
    elif operator=="*":
        return multiply()
    elif operator=="/":
        return divide()

print(operate('+',1,2,3))
print(operate("*", 3, 4))
print(operate("-", 3, 4,5))
print(operate("/", 3, 4))