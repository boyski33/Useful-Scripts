class Stack(list):
    def __init__(self):
        super().__init__()
        self.max_nums = [0] # we need another stack for max nums since otherwise it times out for too many instances

    def push(self, item):
        self.append(item)
        if item >= self.max_nums[-1]:
            self.max_nums.append(item)
            

    def is_empty(self):
        return not self

    def del_top(self):
        if self[-1] == self.max_nums[-1]:
            self.max_nums.__delitem__(-1)
        self.__delitem__(-1)

    def find_max(self):
        return self.max_nums[-1]

# main function where we test the class
s = Stack()

c = int(input())
for i in range(c):
    current = input()
    comm = int(current[0])
    if comm == 1:
        num = current.split(" ")[1]
        s.push(int(num))
    elif comm == 2:
        s.del_top()
    elif comm == 3:
        print(s.find_max())
