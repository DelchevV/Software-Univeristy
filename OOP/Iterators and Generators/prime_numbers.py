def get_primes(numbers):

    for i in numbers:

        c = 0

        for j in range(1, i):

            if i % j == 0:

                c += 1

        if c == 1:

            yield i




print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))

