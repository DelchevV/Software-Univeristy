def fibonacci():
    sequence = [0, 1]
    while True:
        yield sequence[-2]
        sequence.append(sequence[-1] + sequence[-2])


generator = fibonacci()
for i in range(1):
    print(next(generator))
