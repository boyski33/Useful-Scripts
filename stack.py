class Stack(list):
    def __init__(self, *items):
        super().__init__([*items])

    def push(self, item):
        self.append(item)

    def is_empty(self):
        return not self

s = Stack(1, 2, 3, 5)
s.pop()
print(s[-2])
