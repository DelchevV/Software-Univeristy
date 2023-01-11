import sys


class PythonList:
    def __init__(self, *args):
        self.__data = [*args]

    def append(self, value):
        self.__data.append(value)
        return self.__data

    def remove(self, index):
        if 0 <= index <= len(self.__data):
            return self.__data.pop(index)

    def get(self, index):
        if 0 <= index <= len(self.__data):
            return self.__data[index]

    def extend(self, iterable):
        self.__data.extend(iterable)
        return self.__data

    def insert(self, index, value):
        self.__data.insert(index, value)
        return self.__data

    def pop(self):
        return self.__data.pop()

    def clear(self):
        self.__data = []

    def index(self, value):
        for el in self.__data:
            if el == value:
                return self.__data.index(el)

    def count(self, value):
        return self.__data.count(value)

    def reverse(self):
        return list(reversed(self.__data))

    def copy(self):
        return self.__data.copy()

    def size(self):
        return len(self.__data)

    def add_first(self, value):
        self.__data.insert(0, value)
        return self.__data

    def dictionize(self):
        diction = {}
        for index in range(0, len(self.__data), 2):
            if index + 1 < len(self.__data):
                diction[self.__data[index]] = self.__data[index + 1]
            else:
                diction[self.__data[index]] = " "

        return diction

    def sum(self):
        sum = 0
        for el in self.__data:
            if isinstance(el, int) or isinstance(el, float):
                sum += el
            else:
                sum += len(el)

        return sum

    def overbound(self):
        biggest_dict={}
        biggest_value = -sys.maxsize
        for el in self.__data:
            if isinstance(el, int) or isinstance(el, float):
                if el > biggest_value:
                    biggest_value = el
                    index = self.__data.index(el)
                    biggest_dict[el]=index
            else:
                if len(el)>biggest_value:
                    biggest_value=len(el)
                    index=self.__data.index(el)
                    biggest_dict[len(el)]=index

        biggest_el_index=0
        for key, value in biggest_dict.items():
            biggest_el_index=0
            current_biggest=-sys.maxsize
            if key > current_biggest:
                current_biggest=key
                biggest_el_index=value

        return biggest_el_index




