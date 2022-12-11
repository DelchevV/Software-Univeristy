class reverse_iter:
    def __init__(self, iterable_obj):
        self.iter_obj = list(iterable_obj)

    def __iter__(self):
        return self

    def __next__(self):
        if not self.iter_obj:
            raise StopIteration

        return self.iter_obj.pop()


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
