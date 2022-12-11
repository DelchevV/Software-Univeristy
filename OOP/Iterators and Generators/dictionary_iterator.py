class dictionary_iter:
    def __init__(self, dictionary):
        self.values=list(dictionary.values())
        self.keys=list(dictionary.keys())

    def __iter__(self):
        return self

    def __next__(self):
        if not self.keys:
            raise StopIteration
        return (self.keys.pop(0),self.values.pop(0))




result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)

