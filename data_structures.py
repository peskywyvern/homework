# Create a limited stack (with maxsize) using dictionary


from abc import ABC


class DictStack:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.__items = {}

    def __repr__(self):
        return repr(self.__items)

    def push(self, key, item):
        if len(self.__items) >= self.maxsize:
            self.pop()
        self.__items.update({key: item})

    def pop(self):
        return self.__items.popitem()

    def reverse(self):
        items2 = self.__items.copy()
        new_dict = {}
        while items2:
            key, val = items2.popitem()
            new_dict.update({key: val})
        return new_dict

    def reverse_in_place(self):
        self.__items = self.reverse()

    def is_empty(self):
        return bool(len(self.__items))

    def is_full(self):
        return len(self.__items) == self.maxsize

    def get(self, search_key, default=None):
        for key, value in self.__items.items():
            if key == search_key:
                return value
        return default

    def set_default(self, key, default=None):
        if key in self.__items.keys():
            return self.__items[key]
        else:
            self.push(key, default)

    @property
    def size(self):
        return len(self.__items)


# Create an abstract data structure class for methods which could be applied to
# both stack and queue


class AbstractDataStructure(ABC):
    def __init__(self, maxsize):
        self.items = []
        self.maxsize = maxsize

    def reverse(self):
        new_items = []
        for i in self.items:
            new_items.insert(0, i)
        return new_items

    def reverse_in_place(self):
        self.items = self.reverse()

    def join(self, delimiter):
        string = ''
        for i, n in enumerate(self.items):
            if i != len(self.items) - 1:
                string = string + str(n) + delimiter
            else:
                string += str(n)
        return string

    def index(self, item):
        for i, n in enumerate(self.items):
            if n == item:
                return i

    def last_index(self, item):
        index = len(self.items) - 1
        while index >= 0:
            if item == self.items[index]:
                return index

    def sum(self):
        summ = 0
        for n in self.items:
            try:
                summ += n
            except TypeError:
                return 'List contains non-int object'
        return summ

    @property
    def size(self):
        return len(self.items)

    def is_empty(self):
        return bool(len(self.items))

    def is_full(self):
        return len(self.items) == self.maxsize


# LIFO


class Stack(AbstractDataStructure):
    def __init__(self, maxsize):
        super().__init__(maxsize)

    def __repr__(self):
        return repr(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()


# FIFO


class Queue(AbstractDataStructure):
    def __init__(self, maxsize):
        super().__init__(maxsize)

    def __repr__(self):
        return repr(self.items)

    def enqueue(self, element):
        if len(self.items) != self.maxsize:
            self.items.insert(0, element)
        else:
            self.items[0] = element

    def dequeue(self):
        self.items.pop()


