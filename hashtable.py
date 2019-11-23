from data_structures1 import *


class HashTable:
    def __init__(self, table_size=5):
        self.size = table_size
        self.buckets = [LinkedList() for _ in range(self.size)]
        self.keys = {}

    def hash(self, key):
        return key % self.size

    def insert(self, key, value):
        hash_key = self.hash(key)
        self.buckets[hash_key].push(value)

    def to_list(self):
        objects =[]
        for i, obj in enumerate(self.buckets):
            if obj.head:
                objects.append(obj.to_list())
            else:
                objects.append([obj.head])
        return objects

    def __repr__(self):
        return repr(self.to_list())

a = HashTable()
a.insert(23, 'Jane')
a.insert(23, 'Justin')
a.insert(24, 'Phil')
a.insert(20, 'Steph')
print(a)