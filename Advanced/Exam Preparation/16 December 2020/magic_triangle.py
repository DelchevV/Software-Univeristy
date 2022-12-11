from math import factorial


def get_magic_triangle(num):
    matrix = []

    for i in range(num):
        res = []

        for j in range(i + 1):
            res.append(factorial(i) // (factorial(j) * factorial(i - j)))

        matrix.append(res)

    return matrix


# Pascal's Triangle
get_magic_triangle(10)
