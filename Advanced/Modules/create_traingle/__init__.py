def triangle(size):
    for i in range(1, size + 1):
        for col in range(1, i + 1):
            print(col, end=' ')
        print()
    for i in range(size - 1, 0, -1):
        for col in range(1, i + 1):
            print(col, end=' ')
        print()


def square(size):

    for row in range(size):
        for col in range(size):
            print(col, end=' ')

        print()
