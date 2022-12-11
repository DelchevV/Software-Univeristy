class countdown_iterator:
    def __init__(self, count):
        self.numbers=[x for x in range(count+1)]

    def __iter__(self):
        return self
    def __next__(self):
        if not self.numbers:
            raise StopIteration
        return self.numbers.pop()

iterator = countdown_iterator(0)
for item in iterator:
    print(item, end=" ")

