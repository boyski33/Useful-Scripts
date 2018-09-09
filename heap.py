class Heap(object):
    elements = []

    def __init__(self, *numbers):
        self.elements = []
        for num in numbers:
            self.insert_node(num)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return str(self.elements)

    def has_left_child(self, i):
        return len(self.elements) > 2 * i + 1

    def has_right_child(self, i):
        return len(self.elements) > 2 * i + 2

    def is_root(self, i):
        return i == 0

    def get_left_child(self, i):
        return self.elements[2 * i + 1] if self.has_left_child(i) else None

    def get_right_child(self, i):
        return self.elements[2 * i + 2] if self.has_right_child(i) else None

    def get_parent(self, i):
        return self.elements[(i - 1) // 2]

    def insert_node(self, value):
        self.elements.append(value)
        i = len(self.elements) - 1
        while self.elements[i] > self.get_parent(i):
            self.swap(i, (i - 1) // 2)
            i = (i - 1) // 2
            if i == 0:
                break

    def swap(self, first, second):
        self.elements[first], self.elements[second] = self.elements[second], self.elements[first]

