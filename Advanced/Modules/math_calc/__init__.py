def calculation(info):
    def add():
        return num1 + num2

    def sub():
        return num1 - num2

    def div():
        if num2 != 0:
            return num1 / num2
        else:
            return "Division by 0"

    def mul():
        return num1 * num2

    def powing():
        return num1 ** num2

    info = info.split()
    num1 = float(info[0])
    operator = info[1]
    num2 = float(info[2])

    if operator == "+":
        return add()
    elif operator == "-":
        return sub()
    elif operator == "^":
        return powing()
    elif operator == "/":
        return div()
    elif operator == '*':
        return mul()
