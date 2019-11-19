class PriorityNode:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority

    def __repr__(self):
        return f'{self.value}, priority: {self.priority}'


class PriorityQueue:
    def __init__(self):
        self.values = []

    def __repr__(self):
        return repr(self.values)

    def insert(self, item, priority):
        self.values.append(PriorityNode(item, priority))

    def get_highest_priority(self):
        highest_priority = max([value.priority for value in self.values])
        for value in self.values:
            if value.priority == highest_priority:
                return value

    def delete_highest_priority(self):
        self.values.remove(self.get_highest_priority())


