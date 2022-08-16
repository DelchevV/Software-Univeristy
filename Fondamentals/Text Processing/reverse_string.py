while True:
    entry = input()
    if entry == "end":
        break
    result = ""
    for ch in reversed(entry):
        result+=ch
    print(entry + " = " + result)
